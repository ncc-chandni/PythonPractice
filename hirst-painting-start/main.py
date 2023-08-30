# import colorgram

# rgb_colors = []
# colors = colorgram.extract('/Users/umakantmanore/Desktop/amu/practice/hirst-painting-start/image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,b,g)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)

tim = turtle_module.Turtle()
tim.speed("fastest")
tim.hideturtle()

color_list = [(245, 238, 243), (246, 244, 242), (202, 110, 164), (240, 241, 245), (236, 243, 239), (149, 50, 75), (222, 136, 201), (53, 123, 93), (170, 41, 154), (138, 20, 31), (134, 184, 163), (197, 73, 92), (47, 86, 121), (73, 35, 43), (145, 149, 178), (14, 70, 98), (232, 165, 176), (160, 158, 142), (54, 50, 45), (101, 77, 75), (183, 171, 205), (36, 74, 60), (19, 89, 86), (82, 129, 148), (147, 19, 17), (27, 102, 68), (12, 64, 70), (107, 153, 127), (176, 208, 192), (168, 102, 99)]

tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots  = 100

for dot_count in range(1, num_of_dots + 1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()