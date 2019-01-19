import turtle
import time
import random

delayeachtime = 0.12

#score
score = 0
high_score = 0

# Set up the Screen
wn = turtle. Screen()
wn.title("Happy Snake by @Ariel")
wn.bgcolor("brown")
wn.setup(width=600, height=600)
wn.tracer(0)


# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake Snacks
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("black")
food.penup()
food.goto(0,120)

# make the snake longer when eating snacks
segments = []

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center",\
          font=("Courier", 24, "normal"))


# directions
def go_up():
    if head.direction != "down": #prevent the snake from inversing direction
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"
      
def go_left():
    if head.direction != "right":
        head.direction = "left"
    
def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20) 
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)  
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)  

#Keyboard Bind
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


# Main loop
while True:
    wn.update()
    
    # if the snake touched the border, it will die
    # check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 \
       or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        # hide the segments
        # give the segments an coordinate outside the screan
        for segment in segments:
            segment.goto(1000, 1000)
            
        # clear the segments list
        segments.clear()
        
        # reset the score
        # the score should turn into zero when the snake dies
        score = 0
        
        # reset the delay
        # to make it as slow as the original one when snake dies
        delayeachtime = 0.12        
        
        # clear the score when it gets a new score
        pen.clear()
        
        pen.write("Score: {} High score: {}".\
                  format(score, high_score), align="center",\
                  font=("Courier", 24, "normal"))         
    
    # check for a collision with the food
    # using distance
    if head.distance(food) < 15:
        # Move the food to somewhere random
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)
        
        # add a segment when eating the snack
        new_segment = turtle.Turtle()
        new_segment.speed (0)
        new_segment.shape("square")
        new_segment.color("lightblue")
        new_segment.penup()
        # segments is a list of segments and each turtle is a segment
        segments.append(new_segment)
        
        # shorten the delay
        # to make the game more challenging 
        delayeachtime -= 0.001
        
        #increase the score
        score += 10
        
        if score > high_score:
            high_score = score
        
        # clear the score when it gets a new score
        pen.clear()
        
        pen.write("Score: {} High score: {}".\
                  format(score, high_score), align="center",\
                  font=("Courier", 24, "normal"))
            
        
        
    # move the end segments first in reverse order
    # this will only do something if there are more than one segment
    for index in range(len(segments) -1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    
    # move segment 0 to where the head is
    # is there the length over zero?
    # if it is, we want the first segment to move to the head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    
    move()
    
   # check for head collision with the body segments
   # using distance as well
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            # hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
                
            # clear the segments list
            segments.clear()
            
            # reset the score
            # the score should turn into zero when the snake dies
            score = 0
            
            # reset the delay
            # to make it as slow as the original one when snake dies
            delayeachtime = 0.12
            
            # clear the score when it gets a new score
            pen.clear()
            
            pen.write("Score: {} High score: {}".\
                      format(score, high_score), align="center",\
                      font=("Courier", 24, "normal"))            
    
    
    time.sleep(delayeachtime)


wn.mainloop()    