import csv
address = []
city = []
country = []
zip_ = []
customer_no = []
name =[]
#Reads csv File with Address, City, State, and ZIP file
def read_csv_file(file_name):
    try:
        with open(file_name, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            keep_track = int(0)
            for row in csv_reader: #seperates the columns of the rows into seperate Lists that are accesible
                if (keep_track != 0):
                    customer_no.append(row[0])
                    name.append(row[1])
                    address.append(row[2])
                    city.append(row[3])
                    country.append(row[4])
                    zip_.append(row[5])
                keep_track = keep_track + 1
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
