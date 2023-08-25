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
start_time = 5
reps = 1
reset_loop = False
tracker = ""
# ---------------------------- TIMER RESET ------------------------------- # 


def reset():
    global reps, reset_loop, tracker
    reps = 1
    tracker = ""
    checkmark_label.config(text=tracker)
    canvas.itemconfig(timer_text, text="25:00")
    timer_label.config(text="Timer")
    reset_loop = True

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps, tracker

    checkmark_label.config(text=tracker)

    if reps % 8 == 0:
        count_down(int(LONG_BREAK_MIN * 60))
        timer_label.config(text="Long Break")
        reps = 0
        tracker = ""

    elif reps % 2 == 1:
        count_down(int(WORK_MIN * 60))
        timer_label.config(text=f"Work Period {reps // 2 + 1}/4")
        tracker += "✔"

    else:
        count_down(int(SHORT_BREAK_MIN * 60))
        timer_label.config(text=f"Rest Period {reps // 2}")

    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global reset_loop

    if count >= 0:
        if reset_loop:
            count = WORK_MIN * 60
            reset_loop = False

        else:
            canvas.itemconfig(timer_text, text="{:02d}:".format(count//60) + "{:02d}".format(count % 60))
            print(count)
            window.after(1000, count_down, count-1)

    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Technique Interface")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(bg=YELLOW, highlightthickness=0)
pomodoro_img = PhotoImage(file="tomato.png")
canvas.create_image(180, 135, image=pomodoro_img)
timer_text = canvas.create_text(180, 150, text="25:00", fill="white", font=(FONT_NAME, 20, "bold") )
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
timer_label.grid(column=1, row=0)

checkmark_label = Label(text=tracker, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

window.mainloop()