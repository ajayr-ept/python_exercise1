# Create a program that write a .csv file
# From Program 6 read the .csv file and create a dictionary and after that write the values from
# that dictionary to .csv file.
# Read the dictionary and write in the “.csv” file
# Following will be the headers
import csv

with open('data.csv', 'r') as source:
    file = csv.reader(source)

    with open('akki.csv', 'a') as destination:
        destination_file = csv.writer(destination)

        for data in file:
            destination_file.writerow(data)
