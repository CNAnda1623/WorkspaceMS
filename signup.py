from tkinter import*
from tkinter import messagebox
#sql initialization
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='13102004', port='3306', database='w_m_s')
mycursor = mydb.cursor()

color1 = '#020f12'
color2= '#05d7ff'
color3= '#65e7ff'
color4= '#65e7ff'

#whole screen
window=Tk()
window.title("signup")
window.geometry("925x500+300+200")
window.configure(bg='#fff')
window.resizable(True,True)


def signup_admin():
    username = user.get()
    password=int(code.get())
    confirm_password=int(code1.get())
    if password==confirm_password:
        sqlFormula = "INSERT INTO w_m_s.admin_login (username,password) VALUES (%s,%s)"
        users=(username,password)
        mycursor.execute(sqlFormula,users)
        mydb.commit()
        messagebox.showinfo("message", "Signup Successful")
def signup_user():
    username = user.get()
    password=int(code.get())
    confirm_password=int(code1.get())
    if password==confirm_password:
        sqlFormula = "INSERT INTO w_m_s.user_login (username,password) VALUES (%s,%s)"
        users=(username,password)
        mycursor.execute(sqlFormula,users)
        mydb.commit()
        messagebox.showinfo("message", "Signup Successful")


def sign():

    pass


#image on image frame on left side
img = PhotoImage(file='signup.png')
Label(window,image=img,border=0,bg='white').place(x=50,y=90)

# singup frame on right side
frame=Frame(window,width=350,height=390,bg='#fff')
frame.place(x=480,y=50)

# signup label
heading = Label(frame,text='Sign up',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=100,y=5)

# feature for username button
def on_enter(e):
    user.delete(0,"end")
def on_leave(e):

    if user.get()== '':
        user.insert(0,'Username')

# linedit for usernmae
user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)

# feature for password button
def on_enter(e):
    code.delete(0,"end")

def on_leave(e):

    if code.get()== '':
        code.insert(0,'password')

#lineedit for password
code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'password')
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)

# feature for confirm password button
def on_enter(e):
    code1.delete(0,"end")

def on_leave(e):

    if code1.get()== '':
        code1.insert(0,'confirm Password')

code1 = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
code1.place(x=30,y=220)
code1.insert(0,'Confirm Password')
code1.bind("<FocusIn>",on_enter)
code1.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=247)

Button(frame,width=39,pady=7,text='signup as admin',background=color1,foreground=color2,activebackground=color3,activeforeground=color4,highlightthickness=2,highlightbackground=color2,highlightcolor='White',cursor='hand2',border=0,command=signup_admin).place(x=35,y=280)
Button(frame,width=39,pady=7,text='signup as user',background=color1,foreground=color2,activebackground=color3,activeforeground=color4,highlightthickness=2,highlightbackground=color2,highlightcolor='White',cursor='hand2',border=0,command=signup_user).place(x=35,y=320)
label=Label(frame,text='I have an account',fg='black',bg='white',font=('Microsoft Yahei UI Light',9))
label.place(x=90,y=360)

signin=Button(frame,width=6,text='SignIn',border=0,bg='white',cursor='hand2',fg="#57a1f8",command=sign)
signin.place(x=200,y=360)

window.mainloop()

