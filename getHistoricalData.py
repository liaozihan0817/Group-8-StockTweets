import json
def processJson(inputFile,outputFile):
	fin = open(inputFile,'r')
	fout = open(outputFile,'w')
	lines = fin.readlines()
	newLine = lines[lines.__len__() - 1: lines.__len__() - 8002: -1]
	#fout.write('[')
	
	for i in range(0, newLine.__len__() - 2):
		fout.writelines(newLine[i])
		#fout.write(',')
	fout.writelines(newLine[newLine.__len__() -1 ])
	#fout.write(']')

	fin.close()
	fout.close()

processJson('stocktwits_messages_2015-01-01-2015-12-31.json','EndOf2015_8k.json')
print('finish')