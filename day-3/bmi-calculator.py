height = float(input()) # in meters
weight = int(input()) # in kilograms

bmi = weight / (height ** 2)

evaluation = ""
if bmi < 18.5:
    evaluation = "you are underweight."
elif bmi < 25:
    evaluation = "you have a normal weight."
elif bmi < 30:
    evaluation = "you are slightly overweight."
elif bmi < 35:
    evaluation = "you are obese."
else:
    evaluation = "you are clinically obese."

print(f"Your BMI is {round(bmi, 5)}, {evaluation}")
