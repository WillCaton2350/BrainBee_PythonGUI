import tkinter as tk
import tkinter
from tkinter import ttk
import sqlite3
import customtkinter
import webbrowser
from tkinter import END
from tkinter import messagebox
try:
    from tkinter import *
except ImportError:
    from tkinter import *
import time
from tkinter import Tk
import random as rd

root  = tk.Tk()
root.geometry("350x450")
root.title("Brain Bee")
root.resizable(False, False)

def hideIndi():
    moovIndi.config(bg="#fff")
    audIndi.config(bg="#fff")
    podIndi.config(bg="#fff")
    homeIndi.config(bg="#fff")
    
def delete():
    for frame in mainFrame.winfo_children():
      frame.destroy()
      
def indi(lb,page):
    hideIndi()
    lb.config(background="lightblue")
    delete()
    page()
    
optionsFrame = tk.Frame(root, background="#fff")
moovBtn = tk.Button(root, text="BPY",font=('Bold',15),foreground="#141414",bd=0,background="lightblue",command= lambda: indi(moovIndi,moovPage))
moovBtn.place(x=10, y=50)
moovIndi = tk.Label(optionsFrame,text='',background="#eef2f3")
moovIndi.place(x=3,y=50,width=5,height=30)

audBtn = tk.Button(root, text="QID",font=('Bold',15),foreground="#141414",bd=0,background="lightblue",command= lambda: indi(audIndi,audPage))
audBtn.place(x=10, y=100)
audIndi = tk.Label(optionsFrame,text='',background="#eef2f3")
audIndi.place(x=3,y=100,width=5,height=30)

podBtn = tk.Button(root, text="BEE",font=('Bold',15),foreground="#141414",bd=0,background="lightblue",command= lambda: indi(podIndi,podPage))
podBtn.place(x=10, y=150)
podIndi = tk.Label(optionsFrame,text='',background="#eef2f3")
podIndi.place(x=3,y=150,width=5,height=30)

homeBtn = tk.Button(optionsFrame, text="☁",font=('Bold',15),foreground="lightblue",bd=0,background="#fff",command=lambda: indi(homeIndi,homepage))
homeBtn.place(x=10, y=200)
homeIndi = tk.Label(optionsFrame,background="lightblue")
homeIndi.place(x=3,y=200, width=5,height=30)


optionsFrame.pack(side=tk.LEFT)
optionsFrame.pack_propagate(False)
optionsFrame.config(background="lightblue")
optionsFrame.configure(width=100, height=450)

mainFrame = tk.Frame(root)
mainFrame.pack(side=tk.LEFT)
mainFrame.config(background="#eef2f3") 
mainFrame.pack_propagate(False)
mainFrame.configure(width=325, height=450)

mainLogoLabel = tk.Label(mainFrame,text="☁",fg="lightblue",background="#eef2f3",font=('Arial regular',215))
mainLogoLabel.pack(padx=50,pady=50)
mainLogoLabel.place(x=10,y=0)

mainFrameLabel = tk.Label(mainFrame, text="Brain \n Bee", background="lightblue",fg="#fff",font=('Arial, regular',35))
mainFrameLabel.pack(padx=100,pady=150)
mainFrameLabel.place(x=65,y=100,height=80)


def faqs():
  webbrowser.open_new_tab("")
infoFaqsBtn = customtkinter.CTkButton(mainFrame,text="sign in",hover_color="#eef2f3",text_color="#141414",fg_color="lightblue",bg_color="#eef2f3",command=faqs)
infoFaqsBtn.pack(padx=50,pady=50)
infoFaqsBtn.place(x=40,y=265)

def contact():
      webbrowser.open_new_tab("")
contactBtn = customtkinter.CTkButton(mainFrame,text="sign up",hover_color="#eef2f3",text_color="#141414",fg_color="lightblue",bg_color="#eef2f3",command=contact)
contactBtn.pack(padx=50,pady=50)
contactBtn.place(x=37,y=320)

