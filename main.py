import turtle, pandas
l = open("States to Learn.csv", "w") # resets the states to learn.csv
l.truncate()
l.close()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x,y):     # To get the x,y coordinates for the map,
#     print(x,y)                        but it's already in the 50_states.csv file.
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

correct_guesses = 0
data = pandas.read_csv("50_states.csv")
answer_state = screen.textinput(title="Guess the State", prompt="Guess a state's name? (Enter exit to quit)").title()

all_states = data.state.to_list()
guessed = []

while len(guessed) < 50:

    if answer_state == "Exit":
        break

    for st in data.state:

        if answer_state == st and st not in guessed:
            x = int(data[data.state == st].x)
            y = int(data[data.state == st].y)
            new_state = turtle.Turtle()
            new_state.hideturtle()
            new_state.penup()
            new_state.goto(x, y)
            new_state.write(f"{answer_state}", True, "center")
            correct_guesses += 1
            guessed.append(st)

    answer_state = screen.textinput(title=f"{correct_guesses}/50 Correct Guesses",
                                    prompt="What's another state's name? (Enter exit to quit)").title()


    for state in guessed:
        if state in all_states:
            i = all_states.index(state)
            del all_states[i]

    learn = pandas.DataFrame(all_states)
    learn.to_csv("States to Learn.csv")