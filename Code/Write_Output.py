import csv

#writes new CSV file with values created
def write_output(file_name, customer_no, address, city, country, zip_, valid_location):
    data = zip(customer_no, address, city, country, zip_, valid_location)
    
    def format_zip(zip_code): #formatting of zip and No. to not remove leading zeros. ex 00056
        return f"'{zip_code}"
    
    with open(file_name, mode = 'w', newline='',encoding = "utf-8" ) as file:
        writer = csv.writer(file)
        writer.writerow(["No.","Address", "City", "Country", "ZIP", "Valid Location"])
        for row in data:
            writer.writerow([format_zip(row[0]), row[1], row[2], row[3], format_zip(row[4]), row[5]])
    print(f"CSV file has been created")
        