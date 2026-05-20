#Solving brute force optimised
input_str=input("Enter a string")

result=""

for i in range(len(input_str)-1,-1,-1):
    result+=input_str[i]


print("Resultant string is",result)