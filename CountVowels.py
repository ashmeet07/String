#Taking input
input_str=input("Enter you string")
#Storing Variable
v=c=0
#O(n) solving things
for i in input_str:
    if i.lower() in "aeiou":
        v+=1
    else:
        c+=1

#Printing Result
print("Vowels =",v,"Consonants",c)