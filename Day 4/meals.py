# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
howmany = len(names)
howmany -= 1
person = random.randint(0,howmany - 1)
unlucky = names[person]
print(f"{unlucky} is going to buy the meal today!")