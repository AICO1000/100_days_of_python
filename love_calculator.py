print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is there name?\n")
lower_name1 = name1.lower()
lower_name2 = name2.lower()
count_t = lower_name1.count("t") + lower_name2.count("t")

count_r = lower_name1.count("r") + lower_name2.count("r")

count_u = lower_name1.count("u") + lower_name2.count("u")

count_e = lower_name1.count("e") + lower_name2.count("e")

final_count = (count_t + count_r + count_u + count_e)

count_l = lower_name1.count("l") + lower_name2.count("l")

count_o = lower_name1.count("o") + lower_name2.count("o")

count_v = lower_name1.count("v") + lower_name2.count("v")

count_e = lower_name1.count("e") + lower_name2.count("e")

final_count2 = (count_l + count_o + count_v + count_e)

Love_Scores = int(f"{final_count}{final_count2}")

if Love_Scores < 10 or Love_Scores > 90:
    print(
        f"Your score is {Love_Scores}, you go together like coke and mentos.")
elif Love_Scores >= 40 and Love_Scores <= 50:
    print(f"Your score is {Love_Scores}, you are alright together.")
else:
    print(f"Your score is {Love_Scores}.")
