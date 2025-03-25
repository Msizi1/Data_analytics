name = input("Enter your name: ")
weight = int(input("Enter weight(pounds): "))
height = int(input("Enter your height(inches): "))
BMI = (weight * 703) / (height * height)

print(BMI) 

if BMI > 0:
    if(BMI< 18.5):
        print(name + " ,You are underweight")
    elif(BMI< 24.9):
        print(name + " ,You are Normal weight")
    elif(BMI <29.9):
        print(name + " ,You are Overweight")
    elif(BMI < 34.9):
        print(name + " ,You are  Obese")
    elif(BMI < 39.9):
        print(name +" ,You are Severly Obese")
    elif(BMI > 40):
        print(name +" ,You are Morbidly Obese")
else: 
    print("Enter valid values")