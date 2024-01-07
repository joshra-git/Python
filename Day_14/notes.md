# Notes

### Reutrning within a funciton

if I want to create a function that can return something I can do this

def whatever():
    numbr = random.randint(0,19)
    return numbr

This way I can use more functions and possibly less code..

### Lower case for input

.lower() will make the input lowercase

### Return true 

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

What this does is looks at the two inputs and compared them. If Guess is correct, it'll return True (guess == "A"). But if guess was A and it returns B, it would be false.