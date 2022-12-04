#Read data
inputList = []

with open('inputs\input3.txt') as f:
    inputList=f.read().splitlines()

#Part 1 

def splitRucksack(rucksack):
    rucksackMid = int(len(rucksack)/2)
    set1=rucksack[:rucksackMid]
    set2=rucksack[rucksackMid:]
    return set1,set2

def findDuplicateValSingle(set1,set2):    
    for char in set1:
        if char in set2:
            return char
        
def charPriority(char):
    if char.islower(): #a is ascii character 97 and has priority of 1
        return (ord(char)-96)
    else: #A is ascii character 65 and has priority of 27
        return (ord(char)-38)
    
prioritySum=0
    
for rucksack in inputList:
    compartmentLists=splitRucksack(rucksack)
    dupVal = findDuplicateVal(compartmentLists[0],compartmentLists[1])
    prioritySum+=charPriority(dupVal)
    
print(prioritySum)

#Part 2

def generateGroupList(inputList,groupSize):
    inc = 0
    groupList = []
    group = []
    for rucksack in inputList:
        group.append(rucksack)
        inc+=1
        if inc%groupSize==0:
            groupList.append(group)
            group=[]
    return groupList

def findDuplicateValUnlimited(set1,set2): 
    dupList = []
    for char in set1:
        if char in set2:
            dupList.append(char)
    return dupList
         
def findBadgeChar(group):
    dupList = findDuplicateValUnlimited(group[0],group[1])
    for char in dupList:
        if char in group[2]:
            return char
    
badgePrioritySum = 0
        
groupList = generateGroupList(inputList,3)
for group in groupList:
    dupVal = findBadgeChar(group)
    badgePrioritySum+=charPriority(dupVal)
    
print(badgePrioritySum)    