import turtle as trtl

def main():
    # Create the Turtle
    gary = trtl.Turtle()

    # Setup the Box
    box(gary)

    #Drawing the Lines
    #Making a change on repl.it

    # Keep Screen Active
    wn = trtl.Screen()
    wn.mainloop()

def box(gary):
    xPos = -500
    yPos = -300
    gary.speed(0)
    gary.penup()
    gary.goto(xPos, yPos)
    gary.pendown()
    gary.goto(xPos+980, yPos)
    gary.goto(xPos+980, yPos+630)
    gary.goto(xPos, yPos+630)
    gary.goto(xPos, yPos)

if __name__ == "__main__":
    main()