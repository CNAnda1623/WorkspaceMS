from tkinter import *
from tkinter import messagebox
#initialization for sql
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='13102004', port='3306', database='w_m_s')
mycursor = mydb.cursor()

color1 = '#020f12'
color2= '#05d7ff'
color3= '#65e7ff'
color4= '#65e7ff'

#whole frame
root = Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(True, True)

def new_screen():
    screen = Toplevel(root)
    screen.title("App")
    screen.geometry('925x500+300+200')
    screen.configure(bg="white")

    Label(screen, text="HELLO EVERYONE", bg="#fff", font=('Calibri(Body)', 50, 'bold')).pack(expand=True)
    screen.mainloop()

#admin authentication
def real_admin(Username, Password):
    mycursor.execute('SELECT * FROM w_m_s.admin_login')
    worker = mycursor.fetchall()
    for user in worker:
        db_username = (user[0])
        db_password = (user[1])
        if db_username == Username and db_password == Password:
            return True
        elif db_username != Username and db_password == Password:
            messagebox.showerror("Invalid", "invalid username")
        elif db_password != Password and db_username == Username:
            # line : password wrong
            messagebox.showerror("Invalid", "invalid password")
        else:
            pass

# user authentication
def real_user(Username, Password):
    mycursor.execute('SELECT * FROM w_m_s.user_login')
    worker = mycursor.fetchall()
    for user in worker:
        db_username = (user[0])
        db_password = (user[1])
        if db_username == Username and db_password == Password:

            return True
        elif db_username != Username and db_password == Password:
            # line : username wromg
            messagebox.showerror("Invalid", "invalid username")
        elif db_password != Password and db_username == Username:
            # line : password wrong
            messagebox.showerror("Invalid", "invalid password")
        else:
            pass

# actionlistener for admin login button
def signin_admin():
    Username = user.get()
    Password = code.get()
    if real_admin(Username, int(Password)):
        new_screen()

# actionlistener for user login button

def signin_user():
    Username = user.get()
    Password = code.get()
    if real_user(Username, int(Password)):
        new_screen()




#left Frame for image
img = PhotoImage(file="login.png")
Label(root, image=img, bg="white").place(x=50, y=50)
frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)


#right frame for login
heading_signin = Label(frame, text="Sign in", fg="#57a1f8",bg='White' ,font=("Microsoft Yahei UI Light", 23, "bold"))
heading_signin.place(x=100, y=5)

# LAbel of login
user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, "username")


#special feature for username
def on_enter(e):
    user.delete(0, "end")


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


#lineedit for username
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)
code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))




#special feature for password
def on_enter(e):
    code.delete(0, "end")


def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')

#lineedit for password
code.place(x=30, y=150)
code.insert(0, "Password")
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

# Button for signin as admin
Button(frame, width=39, pady=7, text="sign in as Admin", background=color1,foreground=color2,activebackground=color3,activeforeground=color4,highlightthickness=2,highlightbackground=color2,highlightcolor='White',cursor='hand2', border=0, command=signin_admin).place(x=35, y=204)

# Button for signin as user
Button(frame, width=39, pady=7, text="sign in as user", background=color1,foreground=color2,activebackground=color3,activeforeground=color4,highlightthickness=2,highlightbackground=color2,highlightcolor='White',cursor='hand2',border=0, command=signin_user).place(x=35, y=250)

#label for dont have an account
label = Label(frame, text="Don't have an aacount?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
label.place(x=75, y=300)

#small signin button
sign_up = Button(frame, width=6, text="sign up", border=0, bg="white", cursor="hand2", fg="#57a1f8")
sign_up.place(x=215, y=300)


root.mainloop()

