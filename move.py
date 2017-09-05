import chars

def move_left():
    x = chars.player.xcor()
    x -= chars.playerspeed
    if x < -280:
        x = - 280
    chars.player.setx(x)


def move_right():
    x = chars.player.xcor()
    x += chars.playerspeed
    if x > 280:
        x = 280
    chars.player.setx(x)

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
