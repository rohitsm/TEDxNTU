import csv

csvFile = 'Speech_2008.csv'
csvFile_2 = 'Speech2_2008.csv'

def removeNonAscii(s): 
	return "".join(i for i in s if ord(i)<128)

rowNum = 0
with open(csvFile, 'rU') as x:
	csvData = csv.reader(x, delimiter=',')
	
	with open(csvFile_2, 'w') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow( ('Id', 'Author', 'Comment', 'Polarity') )
		for line in csvData:
			if rowNum != 0:
				csvwriter.writerow(	(removeNonAscii(str(rowNum)).decode('UTF-8'), \
									removeNonAscii(line[1]).decode('UTF-8'),  \
									removeNonAscii(line[2].replace('\n', ' ')).decode('UTF-8'), \
									removeNonAscii(line[3]).decode('UTF-8')  \
									)
								   )
			rowNum += 1
	csvfile.close()
x.close()
		