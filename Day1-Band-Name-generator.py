print("Welcome, create your band name!!!")
city = input("What is name of the city you grew up in?\n")
pet = input("What is the name your favorite pet?\n")
band_name = "Your band name is:"+ city + ' ' + pet
print(band_name)
suggest = input("Do you want to create another band name [Y/n]?").lower
if suggest == "Y":
    print("Welcome, create your band name!!!")
    city = input("What is name of the city you grew up in?\n")
    pet = input("What is the name your favorite pet?\n")
    band_name = "Your band name is:"+ city + ' ' + pet
    print(band_name)
else:
    print("Have a good day!")