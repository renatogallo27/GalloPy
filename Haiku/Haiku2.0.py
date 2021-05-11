import random
from guizero import *

def genera_haiku():
    f=open('HaikuUno.txt') 
    f2=open('HaikuDue.txt')
    f3=open('HaikuTre.txt')
    haiku1=random.choice(f.readlines())
    haiku2=random.choice(f2.readlines())
    haiku3=random.choice(f3.readlines())
    #testo1=Text(app, text=haiku1)
    #testo2=Text(app, text=haiku2)
    #testo3=Text(app, text=haiku3)
    listbox= ListBox(app, width=125, height=55, items=[haiku1, haiku2, haiku3])
                                                           
app=App(title="Generatore di Haiku")
intro=Text(app, text="Benvenuto su Generatore di Haiku!")
bottone=PushButton(app, text="Genera Haiku", command=genera_haiku)
app.display()
