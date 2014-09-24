import csv

with open('tedxntu.csv', 'rU') as csvfile:
	fileInput = csv.reader(csvfile, delimiter=',')
	for line in fileInput:
		print line[6] + ','
		