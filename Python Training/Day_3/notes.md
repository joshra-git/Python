# Day 3

## Control flow with if / else and conditional operators

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120: 
  print("You can ride the rollercoaster!")
else:
  print("Sorry, you have to grow taller before you can ride.")



### Comparison operators

**Conditions**
> -- greater
< -- less than
>= -- greater than or equal to
<= -- equal or less than
== -- equal to
!= -- not equal to
+= -- this is the same as having bill = bill + 3 (bill += 3)


% = modulo operation

7 % 2

This will give us the remainder. this should give us a 1. Odd numbers will always give 1 even will give 0

# Don't change the code below
number = int(input("Which number do you want to check? "))
# Don't change the code above

#Write your code below this line


odd_even = number % 2

if odd_even == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


### Nested if statements and elif statements

**if else statements**

if condition:
    if another condition:
        do this:
    else: do that
else:
    do this

**if / elif / else**

if condition1:
    do A
elif condition2:
    do B
else: do this

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120: 
  print("You can ride the rollercoaster!")
  age = int(input("What is your age?"))
  if age <= 12:
    print("You can pay $5")
  elif age <= 18:
    print("You can pay $7")
  else:
    print("You need to pay $12")
else:
  print("Sorry, you have to grow taller before you can ride.")


### BMI and conditions

# Don't change the code below
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# Don't change the code above

#Write your code below this line

bmi = round(int(weight) / (height * height))



if bmi > 18.5:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi > 25:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi > 30:
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi > 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are under weight")


Dealing with " and '
in a situation when you're doing this "Hello, you're 'amazing'" we can add a \ to you\'re and it'll see it as a string rather than multiple strings

When you're writing an input you can add the .lower() to the end to convert it to all lower case

input = ("YoUr CoOl").lower()