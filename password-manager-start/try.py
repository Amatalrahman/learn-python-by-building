from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("main window ")
# button=Button(window,text="main window")
# button.grid(row=0,column=1)


completion_window=Toplevel(window)
completion_window.wm_minsize(width=250,height=150)
completion_window.config(pady=50,padx=50)
completion_window.wm_title("saveed successfully")
check_img=PhotoImage(file="python_bootcamp\\password-manager-start\\check_mark.png")
check_label=Label(completion_window,image=check_img)
check_label.pack()
saved_label=Label(completion_window,text="password saved successfully",font=("arial",12,"bold"))
saved_label.pack()


mainloop()