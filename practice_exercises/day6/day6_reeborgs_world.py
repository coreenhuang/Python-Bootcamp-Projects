# Move in a square-----------

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    

# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_right()
# move()

# Move over hurdles using a for loop -----------

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def move_over_hurdle():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# for one_move in range(6):
#     move_over_hurdle()

# Move over hurdles using a while loop -----------

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def move_over_hurdle():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# number_of_hurdles = 6

# while number_of_hurdles > 0:
#     move_over_hurdle()
#     number_of_hurdles -= 1
#     print(number_of_hurdles)

# Move over hurdles using a while loop but goal is random-----------

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def move_over_hurdle():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# while at_goal() == False:
#     move_over_hurdle()

# OR

# while not at_goal():
#     move_over_hurdle()

# Hurdle 3 - Random goal and different obstacles

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
        
# def jump_only():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# while at_goal() == False:
#     if front_is_clear():
#         move()
#     elif wall_in_front():
#         jump_only()

# Hurdle 4 - Different obstacles with varying heights---------------------------

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
        
# def jump_only():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
    
# while at_goal() == False:
#     if front_is_clear():
#         move()
#     elif wall_in_front():
#         jump_only()

# Maze Challenge -----------------------------

def turn_right():
    turn_left()
    turn_left()
    turn_left()
        
while not at_goal():
    if front_is_clear() and wall_on_right():
        move()