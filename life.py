print("Life")
print("Know little about you".upper())
gender = input("What is your gender\n")
age = int(input("How old are?\n"))

days = age * 356
weeks = age * 52
months = age * 12

print(f"You are {days}days, {weeks}weeks, {months}months old")

if age == 15:
    print("You can drive")
elif age == 18:
    print("You can vote\nYou can smoke\nYou can fight in war")
elif age == 21:
    print("You can drink")
elif age == 25 and gender == "female":
    print("You can have a child")
elif age == 29 and gender == "male":
    print("You can marry")
elif age == 35:
    print("You can resign")
else:
    print("Loading")
