from tkinter import *
from PIL import ImageTk,Image
import os
import random

Credentials='Saveddata.temp'
def Captcha():
    global captcha
    global a
    global rootC
    a=random.randrange(0,13)
    cAPS=['28ivw','FH2DE','e5hb','gwprp','HRAI','jw62k','k4ez','q98p','4D7YS','xmqki','XDHYN','6ne3']
    rootC=Tk()
    rootC.title('Read Captcha')
    instruction=Label(rootC,text='Type the characters that you see below:\n')
    instruction.grid(columnspan=2,row=0,column=0)
    captcha=Entry(rootC)
    im = Image.open(cAPS[a]+'.gif')
    render = ImageTk.PhotoImage(im)
    img = Label(rootC, image=render)
    img.image = render
    img.grid(row=2,column=1,sticky="")
    captcha.grid(row=3,column=1)
    submit=Button(rootC,text="Submit",command=CheckCap)
    submit.grid(columnspan=1,rowspan=200,sticky=W)
    rootC.mainloop()
def CheckCap():
    cAPS=['28ivw','FH2DE','e5hb','gwprp','HRAI','jw62k','k4ez','q98p','4D7YS','xmqki','XDHYN','6ne3']
    if captcha.get()==cAPS[a]:
        rootC.destroy()
        Home()
    else:
        rootC.destroy()
        r = Tk()
        r.title('Warning')
        r.geometry('150x50')
        rlbl = Label(r, text='\nWrong Input!\nTry Again')
        rlbl.pack()
        r.mainloop()
        Captcha()
        print("Try Again")
def Login():
    global nameEL
    global pwordEL
    global rootL
    rootL=Tk()
    rootL.geometry('350x150')
    rootL.title("Login")
    instruction = Label(rootL, text='Please Enter Your Credentials\n') 
    instruction.grid(row=0,column=0,sticky=E)
    nameL = Label(rootL,text='Username: ') 
    pwordL = Label(rootL, text='Password: ')
    nameL.grid(row=1, column=0, sticky=W)
    pwordL.grid(row=2, column=0, sticky=W)
    nameEL = Entry(rootL)
    pwordEL = Entry(rootL, show='*')
    nameEL.grid(row=1,column=1) 
    pwordEL.grid(row=2,column=1)
    loginB = Button(rootL,text='Login',command=CheckLog)
    loginB.grid(columnspan=2,sticky="")
    delB=Button(rootL,text='Delete Account',command=DelAcc)
    delB.grid(columnspan=2,sticky="")
    rootL.mainloop()
def CheckLog():
    with open(Credentials) as f:
        data = f.readlines() 
        uname = data[0].rstrip()
        pword = data[1].rstrip() 
    if nameEL.get() == uname and pwordEL.get() == pword: 
        rootL.destroy()
        Captcha()
    else:
        r = Tk()
        r.title('Warning')
        r.geometry('150x50')
        rlbl = Label(r, text='\nInvalid Login')
        rlbl.pack()
        r.mainloop()
def DelAcc():
    os.remove(Credentials)
    rootL.destroy()
    Signup()
def Signup():
    global nameES
    global pwordES
    global rootS
    rootS=Tk()
    rootS.title('Sign-Up')
    instruction=Label(rootS, text="Please Enter your Credentials\n")
    instruction.grid(row=0,column=0,sticky=E)
    nameS=Label(rootS,text='Username: ')
    pwordS=Label(rootS,text='Password: ')
    nameS.grid(row=1, column=0, sticky=W)
    pwordS.grid(row=2,column=0,sticky=W)
    nameES=Entry(rootS)
    pwordES=Entry(rootS,show="*")
    nameES.grid(row=1,column=1)
    pwordES.grid(row=2,column=1)
    signup=Button(rootS,text='Create a new account',command=SaveData)
    signup.grid(columnspan=2, stick=W)
    rootS.mainloop()
def SaveData(): 
    with open(Credentials, 'w') as f:
        f.write(nameES.get()) 
        f.write('\n') 
        f.write(pwordES.get()) 
    rootS.destroy()
    Login()
def Home():
    global rootH
    rootH=Tk()
    rootH.title('Home')
    rootH.geometry('300x380')
    instruction=Label(rootH,text='Welcome Aboard\n')
    im = Image.open('download.jpeg')
    render = ImageTk.PhotoImage(im)
    img = Label(rootH, image=render)
    img.image = render
    img.grid(row=2,column=2,columnspan=2,sticky="")
    instruction.grid(row=1,column=2,columnspan=2)
    intro=Label(rootH,text='This Project was made by:\nShivani Sharma')
    intro.grid(row=3,column=2,columnspan=2)
    exit=Button(rootH,text='Exit',command=close)
    exit.grid(row=4,column=1,sticky="")
    rootH.mainloop()
def close():
    rootH.destroy()
if os.path.isfile(Credentials):
    Login()
else:
    Signup()
