import turtle
import pandas as pd


def main():
    screen = turtle.Screen()
    screen.title("US States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    data = pd.read_csv("50_states.csv")
    all_states = data.state.to_list()
    guessed_states = []

    while len(guessed_states) < 50:
        answer_state = screen.textinput(title="Guess the state", prompt="What's the name of another state?").title()

        if answer_state == "Exit":
            missing_states = []
            for state in all_states:
                missing_states.append(state)
            new_data = pd.DataFrame(missing_states)
            new_data.to_csv("States_to_learn.csv")
            break
        if answer_state in all_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(state_data.x.item(), state_data.y.item())
            t.write(answer_state)


if __name__ == "__main__":
    main()
