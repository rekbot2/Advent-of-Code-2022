#Read data
inputList = []

with open('inputs\input2.txt') as f:
    inputList=f.read().splitlines()

#Part 1 

#Rock = A,X
#Paper = B,Y
#Scissors = C,Z
winList=['A Y','B Z','C X']
loseList=['A Z','B X','C Y']
drawList=['A X','B Y','C Z']

playScore = {
    "X":1,
    "Y":2,
    "Z":3
}

loseScore = 0
winScore = 6
drawScore = 3

totScore = 0

for match in inputList:
    if match in winList:
        totScore+=winScore
        totScore+=playScore[match[-1]]
    elif match in loseList:
        totScore+=loseScore
        totScore+=playScore[match[-1]]
    else:                                          #assume draw
        totScore+=drawScore
        totScore+=playScore[match[-1]]

print(totScore)

#Part 2

totScore=0

loseScore = 0
winScore = 6
drawScore = 3

playScore = {
    "A":1,
    "B":2,
    "C":3
}

#Wins - A B, B C, C A -> score = match[0]+1 (but then C doesn't work)
#Draws - score = match[0]
#Losses - A C, B A, C B -> score = match[0]-1 (but then A doesn't work)

for match in inputList:
    if match[-1]=='X':
        totScore+=loseScore
        if match[0]=='A':
            totScore+=3
        else:
            totScore+=playScore[match[0]]-1
        
    elif match[-1]=='Y':
        totScore+=drawScore
        totScore+=playScore[match[0]]
        
    elif match[-1]=='Z':
        totScore+=winScore
        if match[0]=='C':
            totScore+=1
        else:
            totScore+=playScore[match[0]]+1
        
print(totScore)