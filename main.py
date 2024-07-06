w=int(input("Enter weight in kg"))
h=int(input("Enter height in m"))
import math
bmi=w/h*h
if (bmi<18.5):
    print("underweight")
if (18.5 <= bmi) and (bmi< 24.9):
    print("Normal weight")
if  (25 <= bmi) and ( bmi < 29.9):
    print("Overweight")
if (bmi>=30):
    print("Obesity")

