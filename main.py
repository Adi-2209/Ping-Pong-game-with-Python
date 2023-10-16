


#NAME:ADITI GHOSH

#DATE:2ND DECEMBER,2022

#PROJECT - PING PONG BALL GAME WITH PYTHON AND TURTLE GRAPHICS


import turtle
import random

global character


s=turtle.Screen()
s.title("Ping Pong Game with Python")
s.setup(width=1000,height=600)
s.bgcolor("black")
text=turtle.Turtle()
text.penup()
text.hideturtle()
text.goto(0,100)
text.color("white")
text.write("Ping Pong Game with Python!", False, align='center', font=('Arial', 30, 'bold'))
text.penup()
text.hideturtle()
text.goto(0,20)
text.color("purple")
text.write("Pick a character:", False, align='center', font=('Arial', 30, 'bold'))
characters = ["character_1.gif", "character_2.gif","character_3.gif","character_4.gif"]
turtles=[]

def start(x, y):
  global notStarted
  notStarted = False

def choose_character(x, y):
  global isNotSelected
  global char

  if x < -400:
    char= " character_1.gif"
    
  elif x >= -300 and x<=50:
    char = "character_2.gif"
    
  elif x>50 and x<=200:
    char = "character_3.gif"

  else:
    char = "character_4.gif"
    
  isNotSelected = False
x = -500
for i in range(0, len(characters)):
  turtle.addshape(characters[i])
  ch = turtle.Turtle()
  turtles.append(ch)
  ch.shape(characters[i])
  ch.penup()
  ch.goto(x, -200)
  x = x + 300

s.listen()


isNotSelected = True

while isNotSelected:
  turtles[0].onclick(choose_character)
  turtles[1].onclick(choose_character)
  turtles[2].onclick(choose_character)
  turtles[3].onclick(choose_character)
 
s.clearscreen()
s.bgcolor("purple")
filename=open("rules.txt")
file_list=filename.readlines()
text=turtle.Turtle()

x=-100
y=100

for line in file_list:
  text.color("black")
  text.penup()
  text.goto(x,y)
  text.write(line,False,align="Center",font=("Arial",16,"bold"))
  y=y-50

button = turtle.Turtle()
turtle.addshape("start.gif")
button.shape("start.gif")
button.penup()
button.goto(-100, -300)

notStarted = True
while notStarted:
  button.onclick(start)


s.clearscreen()
s.bgcolor("pink")
  
left_character = turtle.Turtle()
left_character.shape(char)
left_character.penup()
left_character.goto(-400, 0)


right_character=turtle.Turtle()  
right_character.shape("square")  
right_character.color("Blue")  
right_character.shapesize(stretch_wid = 2, stretch_len = 6)  
right_character.penup()  
right_character.goto(400, 0)  

 

hit_ball = turtle.Turtle()  
hit_ball.speed(45)  
hit_ball.shape("circle")  
hit_ball.color("Black")  
hit_ball.penup()  
hit_ball.goto(0, 0)  
hit_ball.dx = 5  
hit_ball.dy = -5 

left_player=0
right_player=0

score = turtle.Turtle()  
score.speed(0)  
score.color("blue")  
score.penup()  
score.hideturtle()  
score.goto(-30, 260)  
score.write("You : 0    Computer: 0",align = "center", font = ("Courier", 24, "normal"))  
      


def left_up():
  left_character.setheading(90)
  left_character.forward(10)
  



def left_down():
  left_character.setheading(270)
  left_character.forward(10)
  


def right_up():
  right_character.setheading(90)
  right_character.forward(10)

  


def right_down():
  right_character.setheading(270)
  right_character.forward(10)



s.listen()  
s.onkeypress(left_up, "Up")  
s.onkeypress(left_down, "Down")  
s.onkeypress(right_up, "w")  
s.onkeypress(right_down, "e") 


while (left_player<11) and (right_player<11):

  s.update()

  hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
  hit_ball.sety(hit_ball.ycor()+hit_ball.dy)

  if hit_ball.ycor() > 280:
   hit_ball.sety(280)
   hit_ball.dy*=-1 
   
  
  if hit_ball.ycor() < -280:
   hit_ball.sety(-280)
   hit_ball.dy*=-1
    
  if hit_ball.xcor() > 500:  
        hit_ball.goto(0, 0)  
        hit_ball.dy *= -1  
        left_player += 1  
        score.clear()  
        score.write("You : {}    Computer: {}".format(  
                      left_player, right_player), align = "center",  
                      font = ("Courier", 24, "normal"))  
   
  if hit_ball.xcor() < -500:  
        hit_ball.goto(0, 0)  
        hit_ball.dy *= -1  
        right_player += 1  
        score.clear()  
        score.write("You : {}    Computer: {}".format(  
                                 left_player, right_player), align = "center",  
                                 font = ("Courier", 24, "normal"))  

  if (hit_ball.xcor() > 360 and  
                        hit_ball.xcor() < 370) and (hit_ball.ycor() < right_character.ycor() + 40 and  
                        hit_ball.ycor() > right_character.ycor() - 40):  
                        hit_ball.setx(360)  
                        hit_ball.dx *= -1  
          
  if (hit_ball.xcor() < -360 and  
                       hit_ball.xcor() > -370) and (hit_ball.ycor() < left_character.ycor() + 40 and  
                       hit_ball.ycor() > left_character.ycor() - 40):  
                       hit_ball.setx(-360)  
                       hit_ball.dx *= -1  


if left_player>=11:
  s.clearscreen()
  s.bgcolor("blue")
  text.goto(0,0)
  text.color("yellow")
  text.write("Congratualtions!!You won!!",align="center",font=("Arial",35,"normal"))
else:
  s.clearscreen()
  s.bgcolor("blue")
  text.goto(0,0)
  text.color("red")
  text.write("Computer won!!Better Luck next time",align="center",font=("Arial",30,"normal"))






turtle.mainloop()
   
   