def moovPage():
    moovFrame = tk.Frame(mainFrame)
    lb = tk.Label(moovFrame)
    lb.pack()
    moovFrame.pack(pady=20,)
    moovFrame = tkinter.LabelFrame(mainFrame)
    moovLabel = tkinter.Label(mainFrame,background="#fff",text="Brain Bee",font=('Arial bold',20))
    moovFrame.pack(padx=30, pady=0)
    moovLabel.place(x=30, y=20)
    class ratings():
        Rate = tkinter.Label(mainFrame,background='#fff', text="How are you feeling?")
        Rate.pack(padx=10,pady=10)
        Rate.place(x=37, y=75)
        rateMoov = ttk.Combobox(mainFrame,values=(["Great","Good", "Neutral", "Bad"]))
        rateMoov.pack(padx=0, pady=0)
        rateMoov.place(x=37, y=100)
        
    def enter():
        enterData = ratings.rateMoov.get()
        enterFeed = feedText.feedback.get()
        enterFeedEmail = feedText.email.get()
        if enterFeed == enterFeed:
            if enterData == enterData:
                print(enterData)
                if enterFeedEmail == enterFeedEmail:
                    print(enterFeedEmail)
            print(enterFeed)
            conn = sqlite3.connect('moov.db')
            cursor = conn.cursor()
            createTable = ''' CREATE TABLE IF NOT EXISTS moov_db
                            (rateMoov TEXT, feedback TEXT,email TEXT)'''
            cursor.execute(createTable)
            cursor.execute('''INSERT INTO moov_db VALUES(?,?,?)''',
            (ratings.rateMoov.get(), 
            feedText.feedback.get(),
            feedText.email.get(),
            ))
        else:
            conn.close()
        conn.commit() 
        conn.close()
        if enterData == "":
            if enterFeed == "":
                if enterFeedEmail == "":
                    messagebox.showwarning(title="Error",message="Required fields are missing")
                    print("Error.ratings") 
    Enter_btn = tkinter.Button(mainFrame,background="#fff", text="Enter", command=enter)
    Enter_btn.pack(padx=30, pady=100)
    Enter_btn.place(x=37,y=350)
    class feedText():
        feedbackLabel = tkinter.Label(mainFrame,background='#fff',text="Tell us why?")
        feedback = tkinter.Entry(mainFrame)
        feedbackLabel.place(x=37, y=130)
        feedback.place(x=37, y=160)
        email = ttk.Entry(mainFrame)
        def clear():
            feedText.feedback.delete(0,END)
            feedText.email.delete(0,END)
        Clear_btn = tkinter.Button(mainFrame,background="#fff", text="Clear", command=clear)
        Clear_btn.pack(padx=30,pady=100)
        Clear_btn.place(x=37,y=400)
        
       
def audPage(): 
    audFrame = tk.Frame(mainFrame)
    lb = tk.Label(audFrame)
    lb.pack()
    RAI_Text = customtkinter.CTkLabel(mainFrame,text="Quote of the day")
    RAI_Text.place(x=65,y=20)
    def qg():
        f=open("lotus.txt","r")
        lof=f.readlines()
        j=[]
        for i in range(len(lof)):
            if i%2==0:
                j.append(lof[i])
        print("Total quotes:",len(j)) 
        ind=rd.randint(0,50)
        print(ind)
        d=[j[ind]]
        d=d[0].split(" ")
        q=d[1:-2]
        quote=""
        for i in q:
            quote+=i+" "
        a=str(d[-2])+" "+str(d[-1])
        c=quote+"\n\n"+a
        print("Quote: ",quote," Author: -",a,sep="")
        return c
    def colorz():
        color=rd.choice(["#fcba03","#36e0e0","#b543bf","#f72545"])
        return color
    display_quote=Label(mainFrame,text="Press the button below", height=5,pady=6,wraplength=500,font=("Times",15,"bold"),bg="#f72545")
    display_quote.grid(row=0,column=0,stick="WE",padx=28,pady=15)
    display_quote.place(x=50,y=30)
    def fontz():
        font=rd.choice(["Aerial"])
        return font
    def qgenerate():
        display_quote.configure(text=str(qg()),fg="Black",font=fontz(),bg=colorz())
    button=Button(mainFrame,text="Generate Quote",command=qgenerate,bg="#2718c9",font="Times",fg="White",activebackground="#6b0e63",activeforeground="White")
    button.grid(row=1,column=0,stick="WE",padx=100,pady=100)
    
