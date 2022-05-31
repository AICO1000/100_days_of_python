print("Life")
print("Know little about you".upper)
Gender = input("What is your gender\n")
age = input("How old are?\n")
days = int(age) * 356
weeks = int(age) * 52
months = int(age) * 12
print(f"You are {days}days, {weeks}weeks, {months}months old")
if int(age) == 15:
    print("You are drive")
if int(age) == 18:
    print("You can vote\nYou can smoke\nYou can fight in war")
if int(age) == 21:
    print("You can drink")
if int(age) == 25 and str(Gender) == "female":
    print("You can have a child")
if int(age) == 29 and str(Gender) == "male":
    print("You can marry")
if age == 35:
    print("You can resign")
else:
    print("Loading")
