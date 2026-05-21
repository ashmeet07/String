#Bruteforce Optimised

input_str=input("Enter a string")

freq:dict={}

for i in input_str:
    if freq.get(i): freq[i]+=1
    else: freq[i]=1
    
for i in freq:
    if freq[i]==1: print(i); break