import turtle
import chars

# create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

# define bullet state
# ready - ready to fire
# fire - bullet is firing
bulletstate = "ready"

def fire_bullet():
        # declare bulletstate as a global if it needs to be changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        # move the bullet to just above the player
        x = chars.player.xcor()
        y = chars.player.ycor()
        bullet.setposition(x, y + 10)
        bullet.showturtle()
