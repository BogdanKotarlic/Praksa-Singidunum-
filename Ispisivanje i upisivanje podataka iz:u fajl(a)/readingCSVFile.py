import csv 

with open ('csvFile.csv') as myFile:
	readFile = csv.reader(myFile, delimiter=',')
	for row in readFile:
		print(row)