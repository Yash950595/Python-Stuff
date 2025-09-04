from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    windows.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    tick_symbol.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1

    work=WORK_MIN*60
    short_break=SHORT_BREAK_MIN*60
    long_break=LONG_BREAK_MIN*60

    if reps % 8 ==0: #Here the reps go on incrementing and until we reach 8th rep, we take a long break
        count_down(long_break)
        timer_label.config(text="Long Break",fg=GREEN)

    elif reps %2 ==0: #After every work_min there is a gap of 5 mins short break, thus reps %2 == 0
        count_down(short_break)
        timer_label.config(text="Short Break",fg=PINK)
    else:
        count_down(work)
        timer_label.config(text="Work",fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=math.floor(count/60)
        #Used to count in minutes

    count_sec=count%60
        #Used to count in seconds

    if count_sec <10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    #used itemconfig to change the timer_text in GUI along with f-string to take real time values and not constant

    if count > 0:
        if count > 0:
            global timer
            timer = windows.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        tick_symbol.config(text=marks)        
# ---------------------------- UI SETUP ------------------------------- #
windows=Tk()
windows.title("Pomodoro Project")
windows.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0) 
#sets the canvas width and height

tomato_img=PhotoImage(file="Day 29 (Pomodoro Project)/tomato.png") 
#image is stored into a variable. If not working then pasting relative address works better 

canvas.create_image(100,112,image=tomato_img) 
#Giving dimensions of the image and calling the image stored in the variable

timer_text=canvas.create_text(100,130,text="0:0",fill="white",font=(FONT_NAME,35,"bold")) 
#used for careting text and has attributes like font,text,etc.
canvas.grid(column=1,row=1)

timer_label=Label(text="Timer",font=("Consolas",40,"bold"),fg=GREEN,bg=YELLOW,highlightthickness=0)
timer_label.grid(column=1,row=0)

start_button=Button(text="start",command=start_timer)
start_button.grid(column=0,row=3)

reset_button=Button(text="reset",command=reset_timer)
reset_button.grid(column=2 ,row=3)

tick_symbol=Label(text="✔",fg=GREEN,pady=20,bg=YELLOW)
tick_symbol.grid(column=1,row=3)














windows.mainloop()