#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total_letters = len(letters)
total_symbols = len(symbols)
total_numbers = len(numbers)

final_password = []

for number in range(nr_numbers):
    num = random.randint(0, (total_numbers - 1))
    numm = numbers[num]
    final_password.append(numm)

for letter in range(nr_letters):
    let = random.randint(0, (total_letters - 1))
    alpha = letters[let]
    final_password.append(alpha)

for symbol in range(nr_symbols):
    sym = random.randint(0, (total_symbols -1))
    point = symbols[sym]
    final_password.append(point)

random.shuffle(final_password)
password = ""
for char in final_password:
    password += char


# https://www.w3schools.com/python/ref_random_shuffle.asp
# random.shuffle(password)

print(f"Your password is: {password}")

