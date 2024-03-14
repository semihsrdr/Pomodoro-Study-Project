import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK = "✔"
TICKS=""
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps,timer,TICKS
    start_button.config(state="normal")
    reps=0
    window.after_cancel(timer)
    check_marks.config(text="")
    TICKS=""
    canvas.itemconfig(timer_text,text=f"00:00")
    header_label.config(text="Timer",fg=GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    start_button.config(state="disabled")
    global reps,TICKS,TICK

    work_sec=WORK_MIN * 60
    short_break_sec=SHORT_BREAK_MIN * 60
    long_break_sec=LONG_BREAK_MIN * 60

    if reps==0 or reps==2 or reps==4 or reps==6:
        countdown(work_sec)
        header_label.config(text="Work",fg=GREEN)
    elif reps==1 or reps==3 or reps==5:
        header_label.config(text="Break",fg=PINK)
        TICKS+=TICK
        countdown(short_break_sec)
    elif reps ==7:
        header_label.config(text="Break",fg=RED)
        TICKS += TICK
        countdown(long_break_sec)
    else:
        header_label.config(text="Finished",fg=GREEN)
    reps+=1
    check_marks.config(text=TICKS)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    sec = count % 60
    min = math.floor(count / 60)


    canvas.itemconfig(timer_text, text=f"{min:02}:{sec:02}")
    if count > 0:
        timer=window.after(1000, countdown, count - 1)
    else:
        canvas.itemconfig(timer_text,text=f"00:00")
        return start_timer()



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.minsize(500,450)
window.maxsize(500,450)
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

header_label = Label(text="TIMER", font=(FONT_NAME, 50, "normal"), bg=YELLOW, fg=GREEN)
header_label.config(highlightcolor=GREEN)
header_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
my_photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=my_photo)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", height=1, width=5, bg="white", font=(FONT_NAME, 10, "bold"), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", height=1, width=5, bg="white", font=(FONT_NAME, 10, "bold"),command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(text=TICKS, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 16, "bold"))
check_marks.grid(row=3, column=1)

canvas.mainloop()
window.mainloop()
