# Space Invaders - Part 1
# Set up the screen
# Python 2.7
import turtle
import os
import math
import random
import move
import chars
import bullet

# set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)  # 0 is the fastest
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#set the score
score = 0

#draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()



enemyspeed = 2

# Choose a number of enemies
number_of_enemies = 5
# create an empty list of enemies
enemies = []

# add enemies to the list
for i in range(number_of_enemies):
    # create the enemies
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)


# # create the player's bullet
# bullet = turtle.Turtle()
# bullet.color("yellow")
# bullet.shape("triangle")
# bullet.penup()
# bullet.speed(0)
# bullet.setheading(90)
# bullet.shapesize(0.5, 0.5)
# bullet.hideturtle()

# bulletspeed = 20

# # define bullet state
# # ready - ready to fire
# # fire - bullet is firing
# bulletstate = "ready"


# move the player left and right

# horizontal movement


# def move_left():
#     x = player.xcor()
#     x -= playerspeed
#     if x < -280:
#         x = - 280
#     player.setx(x)


# def move_right():
#     x = player.xcor()
#     x += playerspeed
#     if x > 280:
#         x = 280
#     player.setx(x)

# vertical movement
# def move_down():
#   y = player.ycor()
#   y -= playerspeed
    # if y < -280:
    #   y = - 280
#   player.sety(y)


# def move_up():
#   y = player.ycor()
#   y += playerspeed
    # if y > 280:
    #   y = 280
#   player.sety(y)

# def fire_bullet():
#         # declare bulletstate as a global if it needs to be changed
#     global bulletstate
#     if bulletstate == "ready":
#         bulletstate = "fire"
#         # move the bullet to just above the player
#         x = chars.player.xcor()
#         y = chars.player.ycor()
#         bullet.setposition(x, y + 10)
#         bullet.showturtle()


def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) +
                         math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


# Create keyboard bindings
turtle.listen()
turtle.onkey(move.move_left, "Left")
turtle.onkey(move.move_right, "Right")
# turtle.onkey(move_down, "Down")
# turtle.onkey(move_up, "Up")
turtle.onkey(bullet.fire_bullet, "space")


# Main game loop
while True:

    for enemy in enemies:
        # move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # move the enemy back and forth. set up so that it activates if it hits either border
        if enemy.xcor() > 280:
            #move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #change direction
            enemyspeed *= -1

        if enemy.xcor() < -280:
            #move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #change direction
            enemyspeed *= -1


        # check for collision between bullet and enemy
        if isCollision(bullet.bullet, enemy):
            # reset the bullet
            bullet.bullet.hideturtle()
            bullet.bulletstate = "ready"
            bullet.bullet.setposition(0, -400)
            # reset the enemy
            enemy.setposition(-200, 250)
            #update score
            score +=10
            score_pen.clear()
            scorestring = "Score: %s" %score
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
            score_pen.hideturtle()

        if isCollision(chars.player, enemy):
            player.hideturtle()
            print("Game Over")
            break

    # move bullet
    if bullet.bulletstate == "fire":
        y = bullet.bullet.ycor()
        y += bullet.bulletspeed
        bullet.bullet.sety(y)

    # check to see if bullet has reached the top
    if bullet.bullet.ycor() > 275:
        bullet.bullet.hideturtle()
        bullet.bulletstate = "ready"

   


delay = raw_input("Press enter to finish.")
