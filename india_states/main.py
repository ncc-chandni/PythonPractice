import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("India States Map")
image = "/Users/umakantmanore/Desktop/amu/practice/india_states/India-state.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

india_states = pd.read_csv("/Users/umakantmanore/Desktop/amu/practice/india_states/states_data.csv")
all_states = india_states.state.to_list()
guessed_states = []

while len(guessed_states) < 29:
    states = screen.textinput(title=f"{len(guessed_states)}/28! Guess the state", prompt="What is another state name?").title()
    if states == "Exit": 
        missing_states = [state for state in all_states if state not in guessed_states]
        states_to_learn = pd.DataFrame(missing_states)
        states_to_learn.to_csv("/Users/umakantmanore/Desktop/amu/practice/india_states/states_to_learn.csv")
        break
    if states in all_states:
        guessed_states.append(states)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = india_states[india_states.state == states]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(states )


turtle.mainloop()