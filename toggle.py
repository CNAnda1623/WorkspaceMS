from tkinter import *
from mysql.connector import Error
import mysql.connector
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
#sql initialization
mydb = mysql.connector.connect(host='localhost', user='root', password='13102004', port='3306', database='w_m_s')
mycursor = mydb.cursor()

# whole frame
w = Tk()
w.geometry('900x500')
w.configure(bg='#262626')  # 12c4c0')
w.resizable(True,True)
w.title('Toggle Menu')

def promote():
    v=Tk()
    v.geometry('450x250')
    v.configure(bg='#262626')
    v.resizable(True,True)
    v.title('promotion')

    label3=Label(v,text='Name=',border=0,bg='#262626',fg='white',font=('Microsoft Yahei UI Light',15))
    label3.place(x=15,y=15)
    code4 = Entry(v, width=25, fg='#262626', border=0, bg='white', font=('Microsoft Yahei UI Light', 15))
    code4.place(x=90, y=14)
    # code1.insert(0,string='name')

    label4= Label(v, text='Salary=', border=0, bg='#262626', fg='white', font=('Microsoft Yahei UI Light', 15))
    label4.place(x=15, y=80)
    code6 = Entry(v, width=25, fg='#262626', border=0, bg='white', font=('Microsoft Yahei UI Light', 15))
    code6.place(x=90, y=80)

    def promo():
        mycursor = mydb.cursor()
        name=code4.get()
        salary=code6.get()
        # worker = mycursor.fetchall()
        try:
            query = "UPDATE w_m_s.user_login SET salary = %s WHERE name = %s"
            values = (salary, name)
            mycursor.execute(query,values)
            mydb.commit()
            mycursor.close()


        except Error as e:
            print(f"Error: {e}")




    buton = (Button(v,width=20,pady=7,text='Promote',bg='#57a1f8',fg='white',border=0,command=promo).place(x=150,y=190))



    v.mainloop()

def default_home():
    f2 = Frame(w, width=900, height=455, bg='#262626')
    f2.place(x=0, y=45)
    l2 = Label(f2, text='Home', fg='white', bg='#262626')
    l2.config(font=('Comic Sans MS', 90))
    l2.place(x=290, y=150 - 45)

def remove():
    z = Tk()
    z.geometry('450x150')
    z.configure(bg='#262626')
    z.resizable(True, True)
    z.title('promotion')

    label13 = Label(z, text='Name=', border=0, bg='#262626', fg='white', font=('Microsoft Yahei UI Light', 15))
    label13.place(x=15, y=15)
    code14 = Entry(z, width=25, fg='#262626', border=0, bg='white', font=('Microsoft Yahei UI Light', 15))
    code14.place(x=90, y=14)

    def rem():
        try:
            mycursor=mydb.cursor()
            name1 = code14.get()
            sql_delete = "DELETE FROM w_m_s.user_login WHERE name= %s"
            # DELETE FROM `w_m_s`.`user_login` WHERE(`username` = 'Suraj');
            values = [name1]
            mycursor.execute(sql_delete,values)
            mydb.commit()
        except Error as e:
            print(f"Error: {e}")
    buton1 = (Button(z,width=20,pady=7,text='Remove',bg='#57a1f8',fg='white',border=0,command=rem).place(x=150,y=100))


    z.mainloop()

def home():
    f1.destroy()
    #Home Dashboard Frame in black color
    f2 = Frame(w, width=900, height=455, bg='#262626')
    f2.place(x=0, y=45)
    #white screen of profile
    f9=Frame(f2,width=350,height=200,bg='#ffffff')
    f9.place(x=5,y=5)
    #small gray fame on white screen of profile
    f8=Frame(f9,width=100,height=200,bg='#808080')
    f8.place(x=0,y=0)
    # info for profile from dastabase
    mycursor.execute('SELECT * FROM w_m_s.admin_login')
    worker = mycursor.fetchall()
    for user in worker:
        name=user[0]
        break
    # name label
    label= Label(f9,text=name,fg='black',font='bold',bg='#ffffff')
    label.config(font=('comic Sans Ms',10))
    label.place(x=105,y=5)
    # company label
    label1= Label(f9,text='Company:',fg='black',bg='#ffffff')
    label1.config(font=('comic Sans Ms',10))
    label1.place(x=105,y=50)
    #info fetching
    mycursor.execute('SELECT * FROM w_m_s.admin_login')
    worker = mycursor.fetchall()
    for user in worker:
        company = user[2]
        break
    #company name label
    label0= Label(f9, text=company,fg='black',font='bold',bg='#ffffff')
    label0.config(font=('comic Sans Ms', 10))
    label0.place(x=170, y=50)
    # role label
    label2= Label(f9,text='Role:',fg='black',font='bold',bg='#ffffff')
    label2.config(font=('comic Sans Ms',10))
    label2.place(x=105,y=90)
    #info
    mycursor.execute('SELECT * FROM w_m_s.admin_login')
    worker = mycursor.fetchall()
    for user in worker:
        role = user[3]
        break
    #role name label
    label12 = Label(f9, text=role, fg='black',font='bold',bg='#ffffff')
    label12.config(font=('comic Sans Ms', 10))
    label12.place(x=140, y=90)
    # workspace capacity label
    label3= Label(f9,text='Workers Capacity=',fg='black',bg='#ffffff',font='bold')
    label3.config(font=('comic Sans Ms',10))
    label3.place(x=105,y=130)
    #info
    mycursor.execute('SELECT * FROM w_m_s.admin_login')
    worker = mycursor.fetchall()
    for user in worker:
        work_pos= user[4]
        break
    # workers capactiy label
    label3 = Label(f9, text=work_pos, fg='black',bg='#ffffff',font='bold')
    label3.config(font=('comic Sans Ms', 10))
    label3.place(x=240, y=130)

    slide_window()


