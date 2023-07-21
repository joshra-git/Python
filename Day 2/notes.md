# Notes

### Types of data sets in Python

**Float** = Floating Point Number

3.14159 = float

**Boolean** = True / False

They always have a capital otherwise it might be a string

**Integers** are just numbers and can be separated by underscores instead of commas

**String** is a word and only a word. "Josh" is a string. 


print("Hello"[0]) will output the first (zero being the first) character in this string

print("123" + "345") will concatenate them together as we're declaring them as strings

print(123 + 456) - will add the numbers up as they're Integers

print(123_234_456 + 1) will do 123234345 and the _ will be removed


### Type Function

num_char = len(input("What is your name?\n"))

print(type(num_char))

**Convervion** 

num_char = len(input("What is your name?\n"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters")

This will convert it from an int to a str

### Different math stuff

\+ - \* = they do pretty much what you would expect

** will do "to the power of"

### PEMDAS - parentheses, exponents, multiplication, division, addition, and subtraction

- \()
- \** - exponents 
- \* /
- \+ -

print(3 * 3 + / 3 - 3)

### Rounding

print(round(52 / 6, 2)) = 8.67

## Floor Division 

Will use an integer and round to the main number

print(round(52 // 6)) = 8

---

putting the "math" symbol before the = in a variable will do whatever I want to that variable

variable plus=1

score = 0

score += 1

print(score)

### F Strings

In front of a string, we can type the character F 

f"your score is {score}"

score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, and you are winning is {isWinning})