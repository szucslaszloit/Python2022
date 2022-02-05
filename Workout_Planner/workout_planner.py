from cgi import test
from glob import glob
import tkinter as tk
from tkinter  import font
import random
import logging 

#now we will Create and configure logger 

logging.basicConfig(filename="C:\Python\Workout_Planner\workout_plan.log", 
					format='%(asctime)s %(message)s', 
					filemode='a') 

#Let us Create an object 
logger=logging.getLogger() 

#Now we are going to Set the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 
#some messages to test
#logger.debug("This is just a harmless debug message") 
##logger.info("This is just an information for you") 
#logger.warning("OOPS!!!Its a Warning") 
#logger.error("Have you try to divide a number by zero") 
#logger.critical("The Internet is not working....") 

HEIGHT = 600
WIDTH = 800

def ss_function():
     global eo
     label['text'] = "Egyszerű, és ördögi"
     eo = label['text']
def cp_function():
     global cp
     label['text'] = "Clean & Press létra"
     cp = label['text']   
def kettlebell_function():
        global kettlebell_log 
        edzes = random.randint(1, 2)    
        if edzes == 1:
            gyakorlatok = ["Lendítések, és fekvőtámaszok", "Szakítások"]
            gyakorlat = random.choice(gyakorlatok)
            
            volumen =  random.randint(1, 6)
            if volumen == 1:
                mennyiseg = ("Sorozatok: 2" + " " + "Ismétlés: 40" + " " + "Időtartam: 12 perc")
            elif volumen == 2:
                mennyiseg = ("Sorozatok: 3" + " " + "Ismétlés: 60" + " " + "Időtartam: 18 perc")
            elif volumen == 3:
                mennyiseg = ("Sorozatok: 3" + " " + "Ismétlés: 60" + " " + "Időtartam: 18 perc")
            elif volumen == 4:  
                mennyiseg = ("Sorozatok: 4" + " " + "Ismétlés: 80" + " " + "Időtartam: 24 perc")
            elif volumen == 5:  
                mennyiseg = ("Sorozatok: 4" + " " + "Ismétlés: 80" + " " + "Időtartam: 24 perc")
            elif volumen == 6:  
                mennyiseg = ("Sorozatok: 5" + " " + "Ismétlés: 100" + " " + "Időtartam: 30 perc")

            tipus =  random.randint(1, 6)
            
            if tipus == 1:
                tip = ("Ismétlés tipusa: 5/4")
            elif tipus == 2:
                tip = ("Ismétlés tipusa: 5/4")
            elif tipus == 3:  
                tip = ("Ismétlés tipusa: 5/4 -et váltogasd a 10/2 -vel")
            elif tipus == 4:  
                tip = ("Ismétlés tipusa: 5/4 -et váltogasd a 10/2 -vel")
            elif tipus == 5:  
                tip = ("Ismétlés tipusa: 10/2")
            elif tipus == 6:  
                tip = ("Ismétlés tipusa: 10/2") 

            gyakorlat2 = "Szakítások"
            if gyakorlat == gyakorlat2:
                swing = ("")
            if gyakorlat != gyakorlat2:
                lendites =  random.randint(1, 6)
                if lendites == 1:
                    swing = ("Lendítés tipusa: Kétkezes")
                elif lendites == 2:
                    swing = ("Lendítés tipusa: Kétkezes")
                elif lendites == 3:  
                    swing = ("Lendítés tipusa: Kétkezes")
                elif lendites == 4:  
                    swing = ("Lendítés tipusa: Egykezes")
                elif lendites == 5:  
                    swing = ("Lendítés tipusa: Egykezes")
                elif lendites == 6:  
                    swing = ("Lendítés tipusa: Egykezes")
        

            label['text'] = "Lesz edzés" + "\n" +"\n"+str(gyakorlat)   +"\n" +"\n"+ mennyiseg  +"\n" +"\n"+ tip +"\n" +"\n"+ swing
            kettlebell_log = label['text']
           
        else:
            label['text'] = "Nem lesz edzés"
            kettlebell_log = label['text']

