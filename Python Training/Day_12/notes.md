in order to tap into a global variable from within a function you need to use this:


enemies = 1
def increase_enemies():
    global enemies

Global Constant

UPPER_CASE = whatever

Try to use functions where ever possible especially if I'm needing to repeat or call on something multiple times.