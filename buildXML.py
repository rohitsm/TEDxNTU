import csv

csvFile = 'Speech_2008.csv'
xmlFile = 'Speech_2008.xml'


def removeNonAscii(s): 
	return "".join(i for i in s if ord(i)<128)

rowNum = 0
with open(csvFile, 'rU') as x:
	csvData = csv.reader(x, delimiter=',')
	
	xmlData = open(xmlFile, 'w')
	xmlData.write(removeNonAscii('<?xml version="1.0"?>' + "\n"))
	xmlData.write(removeNonAscii('<comments>' + '\n'))	#top level tag
	
	for line in csvData:
		if rowNum != 0:
			# XML structure:
			# <comment id="1" author="John_Smith">Blah blah </comment>
			
			comment = 	'    ' + \
						'<comment ' + \
						'id="' + str(rowNum) + '" ' + \
						'author="' + line[1] + '">' + \
						line[2].replace('\n', ' ') + \
						'</comment>' + '\n'
			xmlData.write(removeNonAscii(comment).decode('UTF-8'))
		rowNum += 1	

	xmlData.write(removeNonAscii('</comments>'))
	xmlData.close()
		