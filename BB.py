import tkinter as tk
import tkinter
from tkinter import ttk
import sqlite3
import customtkinter
import webbrowser
from tkinter import END
from tkinter import messagebox
root  = tk.Tk()
root.geometry("325x450")
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
moovBtn = tk.Button(root, text="MOV",font=('Bold',15),foreground="#141414",bd=0,background="lightblue",command= lambda: indi(moovIndi,moovPage))
moovBtn.place(x=10, y=50)
moovIndi = tk.Label(optionsFrame,text='',background="#eef2f3")
moovIndi.place(x=3,y=50,width=5,height=30)

audBtn = tk.Button(root, text="AUD",font=('Bold',15),foreground="#141414",bd=0,background="lightblue",command= lambda: indi(audIndi,audPage))
audBtn.place(x=10, y=100)
audIndi = tk.Label(optionsFrame,text='',background="#eef2f3")
audIndi.place(x=3,y=100,width=5,height=30)

podBtn = tk.Button(root, text="POD",font=('Bold',15),foreground="#141414",bd=0,background="lightblue",command= lambda: indi(podIndi,podPage))
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
        Rate = tkinter.Label(mainFrame,background='#fff', text="Stars:")
        Rate.pack(padx=10,pady=10)
        Rate.place(x=37, y=75)
        rateMoov = ttk.Combobox(mainFrame,values=(["✰✰✰✰✰✰✰","✰✰✰✰✰✰", "✰✰✰✰✰", "✰✰✰✰", "✰✰✰", "✰✰","✰"]))
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
        if enterData == "✰✰✰✰✰✰✰":
            if enterFeed == "":
                if enterFeedEmail == "":
                    messagebox.showwarning(title="Error",message="Required fields are missing")
                    print("Error.ratings") 
    Enter_btn = tkinter.Button(mainFrame,background="#fff", text="Enter", command=enter)
    Enter_btn.pack(padx=30, pady=100)
    Enter_btn.place(x=37,y=350)
    class feedText():
        feedbackLabel = tkinter.Label(mainFrame,background='#fff',text="Comment:")
        feedback = tkinter.Entry(mainFrame)
        feedbackLabel.place(x=37, y=220)
        feedback.place(x=37, y=247)
        emailLabel = tkinter.Label(mainFrame,background='#fff',text="Email:")
        email = tkinter.Entry(mainFrame)
        emailLabel.place(x=37, y=280)
        email.place(x=37, y=305)
        def clear():
            feedText.feedback.delete(0,END)
            feedText.email.delete(0,END)
        Clear_btn = tkinter.Button(mainFrame,background="#fff", text="Clear", command=clear)
        Clear_btn.pack(padx=30,pady=100)
        Clear_btn.place(x=37,y=400)
        def callback():
            webbrowser.open_new_tab("www.netflix.com")
        netflixBtn = tkinter.Button(mainFrame,foreground="red",background="white", text="NETFLIX",command=callback)
        netflixBtn.pack(padx=50,pady=50)
        netflixBtn.place(x=37,y=140)
        def hulu():
            webbrowser.open_new_tab("www.hulu.com")
        huluBtn = tkinter.Button(mainFrame,foreground="#0f9b0f",background="#fff", text="HULU",command=hulu)
        huluBtn.pack(padx=50,pady=50)
        huluBtn.place(x=37,y=180)
        ########################################################################################################################################
def audPage():
    audFrame = tk.Frame(mainFrame)
    lb = tk.Label(audFrame)
    lb.pack()
    audFrame.pack(pady=20,)
    moovFrame = tkinter.LabelFrame(mainFrame)
    moovLabel = tkinter.Label(mainFrame,background="#fff",text="Brain Bee",font=('Arial bold',20))
    moovFrame.pack(padx=30, pady=0)
    moovLabel.place(x=30, y=20)
    if homeBtn == homeBtn:
        audFrame.destroy()
    class ratings():
        Rate = tkinter.Label(mainFrame,background='#fff', text="Stars:")
        Rate.pack(padx=10,pady=10)
        Rate.place(x=37, y=75)
        rateMoov = ttk.Combobox(mainFrame,values=(["✰✰✰✰✰✰✰","✰✰✰✰✰✰", "✰✰✰✰✰", "✰✰✰✰", "✰✰✰", "✰✰","✰"]))
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
            conn = sqlite3.connect('aud.db')
            cursor = conn.cursor()
            createTable = ''' CREATE TABLE IF NOT EXISTS aud_db
                            (rateMoov TEXT, feedback TEXT,email TEXT)'''
            cursor.execute(createTable)
            cursor.execute('''INSERT INTO aud_db VALUES(?,?,?)''',
            (ratings.rateMoov.get(), 
            feedText.feedback.get(),
            feedText.email.get(),
            ))
        else:
            conn.close()
        conn.commit() 
        conn.close()
        if enterData == "✰✰✰✰✰✰✰":
            if enterFeed == "":
                if enterFeedEmail == "":
                    messagebox.showwarning(title="Error",message="Required fields are missing")
                    print("Error.ratings") 
    Enter_btn = tkinter.Button(mainFrame,background="#fff", text="Enter", command=enter)
    Enter_btn.pack(padx=30, pady=100)
    Enter_btn.place(x=37,y=350)
    class feedText():
        feedbackLabel = tkinter.Label(mainFrame,background='#fff',text="Comment:")
        feedback = tkinter.Entry(mainFrame)
        feedbackLabel.place(x=37, y=220)
        feedback.place(x=37, y=247)
        emailLabel = tkinter.Label(mainFrame,background='#fff',text="Email:")
        email = tkinter.Entry(mainFrame)
        emailLabel.place(x=37, y=280)
        email.place(x=37, y=305)
        def clear():
            feedText.feedback.delete(0,END)
            feedText.email.delete(0,END)
        Clear_btn = tkinter.Button(mainFrame,background="#fff", text="Clear", command=clear)
        Clear_btn.pack(padx=30,pady=100)
        Clear_btn.place(x=37,y=400)
        def soundcloud():
            webbrowser.open_new_tab("www.soundcloud.com")
        netflixBtn = tkinter.Button(mainFrame,foreground="#ff7700",background="#fff", text="SoundCloud",command=soundcloud)
        netflixBtn.pack(padx=50,pady=50)
        netflixBtn.place(x=37,y=140)
        def spotify():
            webbrowser.open_new_tab("www.spotify.com")
        huluBtn = tkinter.Button(mainFrame,foreground="#1DB954",background="#fff", text="Spotify",command=spotify)
        huluBtn.pack(padx=50,pady=50)
        huluBtn.place(x=37,y=180)
  ######################################################################################################      
def podPage():
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