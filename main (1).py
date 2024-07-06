#Write a Python program that takes a number as input from the user
#and prints the multiplication table for that number up to 10. 
#The output should be formatted in a clear and readable manner.

n=int(input("Enter a number"))
for i in range (11):
    m=n*i 
    print(n,"x",i,"=",m)