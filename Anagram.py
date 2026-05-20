#Solving with dictionary brute-force optimised O(M+N)
str1="silent"
str2="listen"

freq:dict={}
#Checking length
if len(str1)!=len(str2):
    #O(N)
    for i,j in zip(str1,str2):
       
       freq[i]=freq.get(i,0)+1
       freq[j]=freq.get(j,0)-1


print(all(i == 0 for i in freq))
