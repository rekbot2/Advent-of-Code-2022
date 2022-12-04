#Read and Process data
inputList = []

with open('inputs\input4.txt') as f:
    inputList=f.read().splitlines()
    
inputClean = []

for pair in inputList:
    elfPair = pair.split(',')    
    elfRange = []    
    for idRange in elfPair:
        elfRange.append(idRange.split('-'))
    inputClean.append(elfRange)

#Part 1

subsetPairs = 0

for pair in inputClean:
    set1 = set(range(int(pair[0][0]),int(pair[0][1])+1))
    set2 = set(range(int(pair[1][0]),int(pair[1][1])+1))
    
    if len(set1)<=len(set2) and set1.issubset(set2):
        subsetPairs+=1
    elif set2.issubset(set1):
        subsetPairs+=1
        
print(subsetPairs)    

#Part 2

intersectPairs = 0

for pair in inputClean:
    set1 = set(range(int(pair[0][0]),int(pair[0][1])+1))
    set2 = set(range(int(pair[1][0]),int(pair[1][1])+1))

    if len(set1.intersection(set2))>0:
        intersectPairs+=1
        
print(intersectPairs)