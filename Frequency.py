#BruteForce optimised
from typing import *
#Taking input string
input_string=input("Enter a string")
#Setting dictionary for frequency
freq:Dict[str,int]={}

for i in input_string:
    if freq.get(i):
        freq[i]+=1
    else:
        freq[i]=1

#Store it in sequence
print("Frequency of character",freq)


#Function approach
from collections import Counter

#Store unsequence
print("Frequency of character",Counter(freq))