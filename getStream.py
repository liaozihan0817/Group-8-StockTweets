import json
def processJson(inputFile,outputFile):
	fin = open(inputFile,'r')
	fout = open(outputFile,'w')
	lines = fin.readlines()
	fout.write('[')
	for i in range(0,9999):
		fout.writelines(lines[i])
		fout.write(',')
	fout.writelins(lines[100])
	fout.write(']')
	fin.close()
	fout.close()
processJson('EndOf2015_8k.json','steamList.json')
print('finish')