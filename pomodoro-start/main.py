
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0 #repetition 
check_txt="✔"
timer=None 
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    ''' 
    reset all the programe 
    delete a time_id to delete a past schedules 
    '''
    global reps,check_txt,timer
    reps=0
    if timer:
        window.after_cancel(timer)
    check_txt="✔"
    canvas.itemconfigure(timer_text, text="00:00")
    main_label.config(text="TIMER",fg=GREEN)
    check_mark.config(text="")

    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_mechanism():
    '''
    start_mechanism() is the entry of the programe 
    it show the sessions
    '''
    global reps,timer
    reps += 1
    if reps % 8 == 0:
        main_label.config(text="LONG BREAK",fg=RED)
        count_down(LONG_BREAK_MIN*60)

    elif reps % 2 == 0:
        main_label.config(text="SHORT BREAK",fg=PINK)
        count_down(SHORT_BREAK_MIN*60)

    else:
        main_label.config(text="WORK",fg=GREEN)
        count_down(WORK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    '''
    this function give the number of mins and secs decrement the count 
    call a start_mechanism to go for the next session and increment the reps
    update the check marks
    '''
    count_min=int (count//60) #the number of mins 
    count_sec=int (count%60) #the number of secs 
    global check_txt
    if count>0 : #decrement the count until it becomes zero then call a start_mechanism to go for the next session and increment the reps
        if count_sec <10: #check if the number of digits <2 concatenate 0
            count_sec="0"+str(count_sec)
        if count_min<10:
          count_min="0"+str(count_min)
          canvas.itemconfigure(timer_text,text=f"{count_min}:{count_sec}")
        timer=window.after(1000,count_down,count-1) #timer holds id of the scheduled countdown event ,It allows you to cancel the countdown when needed (in reset) 
        #after() function in Tkinter schedules a function to run after a certain number of milliseconds.
    else:
        start_mechanism()
        if reps%2==0:
            check_mark.config(text=check_txt) #add a check mark after each session work 
            check_txt+="✔"
# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
import time

#window
window=Tk()
window.title("pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


#canvas
tomato_img=PhotoImage(file="python_bootcamp\\pomodoro-start\\tomato.png") #we have to use PhotoImage function as we cann't pass a path in the canvas 
canvas=Canvas(width=200,height=244,bg=YELLOW,highlightthickness=0)#bg is background ,highlightthickness=0 this will delete the outerline around the canvas
canvas.create_image(100,120,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))#fill is the color 
canvas.grid(row=1,column=1)#using grid is more simple than place() and more control than pack()


#labels 
main_label=Label(text="TIMER",font=(FONT_NAME,50,"bold"),fg=GREEN,bg=YELLOW)#fg is foreground color
main_label.grid(row=0,column=1)


check_mark=Label(text="",font=(FONT_NAME,20,"bold"),fg=GREEN,bg=YELLOW)
check_mark.grid(row=2,column=1)


#buttons
start=Button(text="START",font=(FONT_NAME,10,"normal"),highlightthickness=0,command=start_mechanism)
start.grid(row=2,column=0)

reset=Button(text="RESET",font=(FONT_NAME,10,"normal"),highlightthickness=0,command=timer_reset)
reset.grid(row=2,column=2)


window.mainloop()