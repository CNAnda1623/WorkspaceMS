from tkinter import *

root = Tk()
root.title("Starter")
root.geometry("800x500+300+200")
root.configure(bg="#fff")
root.resizable(True, True)

img2=PhotoImage(file='WhatsApp Image 2024-02-07 at 13.05.20_d1052232 (1).png')
Label(root, image=img2, bg="white").place(x=0,y=0)

Button(root, width=29, pady=7, text="Get Started", bg="#57a1f8", fg="white", border=0).place(x=520, y=400)

root.mainloop()