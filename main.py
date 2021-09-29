# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_name = name1 + name2
combined_name_in_lower_case = combined_name.lower()

t = combined_name_in_lower_case.count("t")
r = combined_name_in_lower_case.count("r")
u = combined_name_in_lower_case.count("u")
e = combined_name_in_lower_case.count("e")

count_true = t + r + u + e 

l = combined_name_in_lower_case.count("l")
o = combined_name_in_lower_case.count("o")
v = combined_name_in_lower_case.count("v")
e = combined_name_in_lower_case.count("e")

count_love = l + o + v + e

love_score = int(str(count_true) + str(count_love))

if love_score < 10 or love_score > 90:
  print(f"Your love score is {love_score}, you go together like coke and mentos.")

elif love_score > 40 and love_score < 50:
  print(f"Your love score is {love_score}, you are alright together.")

else:
  print(f"Your love score is {love_score}.")
  



