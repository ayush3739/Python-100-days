import turtle
import pandas as pd
screen=turtle.Screen()
screen.title("INDIA-State-Game")

image="India-state.gif"
screen.addshape(image)
turtle.shape(image)

data=pd.read_csv("states_data.csv")
state = [s.lower() for s in data.state]

game_is_on=True
guessed_state=[]
while game_is_on:
    i=len(guessed_state)
    answer=screen.textinput(title=f"{i}/30",prompt="what's another state name?").lower()
    if answer=="exit" or i==30:
        break
    if answer in state:
        guessed_state.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        row = data[data.state.str.lower() == answer].iloc[0]
        t.goto(row.x, row.y)
        t.write(row.state)
        i += 1

    else:
        game_is_on=False
    
    


turtle.mainloop()






