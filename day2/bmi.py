height = float(input("Please input your height in meter: "))
weight = float(input ("Please input your weight in kg:"))
bmi = round(weight / (height * height),3)
print ("Your BMI number is: " + str(bmi))