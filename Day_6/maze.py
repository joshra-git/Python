def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    while front_is_clear():
        move()
    while not front_is_clear() and right_is_clear():
        turn_right()
    while not front_is_clear() and not right_is_clear():
        turn_left()
        
        
        
# Either the test front_is_clear() 
#or wall_in_front(), 
#right_is_clear() or 
#wall_on_right(), and 
#at_goal().