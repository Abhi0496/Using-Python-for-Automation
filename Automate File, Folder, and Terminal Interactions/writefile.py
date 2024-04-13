file01 = open('inputFile.txt','r')
file02 = open('passFile.txt','w')
file03 = open('failFile.txt','w')

for line in file01:
    line = line.strip()
    if line[-1] == "P":
        file02.write(line+'\n')
    else:
        file03.write(line+'\n')
        
file01.close()
file02.close()
file03.close()