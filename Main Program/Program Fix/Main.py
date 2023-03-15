from doctest import OutputChecker
import threading
from tkinter import *
import os
from tkinter import ttk
import subprocess
from turtle import back
from webbrowser import BackgroundBrowser
import redis
import time
from PIL import Image, ImageTk
#========================================================================================================================
#-------------------------------------------> Redis Server <-------------------------------------------------------------
redis_host = "localhost"
redis_port = 6379
redis_password = ""
r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
#-----------------------------------------------------------------------------------------------------------------------
# Create an instance of Tkinter frame
win = Tk()
#========================> Menjalankan Redis Sever <==========
def jalankanRedis():
    subprocess.run("redis-server", shell=True)
t1 = threading.Thread(target=jalankanRedis)
t1.start()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def stop():
    subprocess.run("taskkill /F /IM redis-server.exe")
    subprocess.run("taskkill /F /IM python.exe")
#=====================> button start <=========================
def postRedis():
    inputValue=inputtxtStart.get("1.0","end-1c")
    #print(inputValue)
    link = "python bacaRefbox.py" + " "+inputValue
    subprocess.run(link)
    output = subprocess.getoutput()
    print(" hai")
def post():
    t2 = threading.Thread(target=postRedis)
    t2.start()
#***************************************************************
#======================> Robot 1 <==============================
def robot1():
    inputValueR1=inputtxtR1.get("1.0","end-1c")
    print(inputValueR1)
    link = "python sendRobot.py" + " "+inputValueR1
    subprocess.run(link)
    #output = subprocess.getoutput()
    #print(" hai")
def robot1send():
    t2 = threading.Thread(target=robot1)
    t2.start()
#***************************************************************
#======================> Robot 2 <==============================
def robot2():
    inputValueR2=inputtxtR2.get("1.0","end-1c")
    print(inputValueR2)
    link = "python sendRobot2.py" + " "+inputValueR2
    subprocess.run(link)
    #output = subprocess.getoutput()
    #print(" hai")
def robot2send():
    t2 = threading.Thread(target=robot2)
    t2.start()
#***************************************************************
#======================> Robot 3 <==============================
def robot3():
    inputValueR3=inputtxtR3.get("1.0","end-1c")
    print(inputValueR3)
    link = "python sendRobot3.py" + " "+inputValueR3
    subprocess.run(link)
    #output = subprocess.getoutput()
    #print(" hai")
def robot3send():
    t2 = threading.Thread(target=robot3)
    t2.start()
#***************************************************************

# Define the geometry
#win.geometry("750x350")
win.geometry("450x450")
win.resizable(0,0)
win.title("BaseStation")
#win.config(bg='#0f4b6f')
win.config(bg='#4a7a8c')
frame = Frame(win)
frame.pack()
image = Image.open("backGround.png")
w = 600
h = 450
resize_img = image.resize((w, h))
img = ImageTk.PhotoImage(resize_img)
disp_img = Label()
disp_img.pack(pady=20)
disp_img.config(image=img)
disp_img.image = img
#====================================================================================
# Create Buttons in the frame                                                       |
buttonStart = ttk.Button(win, text="START",command=post)#                           |
buttonStart.place(x=10, y=120)#                                                      |
inputtxtStart = Text(win,height = 1,width = 20)#                                    |
inputtxtStart.place(x=100,y=120)#                                                    |
#====================================================================================
#====================================================================================
buttonR1 = ttk.Button(win, text="Robot 1",command=robot1send)#                                         |            
buttonR1.place(x=10, y=175)#                                                        |
inputtxtR1 = Text(win,height = 1,width = 20)#                                       |
inputtxtR1.place(x=100,y=175)#                                                      |    
#====================================================================================
buttonR2 = ttk.Button(win, text="Robot 2",command=robot2send)#                                         |
buttonR2.place(x=10, y=225)#                                                        |
inputtxtR2 = Text(win,height = 1,width = 20)#                                       |
inputtxtR2.place(x=100,y=225)#                                                      |
#====================================================================================
buttonR3 = ttk.Button(win, text="Robot 3",command=robot3send)#                                         |
buttonR3.place(x=10, y=275)#                                                        |
inputtxtR3 = Text(win,height = 1,width = 20)#                                       |
inputtxtR3.place(x=100,y=275)#                                                      |
#====================================================================================
#buttonSet = ttk.Button(win, text="Set")
#buttonSet.place(x=10, y=275)
#buttonSet = ttk.Button(win, text="Home")
#buttonSet.place(x=100, y=375)
buttonSet = ttk.Button(win, text="Stop",command=stop)
buttonSet.place(x=10, y=375)
#====================================================================================
#Create a Label
disp_img = Label()
Background = Label(win, text="BaseStation Refreebox MSL Rocup", font='Consolas 15')
label1 = Label(win, text="BaseStation Refreebox MSL Robocup", font='Consolas 15').place(x = 40, y = 30)
win.mainloop()