def employees():
    f1.destroy()
    #whole black frame
    f59=Frame(w,width=900,height=455,bg='black')
    f59.place(x=0,y=45)
    #white widget for table
    f2 = Frame(f59, width=900, height=455, bg='white')
    f2.place(x=0, y=0)
    mydb = mysql.connector.connect(host='localhost', user='root', password='13102004', port='3306', database='w_m_s')
    # table making
    table = ttk.Treeview(f2, columns=('Employee Id', 'Name', 'Role', 'Status', 'Salary', 'Attendance', 'Project'),
                         show='headings')
    table.heading('Employee Id', text='Employee Id')
    table.heading('Name', text='Name')
    table.heading('Role', text='Role')
    table.heading('Status', text='Status')
    table.heading('Salary', text='Salary')
    table.heading('Attendance', text='Attendance')
    table.heading('Project', text='Project')
    table.pack(fill='both', expand=True)
    mycursor = mydb.cursor()
    mycursor.execute('SELECT employe_id,name,role,status,salary,attendance,projects FROM w_m_s.user_login')
    worker = mycursor.fetchall()
    for user, row in enumerate(worker):
        table.insert(parent='', index=user, values=row)

    button5 =Button(f59,width=30,pady=7,text='Promote',bg='#57a1f8',fg='white',border=0,command=promote).place(x=210,y=310)
    button6 =Button(f59,width=30,pady=7,text='Remove',bg='#57a1f8',fg='white',border=0,command=remove).place(x=490,y=310)

    w.mainloop()

def projects():
    f1.destroy()
    f2 = Frame(w, width=900, height=455, bg='white')
    f2.place(x=0, y=45)
    table = ttk.Treeview(f2, columns=('Name','Date','Due Date','Progress','Profit','Member[1]', 'Member[2]', 'Member[3]', 'Member[4]'),
                         show='headings')

    table.heading('Name', text='Name')
    table.heading('Date', text='Date')
    table.heading('Due Date', text='Due Date')
    table.heading('Progress', text='Progress')
    table.heading('Profit', text='Profit')
    table.heading('Member[1]', text='Member[1]')
    table.heading('Member[2]', text='Member[2]')
    table.heading('Member[3]', text='Member[3]')
    table.heading('Member[4]', text='Member[4]')
    table.pack(fill='both', expand=True)
    mycursor = mydb.cursor()
    mycursor.execute('SELECT name,date,due_date,progress,profit,mem1,mem2,mem3,mem4 FROM w_m_s.project')
    worker = mycursor.fetchall()
    for user, row in enumerate(worker):
        table.insert(parent='', index=user, values=row)

    slide_window()

