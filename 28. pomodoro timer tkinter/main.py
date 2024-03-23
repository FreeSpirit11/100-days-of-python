from tkinter import *
from tkinter import messagebox
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None


def on_break():
    messagebox.showinfo(title="Break Time!", message="It's time for a break!")
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    # This line declares that the variable reps is a global variable. This means that if the variable reps is modified within this function, the change will affect the global variable outside the function.
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text=f"00:00" )
    title_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    reps=0
    print(type(timer_text))
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    reps += 1
    if reps%2!=0:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

    elif reps%8==0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)

    elif reps%2==0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min=count//60
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        timer=window.after(1000,count_down, count-1)
    else:



        start_timer()
        if reps%2==0:
            work_session=reps//2
            check_mark.config(text=work_session*"✔")
            on_break()
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas=Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text=canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(row=1, column=1)

title_label=Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title_label.grid(row=0,column=1)

start_buttton=Button(text="Start",highlightthickness=0, command=start_timer)
start_buttton.grid(row=2, column=0)

reset_buttton=Button(text="Reset", highlightthickness=0, command=reset_timer )
reset_buttton.grid(row=2, column=2)

check_mark=Label( fg=GREEN, font=(FONT_NAME,18), bg=YELLOW)
check_mark.grid(row=3,column=1)

window.mainloop()