from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)



        #background image input code with Text
        self.bg=ImageTk.PhotoImage(file="2A.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0, relwidth=1, relheight=1)
        self.bg_image = Label(root, text="Pavilion of Praise", font="impact 25 bold").grid(row=0, column=3)

        #Login frame
        Frame_login= Frame(self.root, bg="white")
        Frame_login.place(x=330, y=150, width=500, height=600)

        #Title & subtitle
        title =Label(Frame_login, text="Login Here", font=("impact",35,"bold"),fg="#6162FF",bg="white").place(x=90,y=30)
        subtitle = Label(Frame_login, text="Members Login Area", font=("Goudy old style", 15, "bold"), fg="#1d1d1d", bg="white").place(x=90,y=100)

        #Username
        lbl_user = Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(x=90,y=140)
        self.username = Entry(Frame_login, font=("Goudy old style", 15), bg="#E7E6E6")
        self.username.place(x=90, y=170,width=320,height=35)

        #Password
        lbl_password = Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="grey",bg="white").place(x=90,y=210)
        self.password = Entry(Frame_login, font=("Goudy old style", 15), bg="#E7E6E6")
        self.password.place(x=90, y=240, width=320, height=35)

        #Button
        forget=Button(Frame_login, text="forgot password?",bd=0,cursor="hand2", font=("Goudy old style", 12), fg="#6162FF",bg="white").place(x=90,y=280)
        submit = Button(Frame_login,command=self.check_function,cursor="hand2", text="Login", bd=0, font=("Goudy old style", 15), bg="#6162FF",fg="white").place(x=90, y=320,width=180,height=40)
        create_new=Button(Frame_login,cursor="hand2", text="create new account", bd=0, font=("Goudy old style", 18), bg="green",fg="white").place(x=90, y=360,width=210,height=40)

    def check_function(self):
        if self.username.get()==""or self.password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.username.get()!="General Larshy" or self.password.get()!="12345_":
            messagebox.showerror("Error", "Invalid Username or Password",parent=self.root)
        else:
            messagebox.showinfo("Welcome",f"Welcome to Pavilion of Praise {self.username.get()}")










root = Tk()
obj= Login(root)
root.mainloop()