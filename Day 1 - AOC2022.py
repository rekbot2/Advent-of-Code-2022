#Read data
inputList = []

with open('inputs\input1.txt') as f:
    for line in f.readlines():
        inputList.append(line.strip())

#generalizable solution
import numpy as np

def elfCals(inputList,N):
    elfCalList=[]
    tot=0
    
    for val in inputList:
        if val!='':
            tot+=int(val)
        if val=='':
            elfCalList.append(tot)
            tot=0
    elfCalList.sort()
    return sum(elfCalList[-N:])
        
print(elfCals(inputList,1))
print(elfCals(inputList,3))