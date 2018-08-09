# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:58:42 2018

Snake Mini project Starter Code
Name: Yali Miller 
Date: 8/7/18
"""
c = input("Choose a snake color! ")
b = input("Choose a background color! ")
import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

scorev = 0


def score():
    turtle.undo()
    global scorev
    turtle.goto(-75,-400)
    scorev += 1
    turtle.hideturtle()
    turtle.pensize(20)
    turtle.write("Your score is " + str(scorev), font=("Arial", 16, "normal"))
    

border = turtle.clone()
border.showturtle()
border.shape("turtle")
border.penup()
border.goto(-300,300)
border.pendown()
border.goto(300,300)
border.goto(300,-300)
border.goto(-300,-300)
border.goto(-300,300)
if b == "black":
    border.color("white")
else:
    border.color("black")
border.hideturtle()



SIZE_X=1000
SIZE_Y=1000
turtle.setup(SIZE_X, SIZE_Y)#Curious? It's the turtle window  
turtle.bgcolor(b)                             #size. 

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 2

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

snake.color(c)

turtle.register_shape("trash.gif") #Add trash picture
                      # Make sure you have downloaded this shape 
                      # from the Google Drive folder and saved it
                      # in the same folder as this Python script

food = turtle.clone()
food.shape("trash.gif")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for i in range(START_LENGTH) :
    x_pos=snake.xcor() #Get x-position with snake.pos()[0]
    y_pos=snake.ycor()

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos += SQUARE_SIZE

    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    stampID = snake.stamp()
    stamp_list.append(stampID)


###############################################################
#                    PART 2 -- READ INSTRUCTIONS!!
###############################################################
UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 0
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!
DOWN = 1
LEFT = 2
RIGHT = 3

direction = UP
UP_EDGE = 300
DOWN_EDGE = -300
RIGHT_EDGE = 300
LEFT_EDGE = -300

title = turtle.clone()
title.goto(0,400)
title.write("SNAKE GAME!", move=False, align="center", font=("Arial", 20, "normal"))


def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up
    print("You pressed the up key!")

#2. Make functions down(), left(), and right() that change direction
####WRITE YOUR CODE HERE!!

def down():
    global direction
    direction = DOWN
    print("you pressed the down key!")
def left():
    global direction
    direction = LEFT
    print("you pressed the left key!")
def right():
    global direction
    direction = RIGHT
    print("you pressed the right key!")

turtle.onkeypress(up, UP_ARROW) # Create listener for up key

#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()

def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(300/2/SQUARE_SIZE)+1
    max_x=int(300/2/SQUARE_SIZE)-1
    min_y=-int(300/2/SQUARE_SIZE)-1
    max_y=int(300/2/SQUARE_SIZE)+1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
        ##                        position
    food.goto(food_x, food_y)
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
    food_pos.append((food_x,food_y))
        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list
    stampID = food.stamp() 
    food_stamps.append(stampID)

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if my_pos in pos_list[:-1]:
        print("you ate youself BRUH")
        quit()
    
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction == UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("you moved up!")
    elif direction == DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
    #Add new lines to the end of the function
    #Grab position of snake
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    # The next three lines check if the snake is hitting the 
    # right edge.
    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        quit()

     # You should write code to check for the left, top, and bottom edges.
    #####WRITE YOUR CODE HERE
    if new_x_pos <= LEFT_EDGE:
        print("you hit the left edge! game over!")
        quit()
    if new_y_pos >= UP_EDGE:
        print("you hit the upper edge! game over!")
        quit()
        
    if new_y_pos <= DOWN_EDGE:
        print("you hit the lower edge! game over!")
        quit()

    if len(food_stamps) <= 6:
    	make_food()   
        
    


    #4. Write the conditions for UP and DOWN on your own
    ##### YOUR CODE HERE


    #Stamp new element and append new stamp in list
    #Remember: The snake position changed - update my_pos()

    my_pos=snake.pos() 
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ######## SPECIAL PLACE - Remember it for Part 5
    #pop zeroth element in pos_list to get rid of last the last 
    #piece of the tail
    #global food_stamps, food_pos
    #If snake is on top of food item
    #print("food pos",food_pos)
    #print("stamps",food_stamps)
    
    if snake.pos() in food_pos:
        food_ind = food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food                 
                                               #stamp
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove eaten food stamp
        print("You have eaten the food!")
        score()
    
    #HINT: This if statement may be useful for Part 8
    else:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
        #score()

    turtle.ontimer(move_snake,TIME_STEP)
    
move_snake()

 
'''
#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don’t forget to hide the food turtle!
for this_food_pos in food_pos:
    ####WRITE YOUR CODE HERE!!
    food.goto(this.food_pos)
    food_stamps.append(food.stamp())
'''
