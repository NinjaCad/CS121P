import turtle
import random

background_red = 0.25 * random.randrange(0, 2)
background_green = 0.25 * random.randrange(0, 2)
background_blue = 0.25 * random.randrange(0, 2)
print("Random background color is: (", background_red, ",",
      background_green, ",", background_blue, ")")

wn = turtle.Screen()
wn.bgcolor(background_red, background_green, background_blue)

rotational_copies = int(input("Enter rotational copies: "))
sides_per_polygon = int(input("Enter sides_per_polygon per polygon: "))
edge_pixel_length = int(input("Enter edge pixel length: "))

murtle = turtle.Turtle()
murtle.hideturtle()
murtle.speed(0)

murtle.pensize(5)
murtle.color(1,1,1)
for i in range(rotational_copies):
    for j in range(sides_per_polygon):
        murtle.forward(edge_pixel_length)
        murtle.left(360/sides_per_polygon)
    murtle.left(360/rotational_copies)

murtle.pensize(1)
murtle.color(0,0,0)
for i in range(rotational_copies):
    for j in range(sides_per_polygon):
        murtle.forward(edge_pixel_length)
        murtle.left(360/sides_per_polygon)
    murtle.left(360/rotational_copies)

print("Click turtle screen to exit...")
wn.exitonclick()

