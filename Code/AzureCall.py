import requests
import json

URL1 = "https://atlas.microsoft.com/search/fuzzy/json?api-version=1.0&subscription-key="
URL2 = "&language=en-US&ResponseFormat=json&limit=1&query="
#Hides User Key

query = ""
def lookup(secret_key,address,city,country,zip_):
    key = secret_key
    valid_location = False
    query =str(address) + ", " + str(city) + ", " + str(country) + " " + str(zip_)
    #getting response
    response = requests.get(URL1+key+URL2+query)
    jsonData = json.loads(response.text)
    #print(json.dumps(jsonData, indent=4))
    try:
        results = jsonData["results"]
        addressData = results[0]["address"]
        #score is a value that correlates to how close the data is to the search, if too low we do not want our location changing
        scoreData = float(results[0]["score"]) 
        if ((scoreData)>=11):#change this number as you see fit
            try:
                address_json = str(addressData["streetNumber"]) + " " + addressData["streetName"]
            except:
                address_json = addressData["streetName"]
            ###########
            city_json = addressData["municipality"]
            zip_json =  str(addressData["postalCode"])
            country_json = addressData["countryCodeISO3"]
            valid_location = True
            ###########
        else:
            ###########
            address_json = address
            city_json = city
            country_json = country
            zip_json =  zip_
            valid_location = False
            ###########
    except:
        ###########
        address_json = address
        city_json = city
        country_json = country
        zip_json =  zip_
        valid_location = False
        ###########
    return address_json,city_json,country_json,zip_json,valid_location
    
