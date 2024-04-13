file01 = open('inputFile.txt','r')
#print(file01.read())
for line in file01:
    line = line.strip()
    if line[-1] == "P":
        print(line)
    
file01.close()