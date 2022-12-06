#Read data
with open('inputs\input5.txt') as f:
    inputList=f.read().splitlines()
    
#Cargo ship starting configuration
stackList = [[] for x in range(9)]

for line in inputList[0:8]:
    for x in range(9):
        targetChar = line[(4*x+1)]
        if targetChar!=" ":
            stackList[x].append(targetChar)

#Move commands - #,startStack to endStack
moveList = [command.strip('move ').split(' from ') for command in inputList[10:]]

#Part 1
for command in moveList:
    targetStacks = command[1].split(' to ')
    numToMove = int(command[0])
    
    moveToIndex = int(targetStacks[1])-1
    moveFromIndex = int(targetStacks[0])-1
    
    for i in range(numToMove):
        stackList[moveToIndex].insert(0,stackList[moveFromIndex].pop(0))
        
print(''.join([stack[0] for stack in stackList]))

#Part 2
for command in moveList:
    targetStacks = command[1].split(' to ')
    numToMove = int(command[0])
    
    moveToIndex = int(targetStacks[1])-1
    moveFromIndex = int(targetStacks[0])-1
    
    tempStack = []
    
    for i in range(numToMove):
        tempStack.append(stackList[moveFromIndex].pop(0))
    
    while len(tempStack)>0:
        stackList[moveToIndex].insert(0,tempStack.pop(-1))
        
print(''.join([stack[0] for stack in stackList]))