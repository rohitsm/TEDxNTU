import csv

csvFile = ''	# add name of input CSV file here
xmlFile = ''	# add name of output XML file here	


rowNum = 0
with open(csvFile, 'rU') as x:
	csvData = csv.reader(x, delimiter=',')
	
	xmlData = open(xmlFile, 'w')
	xmlData.write('<?xml version="1.0"?>' + "\n")
	xmlData.write('<comments>' + '\n')	#top level tag
	
	for line in csvData:
		if rowNum != 0:
			# XML structure:
			# <comment id="1" author="John_Smith">Blah blah </comment>
			
			xmlData.write(	'    ' + # preserve indentation
							'<comment ' +
							'id="' + str(rowNum) + '" ' +   
							'author="' + line[1] + '">' +
							line[2].replace('\n', ' ') + 		
							'</comment>' + '\n')
		rowNum += 1	

	xmlData.write('</comments>')
	xmlData.close()
		
