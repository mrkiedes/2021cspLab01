import turtle as trtl

def main():
    # Create the Turtle
    sam = trtl.Turtle()

    # Setup the Box
    box(sam)

    #Drawing the Lines


    # Keep Screen Active
    wn = trtl.Screen()
    wn.mainloop()

def box(sam):
    xPos = -500
    yPos = -300
    sam.speed(0)
    sam.penup()
    sam.goto(xPos, yPos)
    sam.pendown()
    sam.goto(xPos + 980, yPos)
    sam.goto(xPos + 980, yPos + 630)
    sam.goto(xPos, yPos + 630)
    gary.goto(xPos, yPos)

if __name__ == "__main__":
    main()