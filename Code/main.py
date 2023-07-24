from Address_Reader import read_csv_file, address, city, country, zip_, customer_no, name
from Write_Output import write_output
from AzureCall import lookup
from secrets import secrets
#main function
address_fin_list = []
city_fin_list =[]
country_fin_list =[]
zip_fin_list = []
valid_location_list =[]
#Hidden Key
secret_key = secrets.get('USER_KEY')

if __name__ == "__main__":
    file_name = "AddressReader"
    read_csv_file(file_name) 
    #for statement calls the Azure API as many times as there are addresses
    for i in range (0, len(address)):
        adress_fin,city_fin,country_fin,zip_fin,valid_location= lookup(secret_key,name[i], address[i],city[i],country[i],zip_[i])
        address_fin_list.append(adress_fin)
        city_fin_list.append(city_fin)
        country_fin_list.append(country_fin)
        zip_fin_list.append(zip_fin)
        valid_location_list.append(valid_location)
    #Just print statements used to check outputs

    #print(address[0:10])
    #print(address_fin_list)
    #print("\n")
    #print(city)
    #print(city_fin_list)
    #print("\n")
    #print(country)
    #print(country_fin_list)
    #print("\n")
    #print(zip_)
    #print(zip_fin_list)
    #print(valid_location_list)
    file_path = "outputLocations.csv"
    write_output(file_path, customer_no ,address_fin_list ,city_fin_list ,country_fin_list ,zip_fin_list ,valid_location_list) 