def create_projects():
    f1.destroy()
    g1=Frame(w, width=900, height=455, bg='black')
    g1.place(x=0, y=45)
    p1 = Label(g1, text='Create a Project', fg='white', bg='black')
    p1.config(font=('Comic Sans MS', 30))
    p1.place(x=270, y=10)
    p2 = Label(g1, text='Project Name', fg='white', bg='black')
    p2.config(font=('Comic Sans MS', 12))
    p2.place(x=30, y=110)
    p3 = Label(g1, text='Date', fg='white', bg='black')
    p3.config(font=('Comic Sans MS', 12))
    p3.place(x=30, y=160)
    p4 = Label(g1, text='Due Date', fg='white', bg='black')
    p4.config(font=('Comic Sans MS', 12))
    p4.place(x=30, y=210)
    p5 = Label(g1, text='Profit', fg='white', bg='black')
    p5.config(font=('Comic Sans MS', 12))
    p5.place(x=30, y=260)
    p6 = Label(g1, text='Member1', fg='white', bg='black')
    p6.config(font=('Comic Sans MS', 12))
    p6.place(x=480,y=110)
    p7 = Label(g1, text='Member2', fg='white', bg='black')
    p7.config(font=('Comic Sans MS', 12))
    p7.place(x=480, y=160)
    p8 = Label(g1, text='Member3', fg='white', bg='black')
    p8.config(font=('Comic Sans MS', 12))
    p8.place(x=480, y=210)
    p9 = Label(g1, text='Member4', fg='white', bg='black')
    p9.config(font=('Comic Sans MS', 12))
    p9.place(x=480, y=260)
    lineedit1 = Entry(g1, width=25, fg='#262626', border=0, bg='white', font=('Microsoft Yahei UI Light', 15))
    lineedit1.place(x=150, y=110)
    lineedit2 = Entry(g1, width=25, fg='#262626', border=0, bg='white', font=('Microsoft Yahei UI Light', 15))
    lineedit2.place(x=150, y=160)
    date_obj=datetime.strptime(lineedit2.get(),'%Y-%m-%d')
    lineedit3 = Entry(g1, width=25, fg='#262626', border=0, bg='white', font=('Microsoft Yahei UI Light', 15))
    lineedit3.place(x=150, y=210)
    due_date_obj=datetime.strptime(lineedit3.get(),'%Y-%m-%d')
    lineedit4 = Entry(g1, width=25, fg='#262626', border=0, bg='white', font=('Microsoft Yahei UI Light', 15))
    lineedit4.place(x=150, y=260)
    lineedit5 = Entry(g1, width=25, fg='#262626', border=0, bg='white', font=('Microsoft Yahei UI Light', 15))
    lineedit5.place(x=580, y=110)
    lineedit6 = Entry(g1, width=25, fg='#262626', border=0, bg='white', font=('Microsoft Yahei UI Light', 15))
    lineedit6.place(x=580, y=160)
    lineedit7 = Entry(g1, width=25, fg='#262626', border=0, bg='white', font=('Microsoft Yahei UI Light', 15))
    lineedit7.place(x=580, y=210)
    lineedit8 = Entry(g1, width=25, fg='#262626', border=0, bg='white', font=('Microsoft Yahei UI Light', 15))
    lineedit8.place(x=580, y=260)
    button5 = Button(g1, width=30, pady=7, text='Create Project', bg='#57a1f8', fg='white', border=0).place(
        x=360, y=350)
    mydb = mysql.connector.connect(host='localhost', user='root', password='13102004', port='3306', database='w_m_s')
    mycursor = mydb.cursor()
    sqlFormula = "INSERT INTO w_m_s.project(name,date,due_date,profit,mem1,mem2,mem3,mem4) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    users = [lineedit1.get(),date_obj,due_date_obj,int(lineedit4.get()),lineedit5.get(),lineedit6.get(),lineedit7.get(),lineedit8.get()]
    mycursor.execute(sqlFormula, users)
    mydb.commit()
    slide_window()

def chatroom():
    f1.destroy()
    f2 = Frame(w, width=900, height=455, bg='white')
    f2.place(x=0, y=45)
    l2 = Label(f2, text='Projects', fg='black', bg='white')
    l2.config(font=('Comic Sans MS', 90))
    l2.place(x=320, y=150 - 45)
    slide_window()

def notification():
    f1.destroy()
    f2 = Frame(w, width=900, height=455, bg='white')
    f2.place(x=0, y=45)
    l2 = Label(f2, text='Projects', fg='black', bg='white')
    l2.config(font=('Comic Sans MS', 90))
    l2.place(x=320, y=150 - 45)
    slide_window()


# slidewindow
def slide_window():
    #f1 = slide window frame
    global f1
    f1 = Frame(w, width=150, height=500, bg='#12c4c0')
    f1.place(x=0, y=0)

    # buttons
    def bttn(x, y, text, bcolor, fcolor, cmd):
        def on_entera(e):
            myButton1['background'] = bcolor  # ffcc66
            myButton1['foreground'] = '#262626'  # 000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground'] = '#262626'

        myButton1 = Button(f1, text=text,
                           width=21,
                           height=2,
                           fg='#262626',
                           border=0,
                           bg=fcolor,
                           activeforeground='#262626',
                           activebackground=bcolor,
                           command=cmd)

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x, y=y)

    bttn(0, 80, 'H O M E', '#0f9d9a', '#12c4c0', home)
    bttn(0, 117, 'E M P L O Y E E S', '#0f9d9a', '#12c4c0', employees)
    bttn(0, 154, 'P R O J E C T S', '#0f9d9a', '#12c4c0', projects)
    bttn(0, 191, 'C R E A T E P R O J E C T S', '#0f9d9a', '#12c4c0',create_projects)
    bttn(0, 228, 'C H A T R O O M', '#0f9d9a', '#12c4c0', chatroom)
    bttn(0, 228+37, 'N O T I F I C A T I O N', '#0f9d9a', '#12c4c0', notification)
    # bttn(0, 265, 'A C E R', '#0f9d9a', '#12c4c0', None)

    #
    def dele():
        f1.destroy()
        b2 = Button(w, image=img1,
                    command=slide_window,
                    border=0,
                    bg='#262626',
                    activebackground='#262626')
        b2.place(x=5, y=8)

    global img2
    img2=PhotoImage(file="close.png")
    Button(f1,
           image=img2,
           border=0,
           command=dele,
           bg='#12c4c0',
           activebackground='#12c4c0').place(x=5, y=10)


default_home()

# img1 = ImageTk.PhotoImage(Image.open("open.png"))
img1 = PhotoImage(file="open.png")
global b2
b2 = Button(w, image=img1,
            command=slide_window,
            border=0,
            bg='#262626',
            activebackground='#262626')
b2.place(x=5, y=8)

w.mainloop()
