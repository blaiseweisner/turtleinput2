import turtle
import random

screen = turtle.Screen()
turtle.screensize(500, 500)
t = turtle.Turtle()
#menu
t.penup()
t.goto(0,200)
t.pendown()
t.pencolor('blue')
t.write("Background Color",font=("Arial",20,"bold"),align="center")
t.penup()
t.goto(0,100)
t.pendown()
t.pencolor('blue')
t.write("1. Tan",font=("Arial",20,"bold"),align="left")
t.speed(0)
t.penup()
t.goto(0,50)
t.pendown()
t.pencolor('blue')
t.write("2. Azure",font=("Arial",20,"bold"),align="left")
t.penup()
t.goto(0,0)
t.pendown()
t.pencolor('blue')
t.write("3. Cornsilk",font=("Arial",20,"bold"),align="left")
t.penup()
t.goto(0,-50)
t.pendown()
t.pencolor('blue')
t.write("4. Khaki",font=("Arial",20,"bold"),align="left")
screen.bgcolor('tan')

name= input("Enter Your Name: ")
# num1=int(input("Enter a number: "))
# num2=int(input("Enter another number: "))
# sum=int(input(num1 + num2))
num1= random.randint(-100,100)
num2= random.randint(-100,100)
sum=num1+num2

t.penup()
t.goto(0,100)
t.pendown()
t.pencolor('blue')
t.write(name,font=("Arial",30,"bold"),align="center")

t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor('green')
t.write(num1,font=("Arial",30,"bold"),align="center")

t.penup()
t.goto(0,0)
t.pendown()
t.pencolor('pink')
t.write(num2,font=("Arial",30,"bold"),align="center")

t.penup()
t.goto(-100,0)
t.pendown()
t.pencolor('blue')
t.write("+",font=("Arial",30,"bold"),align="center")

t.penup()
t.goto(100,0)
t.pendown()
t.pencolor('red')
t.write("=",font=("Arial",30,"bold"),align="center")

ans=int(input("Please enter your answer: "))


t.penup()
t.goto(200,0)
t.pendown()
t.pencolor('red')
t.write(sum,font=("Arial",30,"bold"),align="center")



t.penup()
t.goto(0,-100)
t.pendown()
t.pencolor('black')
t.write("Your answer is: ",font=("Arial",30,"bold"),align="center")

if ans == sum:
    screen.bgcolor('dodgerblue')
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.pencolor('green')
    t.write("Correct " + str(ans), font=("Arial", 30, "bold"), align="center")

else:
    screen.bgcolor('darkorange')



turtle.done()