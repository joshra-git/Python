### Global Variables

test = ""

def testing(item, items):
    global test
    print (item)
    print (items)
    test = "lol"
    return test

noah = "awake"

testing(noah,2)

This takes a blank variable called "test". It will then use that global variable within the function. modify it and return the new variable so it can be used outside of the function

### Functions

When you write a function, you can pass in however many variables within the function itself. When you call the function, you need to pass in the same amount. 

In the example, I've passed in 5 and 2, which are position 0 and 1. It will then use these and print them based on the input

### Lists

