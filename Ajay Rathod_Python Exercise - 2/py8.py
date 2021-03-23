# Create a program that write a .csv file
# From Program 6 read the .csv file and create a dictionary and after that write the values
# from that dictionary to .xls file.
# Read the dictionary and write in the “.xls” file
# Following will be the headers

from openpyxl import Workbook
import csv

# workbook class as workbook
workbooks = Workbook()
# worksheet to get started
worksheet = workbooks.active
# open the data.csv and read it
with open('data.csv', 'r') as file:
    for data in csv.reader(file):
        # This will append data one by one into file
        worksheet.append(data)
# After completed save the file
workbooks.save('datas11.xlsx')
