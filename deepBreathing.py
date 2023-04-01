import time
import settings as st
from tkinter import *
from threading import *
import multiprocessing as mp
from playsound import playsound
from tkinter import ttk, messagebox

class Meditation:
    def __init__(self, root):
        # Window Settings
        self.window = root
        self.window.geometry(f"{st.width}x{st.height}")
        self.window.title('Meditation App')
        self.window.resizable(width = False, height = False)
        self.window.configure(bg=st.color2)

        # Tkinter Frame
        self.frame = Frame(self.window, bg=st.color1, \
        width=800, height=450)
        self.frame.place(x=0, y=0)

        # Default values
        self.inhale = True
        self.exhale = False
        self.onHomePage = False
        self.defaultTime = st.baseTime

        # Calling Home Page
        self.HomePage()

    # Manage the Home/Welcoming Window
    def HomePage(self):
        self.Reset()
        self.ClearScreen()
        self.RemainingTime(self.defaultTime)

    # Function to reset the default values
    def Reset(self):
        self.onHomePage = True
        self.inhale = True
        self.exhale = False
        self.defaultTime = st.baseTime

    # Clear all widgets from the Tkinter Frame
    def ClearScreen(self):
        for widget in self.frame.winfo_children():
            widget.destroy()





    
    # Label to show the remaining time of mediation
    def RemainingTime(self, rTime):
        mins, secs = divmod(rTime, 60)
        self.timeLabel = Label(self.frame, text=f"{mins}:{secs}", \
        bg=st.color2, fg=st.color3 ,font=(st.font3, 15))
        self.timeLabel.place(x=727, y=25)

    # A different window for setting the mediation period
    def SecondWindow(self):
        self.newWindow = Tk()
        self.newWindow.title("Set Time")
        self.newWindow.geometry(st.resolution)

        self.totalTime = IntVar()

        self.chosenTime = ttk.Combobox(self.newWindow, \
        textvariable=self.totalTime, values=st.timeList, \
        font=(st.font3, 20), width=8)
        self.chosenTime.set(1)
        self.chosenTime.place(x=160, y=110)

        setTimeBtn = Button(self.newWindow, text="Set Time", \
        font=(st.font4, 11), bg=st.color5, fg=st.color2, \
        cursor='hand2', command=self.GetTime)
        setTimeBtn.place(x=185, y=150)

    # It takes the time chosen by the user, and calculates in minutes
    # and seconds, and displays on the time label.
    def GetTime(self):
        self.defaultTime = int(self.chosenTime.get()) * 60
        self.newWindow.destroy()

        mins, secs = divmod(self.defaultTime, 60)

        self.timeLabel.config(text=f"{mins}:{secs}")
        self.timeLabel.update()

    # It manages the Mediation/Second page and all its widgets
    def MeditationPage(self):
        self.onHomePage = False
        self.ClearScreen()

        self.breathLabel = Label(self.frame, text="", \
        bg=st.color3, fg=st.color2 ,font=(st.font1, 28))
        self.breathLabel.place(x=387, y=172)

        self.statusLabel = Label(self.frame, text="", \
        bg=st.color2, fg=st.color3 ,font=(st.font4, 20))
        self.statusLabel.place(x=360, y=325)

        self.RemainingTime(self.defaultTime)

        # Call the function for Multi-Threading
        self.MultiThreading()

    # Function to create a different thread to handle
    # time management tasks.
    def MultiThreading(self):
        self.x = Thread(target=self.CountDown, daemon=True)
        self.x.start()
    
    # Creates a Tkinter Button to return to the Home/Welcoming Page

    # Function to handle time management tasks
    def CountDown(self):
        try:
            self.UpdateStatus("Relax!")
            process = self.PlayVoice(st.Relax)
            time.sleep(4)
            process.terminate()

            self.HomeButton()

            while self.defaultTime > 0:
                # Inhale CountDown
                if self.inhale:
                    # A separate process to play 'Inhale' voice
                    process = self.PlayVoice(st.Inhale)
                    # Countdown inhale time
                    self.CountInhale()
                    # Terminate the process
                    process.terminate()

                # Exhale CountDown                  
                elif self.exhale:
                    # A separate process to play 'Exhale' voice
                    process = self.PlayVoice(st.Exhale)
                    # Countdown exhale time
                    self.CountExhale()
                    # Terminate the process
                    process.terminate()

                # Time is up
                if self.defaultTime <= 0:
                    self.UpdateStatus("Done!!")
                    self.UpdateTime(0, 0)

                # To Break the outer loop:
                # If the user presses the Home button 
                # during meditation.
                if self.onHomePage:
                    break

        # Catch and display any exceptions, if arises.
        except Exception as es:
            messagebox.showerror("Error!", f"Error due to {es}")

    # Function to Count Inhale time repeatedly 
    # until the time ends up.
    def CountInhale(self):
        self.inhale = False
        self.exhale = True

        # getting the default inhale time
        inhale = st.inhaleTime

        # Update the Status with 'Inhale' text
        self.UpdateStatus("Inhale")

        while inhale > 0:
            # To Break the inner loop: If the user presses 
            # the Home button during inhaling.
            if self.onHomePage:
                break
            else:
                # Update the remaining time of meditation
                mins, secs = divmod(self.defaultTime, 60)
                self.UpdateTime(mins, secs)

                # Update the remaining inhale time
                self.UpdateBreathTime(inhale)

                # Decrease time by 1 per second
                inhale -= 1
                self.defaultTime -= 1
                time.sleep(1)

    # Function to Count Exhale time repeatedly
    # until the time ends up.
    def CountExhale(self):
        self.exhale = False
        self.inhale = True
        
        # getting the default exhale time
        exhale = st.exhaleTime

        # Update the Status with 'Exhale' text
        self.UpdateStatus("Exhale")

        while exhale > 0:
            # To Break the inner loop: If the user presses 
            # the Home button during exhaling.
            if self.onHomePage:
                break
            else:
                # Update the remaining time of meditation
                mins, secs = divmod(self.defaultTime, 60)
                self.UpdateTime(mins, secs)

                # Update the remaining exhale time
                self.UpdateBreathTime(exhale)

                # Decrease time by 1 per second
                exhale -= 1
                self.defaultTime -= 1
                time.sleep(1)

    # Function to update the status: Inhale/Exhale
    def UpdateStatus(self, msg):
        self.statusLabel.config(text=msg)
        self.statusLabel.update()

    # Function to update the remaining time
    def UpdateTime(self, mins, secs):
        self.timeLabel.config(text=f"{mins}:{secs}")
        self.timeLabel.update()

    def UpdateBreathTime(self, breath):
        self.breathLabel.config(text=f"{breath}")
        self.breathLabel.update()

    # It plays a .mp3 file to express the current
    # status of meditation: 'Inhale' or 'Exhale'.
    def PlayVoice(self, voice):
        process = mp.Process(target=playsound, args=(voice,))
        process.start()
        return process

# The main function
if __name__ == "__main__":
    # Instance of Tk class
    root = Tk()
    # Object of Meditation class
    obj = Meditation(root)
    root.mainloop()