<h1>Azure Fuzzy Search</h1>

This python script uses Azure maps, specifically Azure Fuzzy search.

Need to input a csv file with No., Name, Address,City, Coutry, and zip. Also necesarry to have a MapsSandbox Azure liscence, and find your Primary Key
Script will call Azures FuzzySearch API call and will look through the excel sheet and will find the locations if they exist
Once found the correct information will be put into an output csv file. 
In all, this script standardizes location data in an output csv file

Do Not upload a csv file with too many entries, Azure MapsSandbox is a paid service and doing too many entries will cost a lot.
Also would try to limit how many rows are imputted at a time to not break the code

upload a file named AddressReader.csv as in the same folder, also upload a secrets.py file with your key

Made for AMS group

Made by William Beckhorn
