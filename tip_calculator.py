age = input("What is your current age?")
olddays = 32873
oldweeks = 4680
oldmonths = 1080
newdays = int(age) * 356
neweday = int(olddays)-int(newdays)
newweeks = int(age) * 52
neweweeks = int(oldweeks)-int(newweeks)
newmonths = int(age) * 12
newemonths = int(oldmonths)-int(newmonths)
print(
    f"You have {neweday} days, {newweeks} weeks, and {newemonths} months left")


# print(f"You have {12410} days, {1768} weeks, and {408} months left")
