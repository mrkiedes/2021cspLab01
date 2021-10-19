import turtle as trtl

def main():
    # Create the Turtle
    terry = trtl.Turtle()

    # Setup the Box
    box(terry)

    #Drawing the Lines


    # Keep Screen Active
    wn = trtl.Screen()
    wn.mainloop()

def box(terry):
    xPos = -500
    yPos = -300
    terry.speed(0)
    terry.penup()
    terry.goto(xPos, yPos)
    terry.pendown()
    terry.goto(xPos+980, yPos)
    terry.goto(xPos+980, yPos+630)
    terry.goto(xPos, yPos+630)
    gary.goto(xPos, yPos)

if __name__ == "__main__":
    main()