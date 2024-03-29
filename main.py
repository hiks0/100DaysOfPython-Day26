import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
state_list = data.state.to_list()
tim = turtle.Turtle()
tim.penup()
tim.hideturtle()
guessed_states = []

count = 0
game_on = True
while game_on:
    answer_state = screen.textinput(title=f"{count}/50 States Correct",
                                    prompt="enter guess: ").title()
    if answer_state in state_list:
        count += 1
        guessed_states.append(answer_state)
        xco = int(data[data["state"] == answer_state].x)
        yco = int(data[data["state"] == answer_state].y)
        tim.goto(xco, yco)
        tim.write(answer_state, align="center", font=("Ariel", 13, "normal"))
    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in guessed_states]
        # for state in state_list:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        break

    if count == len(state_list):
        tim.goto(0, 0)
        tim.write("GAME OVER", align="center", font=("Courier", 13, "normal"))
        game_on = False

dict = {
    "States To Learn": missing_states
}
df = pd.DataFrame(dict)
df.to_csv("StatesToLearn.csv")

