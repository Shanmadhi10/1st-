#Write a Python program that defines a function to convert temperatures from Fahrenheit to Celsius.
#The program should prompt the user to enter a temperature in Fahrenheit, 
#call the function to convert it to Celsius, and then display the result.C = (F - 32) × 5/9

f=int(input("enter a temperature in Fahrenheit"))
def cel():
    c=(f-32)*(5/9)
    print(c)
    
cel()