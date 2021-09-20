import turtle

def test_drive():
    turtle.forward(100)
    turtle.left(87)
    turtle.setheading(127)
    turtle.up()
    turtle.goto(50,40)
    turtle.down()
    turtle.home()
    turtle.circle(25)

def turtle_state():
    v1=turtle.isdown()
    v2=turtle.heading()
    vx=turtle.xcor()
    vy=turtle.ycor()
    print("is the turtle down? ",v1)
    print("current angle: ",v2)
    print("xcor: ",vx,"ycor: ",vy)

def main():
    turtle_state()
    test_drive()
    turtle_state()
    input("press enter to continue...")

main()