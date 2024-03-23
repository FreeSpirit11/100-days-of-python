import turtle
import pandas
screen=turtle.Screen()
image="blank_states_img.gif"
screen.bgpic(image)
count=0
screen.title(" U.S. Sates Game ")
data=pandas.read_csv("50_states.csv")
tim=turtle.Turtle()
tim.hideturtle()
tim.penup()
game_is_on=True
answer_states=[]
while game_is_on:

    answer_state = screen.textinput(title=f"{count}/50 States Correct", prompt="what's the state?").title()
    if (data.state==answer_state).any():
        #without .any(), the condition will return a Series of boolean values rather than a single boolean value. In a boolean context (like an if statement), this Series would be treated as ambiguous, and it may raise a ValueError.
        answer_states.append(answer_state)
        state_data=data[data.state==answer_state]
        x=int(state_data.x)
        y=int(state_data.y)
        tim.goto(x,y)
        tim.write(answer_state)
        count+=1
    if count==50 or answer_state=="No":
        game_is_on=False


ddf=data[~data.state.isin(answer_states)]
df=ddf.state

df.to_csv("states_to_name.csv",index=False)
screen.exitonclick()