def podPage():#BEE
    podFrame = tk.Frame(mainFrame)
    lb = tk.Label(podFrame)
    lb.pack()
    podFrame.pack(pady=20)
    mainLogoLabel = tk.Label(mainFrame,text="☁",fg="lightblue",background="#eef2f3",font=('Arial regular',150))
    mainLogoLabel.pack(padx=50,pady=50)
    mainLogoLabel.place(x=40,y=-50)
    moovFrame = tkinter.LabelFrame(mainFrame)
    moovLabel = tkinter.Label(mainFrame,background="lightblue",foreground="#fff",text="Brain Bee",font=('Arial bold',20))
    moovFrame.pack(padx=30, pady=0)
    moovLabel.place(x=63, y=35)
    
    BEE_Text = customtkinter.CTkLabel(mainFrame,text="BEE")
    BEE_Text.place(x=100,y=150)
    
    
    def countdown():
        global loop_is_working
        loop_is_working = True
        greetinglist = ["/// BB ///", "/// Meditation ///", "/// Processing ///", "/// Brain Bee ///"]
        greeting = greetinglist[int(round(rd.random()*(len(greetinglist)-1),0))]
        b=5
        for i in range(1,6):
            print(greeting)
            t.set(str(greeting)+"\nMeditation starting in "+str(b)+" seconds")
            root.update_idletasks()
            print("Meditation starting in "+str(b))
            time.sleep(1)
            b -= 1
        root.after(0, loop)

    def loop():
        global loop_is_working
        
        inhalesleep = float(inhale.get())
        holdsleep = float(hold.get())
        exhalesleep = float(exhale.get())
        nohold = False

        if holdsleep == 0:
            nohold = True
    # I Need to get this Statement to move up between 20-50 pixels
        print(("Inhale for: ")+str(inhale.get())+(" seconds.\nHold for: ")+str(hold.get())+
        (" seconds.\nExhale for: ")+str(exhale.get())+" seconds.")
        t.set("Now Counting:\nInhale for: "+str(inhale.get())+" seconds.\nHold for: "+str(hold.get())+
        " seconds.\nExhale for: "+str(exhale.get())+" seconds.")
        root.update_idletasks()
        
        loop_is_working = False
        print(screen_width)
        print(screen_height)
        nohold = False

    def reset():
        global loop_is_working
        inhale.set(0)
        hold.set(0)
        exhale.set(0)
        t.set("Drag the sliders to set values")
        loop_is_working = False
        
    # I Need to get this Statement to move up between 20-50 pixels
    # t variavle is attached to the StringVar()
    t = StringVar()
    t.set("Meditation Scale")

    welcome = customtkinter.CTkLabel(podFrame, text_color="#6DD5FA", fg_color="#2980B9",
    width=136, height=6, textvariable=t)
    welcome.place(x=150,y=200)

    inhaleLabel = customtkinter.CTkLabel(podFrame,text="Inhale:")
    inhaleLabel.place(x=130,y=250)
    inhale = ttk.Scale(root,from_=0, to=5, orient=HORIZONTAL)
    inhale.place(x=180,y=250)

    holdLabel = customtkinter.CTkLabel(podFrame,text="Hold:")
    holdLabel.place(x=130,y=280)
    hold = ttk.Scale(root,
    from_=0, to=5, orient=HORIZONTAL)
    hold.place(x=180,y=280)

    exhaleLabel = customtkinter.CTkLabel(podFrame,text="Exhale:")
    exhaleLabel.place(x=130,y=310)
    exhale = ttk.Scale(root,
    from_=0, to=5, orient=HORIZONTAL)
    exhale.place(x=180,y=310)

    enter_btn = customtkinter.CTkButton(podFrame, text="START", command=countdown, text_color="#FFF200",
    width=39, height=8, fg_color="#0f9b0f")
    enter_btn.place(x=120,y=370)

    reset_btn = customtkinter.CTkButton(podFrame, text="RESET", command=reset, text_color="#FFF200",
    width=39, height=8, fg_color="#0f9b0f")
    reset_btn.place(x=200,y=370)

    exit_quit = customtkinter.CTkButton(podFrame, text="EXIT", command=exit, text_color="#FF0000",
    width=39, height=8, fg_color="#0f9b0f")
    exit_quit.place(x=280,y=370)
        
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

   


def homepage():
    mainLogoLabel = tk.Label(mainFrame,text="☁",fg="lightblue",background="#eef2f3",font=('Arial regular',215))
    mainLogoLabel.pack(padx=50,pady=50)
    mainLogoLabel.place(x=10,y=0)
    mainFrameLabel = tk.Label(mainFrame, text="Brain \n Bee", background="lightblue",fg="#fff",font=('Arial, regular',35))
    mainFrameLabel.pack(padx=100,pady=150)
    mainFrameLabel.place(x=65,y=100,height=80)
    def faqs():
      webbrowser.open_new_tab("")
    infoFaqsBtn = customtkinter.CTkButton(mainFrame,text="sign in",hover_color="#eef2f3",text_color="#141414",fg_color="lightblue",bg_color="#eef2f3",command=faqs)
    infoFaqsBtn.pack(padx=50,pady=50)
    infoFaqsBtn.place(x=40,y=265)
    def contact():
        webbrowser.open_new_tab("")
    contactBtn = customtkinter.CTkButton(mainFrame,text="sign up",hover_color="#eef2f3",text_color="#141414",fg_color="lightblue",bg_color="#eef2f3",command=contact)
    contactBtn.pack(padx=50,pady=50)
    contactBtn.place(x=37,y=320)
root.mainloop()