import csv

f = open('Nelisa Sales History.csv', 'rU')#opennibg the csv file

csv_f = csv.reader(f) #reading the csv file	

sales = []
for row in csv_f: #iterating in the csv file
	sales.append(row)

print sales
print len(sales)
f.close()