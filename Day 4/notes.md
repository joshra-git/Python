# Notes

You can import any module and refer to some here - https://www.askpython.com/?s=python+random+module

random.randint(0,1) 

that will give me a random number between 0 and 1

random.random() 

that will give me a random float between 0.000001 and 0.9999999

list ["random1","random2","random3","random4","random5"]

You can change random1 to random 6 by

list[0] = "random6" which will change it within that list after you set it

I can add by going

list.append("random7")

list.exend(["random8", "random9"])

https://docs.python.org/3/tutorial/datastructures.html


### Random

import random

random_integer = random.randint(0.0, 5.0)

random_float = random.random()


print(float(random_integer))


split(",")

### Lists

list = ["Apple", "pear", "grapes"]
list2 = ["Carrot", "potato", "spinach"]

list3 = [list, list2]

print (list3) ==== [["Apple", "pear", "grapes"],["Carrot", "potato", "spinach"]]