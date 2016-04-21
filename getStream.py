import json
def processJson(inputFile,outputFile):
	fin = open(inputFile,'r')
	fout = open(outputFile,'w')
	lines = fin.readlines()
	for i in range(0,100):
		fout.writelines(lines[i])
	fout.write(']')
	fin.close()
	fout.close()
processJson('EndOf2015_8k.json','steamList.json')
print('finish')