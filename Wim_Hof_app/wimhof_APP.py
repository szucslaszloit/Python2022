from email.mime import image
from glob import glob
from itertools import count
from os import times
from threading import *
from tkinter import *
import time
import tkinter
import logging 
from pygame import mixer

logging.basicConfig(
                    
                    format='%(asctime)s %(levelname)s %(message)s', 
                    filename="C:\Python\Wim_Hof_App\wim_hof_times.log", 
					filemode='a') 

#Let us Create an object 
logger=logging.getLogger() 

#Now we are going to Set the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 

#logger = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s",
#                              "%Y-%m-%d %H:%M:%S")


root = Tk()
root.title('Wim Hof gyakorlat')
#root.iconbitmap('c:/gui/codemy.ico')
root.geometry("660x400")

background_image = tkinter.PhotoImage(file='c:\Python\Wim_Hof_App\wh.png')
background_label = tkinter.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

mins= StringVar()
Entry(root, textvariable = mins, width = 2, font = 'arial 30').place(x=270, y=150)
mins.set('00')
sec = StringVar()
Entry(root, textvariable = sec, width = 2, font = 'arial 30').place(x=318, y=150)
sec.set('00')

running = True
stopper = True
szamlalo = 1

def on_start():
   global running
   running = True

def on_stop():
   global running
   running = False

def on_start_stopper():
    global stopper
    stopper = True

def on_stop_stopper(): 
    global stopper
    stopper = False
  

def legzes():
    global szamlalo
    global running

    if running==True:
        while szamlalo < 30:
            my_label.config(text=f"Lélegezz BE! \n {szamlalo}")
            root.update()
            time.sleep(2)
            my_label.config(text=f"Lélegezz KI! \n {szamlalo} ") 
            root.update()
            time.sleep(1)
            szamlalo+=1 

def zene1():
        mixer.init()
        mixer.music.load('C:\Python\Wim_Hof_app\wh.mp3')
        mixer.music.play()

def elso_kor():
    if running==True:
        my_label.config(text="Kezdünk!\nElső Kör")
def masdoik_kor():
    if running==True:
        my_label.config(text="Második Kör")
def harmadik_kor():
    if running==True:
        my_label.config(text="Harmadik Kör")
def negyedik_kor():
    if running==True:
        my_label.config(text="Negyedik Kör")
def otodik_kor():
    if running==True:
        my_label.config(text="Ötödik Kör")
def be_ki():
    if running==True:
        my_label.config(text="Teljesen BE\nEngedd ki")
def ritmus():
    if running==True:
        my_label.config(text="Térj vissza a ritmusba!")
def bent_tart():
    if running==True:
        
        my_label.config(text="Mély levegő,tartsd bent 15 másodpercig!\nEngedd ki!")
def vissza_tart():
    if running==True:
        my_label.config(text="Lélegzet visszatartás!")
def vege():
    if running==True:
        my_label.config(text="Vége!")


