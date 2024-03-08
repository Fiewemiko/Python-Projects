from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_laber.config(text="Timer", fg=GREEN)
    reps = 0
    checkmark.config(text='✔'* reps)

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    if reps % 2 == 1:
        countdown(WORK_MIN*60)
        timer_laber.config(text="WORK",fg=RED)
    elif reps % 8 == 0:
        countdown(LONG_BREAK_MIN*60)
        timer_laber.config(text="Break", fg=GREEN)
    else:
        countdown(SHORT_BREAK_MIN*60)
        timer_laber.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import math
def countdown(count):

    minutes = math.floor(count/60)
    seconds = count % 60

    canvas.itemconfig(timer_text,text = f"{minutes:02}:{seconds:02}")
    if count >0:
        global timer
        timer = window.after(1000,countdown,count-1)
    else:
        start_timer()
        checkmark.config(text='✔'* (reps//2))
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100,pady=50, bg=YELLOW)

canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
bg_image = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image = bg_image )
timer_text = canvas.create_text(100,130,text ="00:00",fill="white",font=(FONT_NAME,35,'bold'))


timer_laber = Label(text='Timer',fg=GREEN,bg=YELLOW,font=(FONT_NAME,30,'bold'))
start_button = Button(text='Start',command=start_timer)
reset_button = Button(text='Reset',command=reset_timer)

checkmark =Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,24,'normal'))

canvas.grid(row=2,column=2)
timer_laber.grid(row=1,column=2)
start_button.grid(row=3,column=1)
reset_button.grid(row=3,column=3)
checkmark.grid(row=4,column=2)


window.mainloop()