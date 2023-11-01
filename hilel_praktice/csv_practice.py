import csv


with open('airport-codes_csv.csv', 'r') as file:
    main = csv.reader(file)

    for i in main:
        print(i)

# print(main)