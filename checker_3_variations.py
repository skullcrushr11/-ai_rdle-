import random
import json
f=open(r"words.txt","r")
t=open(r'targets.txt','r')
data=f.read()
a=(random.choice(data))
print(a)
hidden_word=a
attempts=6
#To check for condition of word
def checker():
    u=input('enter guess:')
    subset_position=[]
    for i,j in zip(a,u):
        if i==j:
            subset_position.append('g')
        elif j in list(a):
            subset_position.append('y')
        else:
            subset_position.append('r')
    return subset_position
while attempts>0:
    print(checker())
    attempts-=1
            
            
    