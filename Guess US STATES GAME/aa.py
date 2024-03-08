import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_map.gif"
screen.addshape(image)
turtle.shape(image)

correct_answers = []

data = pd.read_csv("50_states.csv")


def move_guess(answer):
    new_guess = turtle.Turtle()
    new_guess.hideturtle()
    new_guess.penup()
    guess_data = data[data["state"] == f"{answer_state}"]
    new_guess.goto(int(guess_data.x),int(guess_data.y))
    new_guess.write(f"{answer}",font=("Courier",8,"normal"))


while len(correct_answers) < 50:

    answer_state = screen.textinput(title=f"{len(correct_answers)}/50 Guess Correct",
                                    prompt="Enter the state name: ").title()
    for state in data["state"]:
        if answer_state == state:
            correct_answers.append(answer_state)
            move_guess(answer_state)

    if answer_state=="Exit":
        missing_states = [state for state in data.state if state not in correct_answers]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("States to learn")

turtle.mainloop()
