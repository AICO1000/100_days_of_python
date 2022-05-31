# test tes
print("Welcome to your weight body mass clinic")
age = input("How old are you?\n")
age_default = 90
new_age = int(age_default) - int(age)
days_rem = int(new_age) * 356
weeks_rem = int(new_age) * 52
months_rem = int(new_age) * 12
print(
    f"you have: {days_rem} days {weeks_rem} weeks and {months_rem} months before 90 years")
print("now check your bmi")
weight = input("what is your weight?\n")
height = input("what is your height?\n")
weight_new = int(weight)
height_new = float(height)**2
bmi = int(weight_new) / float(height_new)
print(round(bmi))
if bmi > 40:
    print("you are over weight")
elif bmi < 39:
    print("you are balanced")
