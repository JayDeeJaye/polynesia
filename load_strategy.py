import csv

BASIC = {}
f = open('BasicStrategy_1.csv','r')
reader = csv.reader(f)
for line in reader:
    BASIC[(int(line[0]),int(line[1]))] = line[2]
f.close()

print("Basic stragety loaded into BASIC")