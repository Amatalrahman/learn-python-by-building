# ---------------------------- COSTANTS------------------------------- #
FONT="Bebas Neue"





# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random 
# Alphabets
lowercase_letters = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m',
                      'n','o','p','q','r','s','t','u','v','w','x','y','z' ]

uppercase_letters = [ 'A','B','C','D','E','F','G','H','I','J','K','L','M',
                      'N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]

# Numbers
numbers = [ '0','1','2','3','4','5','6','7','8','9' ]

# Symbols
symbols = [ '.',',',';' ,':',"'",'"','!','?','+','-','*','/','=','%','<','>',
            '(' ,')','[',']','{','}','@','#','$','&','_','|','\\','^','~' ]

#list for all_lists 
all_lists=[lowercase_letters,uppercase_letters,numbers,symbols]


password=""
def pass_gen():
    global password
    global v
    password=""
    for length in range (random.randrange (8,16)):
        password+=random.choice (random.choice(all_lists))
    print (password)
    v.set(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    global password
    web=web_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    if len(web)==0 or len(password)==0 :
        retry=messagebox.showwarning(title="error",message="web or password is empty")
    else:
        is_ok=messagebox.askokcancel(title="website",message=f"the website is {web} and the Email is {email} the password is {password} is this Ok")
        if is_ok:
            with open ("python_bootcamp\\password-manager-start\\pass_file.txt",mode="a")as pass_file:
                pass_file.write(f"{web} | {email} |{password} \n")
                web_entry.delete(0,END)
                password_entry.delete(0,END)
                password=NONE
        
    #another idea was to use toplevel window that containe icon 
    # completion_window=Toplevel(window)
    # completion_window.wm_minsize(width=250,height=150)
    # completion_window.config(pady=50,padx=50)
    # completion_window.wm_title("saveed successfully")
    # check_img=PhotoImage(file="python_bootcamp\\password-manager-start\\check_mark.png")
    # check_label=Label(completion_window,image=check_img)
    # check_label.image_names=check_img
    # check_label.pack()
    # saved_label=Label(completion_window,text="password saved successfully",font=("arial",12,"bold"))
    # saved_label.pack()

            
# ---------------------------- UI SETUP ------------------------------- #
from tkinter import*
from tkinter import messagebox
window =Tk()
window.title("password manger")
window.config(padx=50,pady=20)

#logo
lock_img=PhotoImage(file="python_bootcamp\\password-manager-start\\logo.png") 
Label_img=Label(image=lock_img)
Label_img.grid(row=0,column=1)

#labels
web_label=Label(text="website",font=(FONT,12,"bold"))
web_label.grid(row=1,column=0)

email_label=Label(text="Email/Username",font=(FONT,12,"bold"))
email_label.grid (row=2,column=0)

password_label=Label(text="Password",font=(FONT,12,"bold"))
password_label.grid(row=3,column=0)


#entry
web_entry=Entry()
web_entry.config(width=50)
web_entry.focus()
web_entry.grid(row=1,column=1,columnspan=2)


email_entry=Entry()
email_entry.config(width=50)
email_entry.insert(0,"AmatAlrahman@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2)


v=StringVar()
password_entry=Entry(window,textvariable=v)
password_entry.config(width=33)
password_entry.grid(row=3,column=1)


#buttons 
pass_gen_button=Button(text="generation",font=(FONT,9,"bold"),command=pass_gen)
pass_gen_button.config(width=13)
pass_gen_button.grid(row=3,column=2)

add_button=Button(text="Add",font=(FONT,9,"bold","bold"),command=add_pass)
add_button.config(width=42)
add_button.grid(row=4,column=1,columnspan=2)

mainloop()