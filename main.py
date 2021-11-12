import turtle as trtl


def main():
    # create the turtle
    gary = trtl.Turtle()
    # set up the box
    box(gary)
    # Drawing the lines
    lines(gary)
    # Keep Screen Active
    wn = trtl.Screen()
    wn.mainloop()


def lines(gary):
    xPos = -500
    yPos = -300
    xCord = 480
    yCord = -290
    n = 0
    while n <= 60:
        gary.speed(0)
        gary.penup()
        gary.goto(xPos, yPos)
        gary.pendown()
        gary.goto(xCord, yCord)
        xPos += 16
        yCord += 10
        n += 1
    z = 0
    X2Pos = 480
    Y2Pos = -300
    X2Cord = -500
    Y2Cord = -290
    while z <= 60:
        gary.speed(0)
        gary.penup()
        gary.goto(X2Pos, Y2Pos)
        gary.pendown()
        gary.goto(X2Cord, Y2Cord)
        X2Pos -= 16
        Y2Cord += 10
        z += 1
    y = 0
    X3Pos = -500
    Y3Pos = 330
    X3Cord = 480
    Y3Cord = 320
    while y <= 60:
        gary.speed(0)
        gary.penup()
        gary.goto(X3Pos, Y3Pos)
        gary.pendown()
        gary.goto(X3Cord, Y3Cord)
        X3Pos += 16
        Y3Cord -= 10
        y += 1
    v = 0
    X4Pos = 480
    Y4Pos = 330
    X4Cord = -500
    Y4Cord = 320
    while v <= 60:
        gary.speed(0)
        gary.penup()
        gary.goto(X4Pos, Y4Pos)
        gary.pendown()
        gary.goto(X4Cord, Y4Cord)
        X4Pos -= 16
        Y4Cord -= 10
        v += 1


def box(gary):
    xPos = -500
    yPos = -300
    gary.speed(0)
    gary.penup()
    gary.goto(xPos, yPos)
    gary.pendown()
    gary.goto(xPos + 980, yPos)
    gary.goto(xPos + 980, yPos + 630)
    gary.goto(xPos, yPos + 630)
    gary.goto(xPos, yPos)


if __name__ == "__main__":
    main()