def testepito_function():
    global teste
    testepito = random.randint(1, 6)  
      
    if testepito == 1:
        label['text'] = "Mell - Has"
        mell = random.randint(1, 3)
        if mell == 1:
            label['text'] = "Mell első fázis:" + "\n" +"\n" "Fekvenyomás 4-5 széria Ismétlés: 6-8" + "\n" +"\n" + "Fekvenyomás döntött: 4-5 széria Ismétlés: 6-8" + "\n" +"\n" + "Tárogatás 3-4 széria Ismétlés 12-15"
            teste = label['text']        
        elif mell ==2:
            label['text'] = "Mell második fázis:" + "\n" +"\n" "Fekvenyomás 5 széria Ismétlés: 6-8" + "\n" +"\n" + "Fekvenyomás döntött: 4-5 széria Ismétlés: 6-8" + "\n" +"\n" + "Tárogatás 3-4 széria Ismétlés 12-15" + "\n" +"\n" + "Tolózkodás 3 széria Ismétlés 15"
            teste = label['text'] 
        elif mell ==3:
            label['text'] = "Mell harmadik fázis:" + "\n" +"\n" "Fekvenyomás 4-5 széria Ismétlés: 6-8" + "\n" +"\n" + "Fekvenyomás egykezes: 3-4 széria Ismétlés: 10-12" + "\n" +"\n" + "Fekvenyomás döntött: 3 széria Ismétlés: 6-8"+ "\n" +"\n" + "Fekvenyomás döntött egykezes: 2-3 széria Ismétlés: 10-12" + "\n" +"\n" + "Tárogatás 3-4 széria Ismétlés 12-15" + "\n" +"\n" + "Tolózkodás 3 széria Ismétlés 15"
            teste = label['text'] 
    elif testepito ==2:
        vall = random.randint(1, 3)
        if vall == 1:
            label['text'] = "Váll első fázis:" + "\n" +"\n" "Vállról, vagy nyakból nyomás 5 széria Ismétlés: 6-8" + "\n" +"\n" + "Oldalemelés: 4 széria Ismétlés: 10-12" + "\n" +"\n" + "Fordított felhúzás 3 széria Ismétlés 8-10"
            teste = label['text'] 
        elif vall ==2:
            label['text'] = "Váll második fázis:" + "\n" +"\n" "Nyak mögül nyomás 5 széria Ismétlés: 6-8" + "\n" +"\n" + "Vállról nyomás 4 széria Ismétlés: 6-8" + "\n" +"\n" + "Oldalemelés: 4 széria Ismétlés: 10-12"+ "\n" +"\n" + "Döntött oldalemelés: 4 széria Ismétlés: 10-12"+ "\n" +"\n" + "Állig húzás: 3-4 széria Ismétlés: 12-15"+ "\n" +"\n" + "Fordított felhúzás 3 széria Ismétlés 8-10"
            teste = label['text'] 
        elif vall ==3:
            label['text'] = "Váll harmadik fázis:" + "\n" +"\n" "Vállról, vagy nyak mögül nyomás 3-4 széria Ismétlés: 10-12" + "\n" +"\n" + "Oldalemelés: 3 széria Ismétlés: 12-15" + "\n" +"\n" + "Döntött oldalemelés: 3 széria Ismétlés: 12-15" "\n" +"\n" + "Fordított felhúzás 4 széria Ismétlés 8-10"
            teste = label['text'] 
    elif testepito ==3:
        bicepsz = random.randint(1, 3)
        if bicepsz == 1:
            label['text'] = "Bicpesz első fázis:" + "\n" +"\n" "Hajlítás rúddal: 4 széria 6-8 ismétlés" + "\n" +"\n" + "Hajlítás Scott padon: 4 széria 12-15 ismétlés" + "\n" +"\n" + "Koncentrált bicpesz: 3 széria 8-10 ismétlés"
            teste = label['text'] 
        elif bicepsz ==2:
            label['text'] = "Bicpesz második fázis:" + "\n" +"\n" "Hajlítás rúddal: 5 széria 6-8 ismétlés" + "\n" +"\n" + "Hajlítás Scott padon: 4 széria 12 ismétlés" + "\n" +"\n" + "Koncentrált bicpesz: 3 széria 12-15 ismétlés"  + "\n" +"\n" + "Karhajlítás dönött padon 3 széria 10-12 ismétlés"
            teste = label['text'] 
        elif bicepsz ==3:
            label['text'] = "Bicpesz harmadik fázis:" +  "\n" +"\n" "Óriásszett, 1 perc pihenővel" + "\n" +"\n" "Hajlítás rúddal: 4-5 széria 6-8 ismétlés" + "\n" +"\n" + "Hajlítás Scott padon: 4 széria 10-12 ismétlés" + "\n" +"\n" + "Koncentrált bicpesz: 4-5 széria 10-12 ismétlés"
            teste = label['text'] 
    elif testepito ==4:
        tricpesz = random.randint(1, 3)
        if tricpesz == 1:
            label['text'] = "Tricepsz első fázis:" + "\n" +"\n" "Tricpesz lenyomás 5 széria 10-15 ismétlés" + "\n" +"\n" + "Fekvő tricpesz: 4 széria Ismétlés: 8-10"
            teste = label['text'] 
        elif tricpesz ==2:
            label['text'] = "Tricpesz második fázis:" + "\n" +"\n" "Tricpesz lenyomás 5 széria 10-15 ismétlés" + "\n" +"\n" + "Fekvő tricpesz: 4 széria Ismétlés: 8-10" + "\n" +"\n" + "Egykezes koncentrált tricepsz 3-4 széria Ismétlés 12-15"
            teste = label['text'] 
        elif tricpesz ==3:
            label['text'] = "Tricpesz harmadik fázis:" + "\n" +"\n" "Tricpesz lenyomás 5 széria 10-15 ismétlés" + "\n" +"\n" + "Fekvő tricpesz: 4 széria Ismétlés: 8-10" + "\n" +"\n" + "Álló tricpeszgyakolat kötéllel 4-5 széria Ismétlés 12-15"+ "\n" +"\n" + "Egykezes tricpesz fordított fogás  3 széria Ismétlés 12-15"
            teste = label['text'] 
    elif testepito ==5:
        hat = random.randint(1, 3)
        if hat == 1:
            label['text'] = "Hát első fázis:" + "\n" +"\n" "Lehúzás széles fogással 5 széria Ismétlés 10-12" + "\n" +"\n" + "Evezés döntött törzzsel 4 széria Ismétlés: 6-8" 
            teste = label['text'] 
        elif hat ==2:
            label['text'] = "Hát második fázis:" + "\n" +"\n" "Lehúzás széles fogással 5 széria Ismétlés 10-12" + "\n" +"\n" + "Evezés döntött törzzsel 4 széria Ismétlés: 6-8" + "\n" +"\n" + "Egykezes lehúzás csingán 4 széria Ismétlés 12-15"
            teste = label['text'] 
        elif hat ==3:
            label['text'] = "Hát harmadik fázis:" + "\n" +"\n" "Lehúzás széles fogással 5 széria Ismétlés 10-12" + "\n" +"\n" + "Húzózkodás 4 x max" + "\n" +"\n" + "Evezés T rúddal 4 széria Ismétlés: 6-8 " + "\n" +"\n" + "Egykezes lehúzás csingán 4 széria Ismétlés 12-15" + "\n" +"\n" + "Döntött törzsű evezés 4 széria Ismétlés 6-8"+ "\n" +"\n" + "Lehúzás szűk fogással 2-3 széria Ismétlés 10-12"
            teste = label['text'] 
    elif testepito ==6:
        lab = random.randint(1, 3)
        if lab == 1:
            label['text'] = "Láb első fázis:" + "\n" +"\n" "Bolgár guggolás 4-5 széria Ismétlés: 12-15" + "\n" +"\n" + "Guggolás: 4-5 széria Ismétlés: 8-10" + "\n" +"\n" + "Merevlábas felhúzás 3-5 széria Ismétlés 8-10"
            teste = label['text'] 
        elif lab ==2:
            label['text'] = "Láb második fázis:" + "\n" +"\n" "Hacksquat kettlebellel 4-5 széria Ismétlés: 12-15" + "\n" +"\n" + "Guggolás: 4-5 széria Ismétlés: 8-10" + "\n" +"\n" + "Merevlábas felhúzás 3-5 széria Ismétlés 8-10"
            teste = label['text'] 
        elif lab ==3:
            label['text'] = "Láb harmadik fázis:" + "\n" +"\n" "Bolgár guggolás 4-5 széria Ismétlés: 10-12" + "\n" +"\n" +"Hacksquat 4 széria Ismétlés: 12-15" + "\n" +"\n" + "Guggolás: 4-5 széria Ismétlés: 8-10" + "\n" +"\n" + "Merevlábas felhúzás 3-5 széria Ismétlés 8-10"
            teste = label['text'] 

root = tk.Tk()
root.title("Workout planner")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='c:\Python\Workout_planner\siluette2.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')


def edzo_sorsolas():
    
    global kettlebell_log
    global teste
    global eo
    global cp

    sorsolo_gomb1 = random.randint(1, 6) 
    if sorsolo_gomb1 == 1:
        kettlebell_function()
        logger.info(kettlebell_log)
    elif sorsolo_gomb1 ==2:
        kettlebell_function()
        logger.info(kettlebell_log)
    elif sorsolo_gomb1 == 3:
        testepito_function()
        logger.info(teste)
    elif sorsolo_gomb1 == 4:
        testepito_function()
        logger.info(teste)
    elif sorsolo_gomb1 == 5:
        ss_function()
        logger.info(eo)
    elif sorsolo_gomb1 == 6:
        cp_function()
        logger.info(cp)

button = tk.Button(frame, text="Mutasd az edzést", bg='gray', fg='white',font=40, command=lambda: edzo_sorsolas())
button.pack(side='left',fill='x', expand=True)
lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
label = tk.Label(lower_frame, font=('Courier', 11))
label.place(relwidth=1, relheight=1)
root.mainloop()
