import json
def processJson(inputFile,outputFile):
	fin = open(inputFile,'r')
	fout = open(outputFile,'w')
	lines = fin.readlines()
	fout.write('[')
	for i in range(0,7998):
		fout.writelines(lines[i])
		fout.write(',')
	fout.writelines(lines[7999])
	fout.write(']')
	fin.close()
	fout.close()
processJson('EndOf2015_8k.json','sentimentList.json')
print('finish')