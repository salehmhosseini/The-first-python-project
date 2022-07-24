from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Style

from captcha.image import *
import SignupPage
import ForgetPasswordPage
import random
import string

import webbrowser
class loginPage:

    def __init__(self):
        # creat an object from Tkinter
        root = Tk()

        # icon image
        iconImage = PhotoImage(file=r"C:\Users\HUAWEI\Desktop\FirstProject/logo.png")

        root.iconphoto(False, iconImage)
        root.config(bg='LightCyan2')

        root.geometry("1000x650")
        root.title("Login Page")
        root.resizable(False, False)

        # logo image
        logoImage = PhotoImage(file=r"C:\Users\HUAWEI\Desktop\FirstProject/logo.png")
        logoImage = logoImage.subsample(3, 3)

        # logo label
        logoLabel = Label(root, image=logoImage, bg='LightCyan2')
        logoLabel.pack()

        # xatrock label
        xatrockLabel = Label(root, text="Xatrock", fg="black", font=("segoe print", 20, "bold"), bg='LightCyan2')
        xatrockLabel.pack(fill="none" )

        # login Label
        loginLabel = Label(root, text="Login", fg="black", font=("segoe print", 20, "bold") , bg='LightCyan2')
        loginLabel.pack()

        # email label
        emailLabel = Label(root, text="Email", fg="black", font=("segoe print", 17, "bold") , bg='LightCyan2')
        emailLabel.pack()


        # email entry
        emailTextField = Entry(root , width=26, font=("plain", 13, "bold") , bd = 2)
        emailTextField.pack()

        # password label
        passLabel = Label(root, text="Password", fg="black", font=("segoe print", 17, "bold") , bg='LightCyan2')
        passLabel.pack()

        # password entry
        passTextField = Entry(root, width=26, show="*", font=("plain", 13, "bold") , bd=2)
        passTextField.pack()
        #function of switch to forget password page
        def switchToForgetPasswordPage(self):
            root.destroy()
            ForgetPasswordPage.forgetPassword()
        # foreget password hyper link
        def callback(url):
            webbrowser.open_new(url)

        forgetPasswordHyper = Label(root, text="Forget password", fg="blue",
                                    cursor="hand2" , font=("plain", 12) , bg='LightCyan2')
        forgetPasswordHyper.pack(pady=5)
        forgetPasswordHyper.bind("<Button-1>",switchToForgetPasswordPage)




       # catcha generator
        self.image = ImageCaptcha(width=200, height=60)
        self.x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase
                                       + string.digits) for _ in range(5))

        self.captcha_text = self.x


        self.image.write(self.captcha_text, 'CAPTCHA.png')

        self.captchaImage = PhotoImage(file=r"C:\Users\HUAWEI\PycharmProjects\FirstProject/CAPTCHA.png")
        self.captchaImage.subsample(80, 80)
        self.captchaLabel = Label(root, image=self.captchaImage)
        self.captchaLabel.pack(pady=10)
        # function of return button to handle it
        def returnButtonHandler():
           pass

        #captcha entry
        captchaEntry = Entry(root ,width=20 , font=("plain" ,13,  "bold") , bd=2 )
        captchaEntry.pack()

        #verify captcha button
        verifyButton = Button(root  ,text="verify" , font=("plain" , 12 ) , height=0
                              , cursor="hand2" , fg="red" , bg="#E4CDEF" )

        verifyButton.place(x=610 , y=449)

        # change the captcha code by cliking on return button

        returnImage = PhotoImage(file=r"C:\Users\HUAWEI\Desktop\FirstProject/return.png")
        returnLabel= Label(root , image =returnImage , cursor="hand2" , bg='LightCyan2')
        returnLabel.bind("<Button-1>" , returnButtonHandler())

        returnLabel.place(x=610 , y=392)



        # loginLabel.config(text = input.get())
        def loginButtonHandler():

               messagebox.showinfo("Login status ", "You are successfully loged in!" )
        #check robot label
        checkRobotLabel = Label(text="Im NOT a robot " , font=("plain" ,12) , bg="LightCyan2")

        checkRobotLabel.place(x=438 , y=480)


        # check button
        tk.Checkbutton(root,
             text='',
             onvalue='agree',
             offvalue='disagree' , bg='LightCyan2' , fg="green").place(x=548 , y=480)



        # login button
        loginButton = Button(root, width=14, height=-10, text="Login", fg="red", bg="#E4CDEF",
                             font=("plain", 12),
                             command=loginButtonHandler, cursor="hand2")
        loginButton.pack(pady=35)

        #dont have an account label
        dontHaveAccountLabel = Label(root , text = "Dont have an account?" , font=("plain" , 12)
                                     , bg='LightCyan2')
        dontHaveAccountLabel.pack()

        #function of switch to cignup page
        def switchToSignUpPage(self):
             root.destroy()
             SignupPage.singUp()

        #signuo hyper link label
        signUpHyperLabel = Label(root , text = "sign up here" , font=("plain" , 12) , fg="blue"
                                 , cursor="hand2" , bg='LightCyan2')
        signUpHyperLabel.pack(pady=5)
        signUpHyperLabel.bind("<Button-1>",switchToSignUpPage)

        root.mainloop()