def countdowns(minu,seco):
   global times 
   if stopper==True: 
    if running==True: 
        times = int(minu)*60 + int(seco)
        #times = int(mins.get())*60 + int(sec.get())
        while times > -1:
                
                minute,second = (times // 60 , times % 60)
                
                hour = 0
                if minute > 60:
                    hour , minute = (minute // 60 , minute % 60)
            
                sec.set(second)
                mins.set(minute)
        
                root.update()
                time.sleep(1)
                if(times == 0):
                    
                    mins.set('00')
                    sec.set('00')
                    
                times -= 1 
                print(times)

def countdowns2():
    #vissza_tart()
    global times
    if running==True: 

   # times = int(minu)*60 + int(seco)
    #times = int(mins.get())*60 + int(sec.get())
        times = 0
        while stopper==True: 
    
                
            minute,second = (times // 60 , times % 60)
                
            hour = 0
            if minute > 60:
                    hour , minute = (minute // 60 , minute % 60)
            
            sec.set(second)
            mins.set(minute)

            root.update()
            time.sleep(1)
            times += 1 
            print(times)
                #if(times == 0):
                #    
                #    mins.set('00')
                #    sec.set('00')
                    
                #times += 1 

def kezdo():
        on_start() 
        on_start_stopper()
        global szamlalo
        
        zene1()
        szamlalo = 1
        elso_kor()
        countdowns(0,3)
        legzes()
        be_ki()
        countdowns(0,2)
        vissza_tart()
        root.update()
        countdowns(0,30)
        bent_tart()
        root.update()
        countdowns(0,15)

        masdoik_kor()
        countdowns(0,3)
        ritmus()
        countdowns(0,2)
        root.update()
        szamlalo = 1
        legzes()
        be_ki()
        countdowns(0,2)
        vissza_tart()
        root.update()
        countdowns(1,00)
        bent_tart()
        root.update()
        countdowns(0,15)

        harmadik_kor()
        countdowns(0,3)
        ritmus()
        countdowns(0,2)
        root.update()
        szamlalo = 1
        legzes()
        be_ki()
        countdowns(0,2)
        vissza_tart()
        root.update()
        countdowns(1,30)
        bent_tart()
        root.update()
        countdowns(0,15)
        vege()

def kozep():
        on_start()
        on_start_stopper()
        global szamlalo
        zene1()
        szamlalo = 1
        elso_kor()
        countdowns(0,3)
        legzes()
        be_ki()
        countdowns(0,2)
        vissza_tart()
        root.update()
        countdowns(0,30)
        bent_tart()
        root.update()
        countdowns(0,15)

        masdoik_kor()
        countdowns(0,3)
        ritmus()
        countdowns(0,2)
        root.update()
        szamlalo = 1
        legzes()
        be_ki()
        countdowns(0,2)
        vissza_tart()
        root.update()
        countdowns(1,00)
        bent_tart()
        root.update()
        countdowns(0,15)

        harmadik_kor()
        countdowns(0,3)
        ritmus()
        countdowns(0,2)
        root.update()
        szamlalo = 1
        legzes()
        be_ki()
        countdowns(0,2)
        vissza_tart()
        root.update()
        countdowns(1,30)
        bent_tart()
        root.update()
        countdowns(0,15)

        negyedik_kor()
        countdowns(0,3)
        ritmus()
        countdowns(0,2)
        root.update()
        szamlalo = 1
        legzes()
        be_ki()
        countdowns(0,2)
        vissza_tart()
        root.update()
        countdowns(2,00)
        bent_tart()
        root.update()
        countdowns(0,15)
        vege()

def halado():
        on_start()
        on_start_stopper()
        global szamlalo
        zene1()
        szamlalo = 1
        elso_kor()
        countdowns(0,3)
        legzes()
        be_ki()
        countdowns(0,2)
        vissza_tart()
        root.update()
        countdowns(0,30)
        bent_tart()
        root.update()
        countdowns(0,15)

        masdoik_kor()
        countdowns(0,3)
        ritmus()
        countdowns(0,2)
        root.update()
        szamlalo = 1
        legzes()
        be_ki()
        countdowns(0,2)
        vissza_tart()
        root.update()
        countdowns(1,00)
        bent_tart()
        root.update()
        countdowns(0,15)

        harmadik_kor()
        countdowns(0,3)
        ritmus()
        countdowns(0,2)
        root.update()
        szamlalo = 1
        legzes()
        be_ki()
        countdowns(0,2)
        vissza_tart()
        root.update()
        countdowns(1,30)
        bent_tart()
        root.update()
        countdowns(0,15)

        negyedik_kor()
        countdowns(0,3)
        ritmus()
        countdowns(0,2)
        root.update()
        szamlalo = 1
        legzes()
        be_ki()
        countdowns(0,2)
        vissza_tart()
        root.update()
        countdowns(2,00)
        bent_tart()
        root.update()
        countdowns(0,15)

        otodik_kor()
        countdowns(0,3)
        ritmus()
        countdowns(0,2)
        root.update()
        szamlalo = 1
        legzes()
        be_ki()
        countdowns(0,2)
        vissza_tart()
        root.update()
        countdowns(2,00)
        bent_tart()
        root.update()
        countdowns(0,15)
        
        vege()

def custom():
        on_start() 
        on_start_stopper()
        global szamlalo
    
        zene1()
        szamlalo = 1
        elso_kor()
        countdowns(0,3)
        legzes()
        be_ki()
        countdowns(0,2)
        vissza_tart()
        root.update()
        countdowns2()
        bent_tart()
        root.update()
        on_start_stopper()
        countdowns(0,15)

        
        masdoik_kor()
        countdowns(0,3)
        ritmus()
        countdowns(0,2)
        root.update()
        szamlalo = 1
        legzes()
        be_ki()
        countdowns(0,2)
        vissza_tart()
        root.update()
        countdowns2()
        bent_tart()
        root.update()
        on_start_stopper()
        countdowns(0,15)

        harmadik_kor()
        countdowns(0,3)
        ritmus()
        countdowns(0,2)
        root.update()
        szamlalo = 1
        legzes()
        be_ki()
        countdowns(0,2)
        vissza_tart()
        root.update()
        countdowns2()
        bent_tart()
        root.update()
        on_start_stopper()
        countdowns(0,15)

        vege()

def stoplegzes():
    global stopper
    global szamlalo
    szamlalo = 30
    global times
    time_log = times
    logger.info(time_log)
    times = -10
    on_stop_stopper()
    mins.set('00')
    sec.set('00')
    

def stopprogram():
         
    global times
    global running
    global szamlalo
    szamlalo = 30
    running = False
    times = -10
    on_stop()
    on_stop_stopper()
    mixer.init()
    mixer.music.pause()
    mins.set('aa')
    sec.set('aa')
    my_label.config(text="STOP")
   


root.wm_attributes('-transparentcolor', '#ab23ff')
my_label = Label(root,text="", font=("Hevletica",22),fg="black")#,bg='#ab23ff')
my_label.pack(pady=30)

Button(root, text='KEZDŐ LÉGZÉSGYAKORLAT', bd ='5', command =  kezdo, bg = 'antique white', font = 'arial 10 bold').place(x=0, y=280)
Button(root, text='KÖZÉPHALADÓ LÉGZÉSGYAKORLAT', bd ='5', command =  kozep, bg = 'antique white', font = 'arial 10 bold').place(x=200, y=280)
Button(root, text='HALADÓ LÉGZÉSGYAKORLAT', bd ='5', command =  halado, bg = 'antique white', font = 'arial 10 bold').place(x=455, y=280)
Button(root, text='CUSTOM LÉGZÉSGYAKORLAT', bd ='5', command = custom , bg = 'antique white', font = 'arial 10 bold').place(x=100, y=330)
Button(root, text='LÉGZÉSGYAKROLAT STOP', bd ='5', command = stopprogram, bg = 'antique white', font = 'arial 10 bold').place(x=215, y=365)
Button(root, text='LÉGZÉS VISSZATART STOP', bd ='5', command = stoplegzes, bg = 'antique white', font = 'arial 10 bold').place(x=310, y=330)


root.mainloop()
