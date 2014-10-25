import csv

csvFile = 'Speech_2012.csv'
xmlFile = 'Speech_2012.xml'


def removeNonAscii(s): 
	return "".join(i for i in s if ord(i)<128)

rowNum = 0
with open(csvFile, 'rU') as x:
	csvData = csv.reader(x, delimiter=',')
	
	# Build XML structure as follows:

	# <comments>
	# 		<comment id="1" author="John Smith">Hello World!</comment>
	#     	<comment id="2" author="Bob Smith">Hello World Again!</comment>
	#         ...
	# </comments>

	xmlData = open(xmlFile, 'w')
	xmlData.write(removeNonAscii('<?xml version="1.0"?>' + "\n"))
	xmlData.write(removeNonAscii('<comments>' + '\n'))	#top level tag
	
	for line in csvData:
		if rowNum != 0:

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
		