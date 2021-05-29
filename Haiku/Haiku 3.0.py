import random
from guizero import *

def genera_haiku():
    f=open('HaikuUno.txt') 
    f2=open('HaikuDue.txt')
    f3=open('HaikuTre.txt')
    haiku1=random.choice(f.readlines())
    haiku2=random.choice(f2.readlines())
    haiku3=random.choice(f3.readlines())
    listbox= ListBox(app, width=125, height=55, items=[haiku1, haiku2, haiku3])
    listbox.bg="white"
    listbox.font="Arial"
    listbox.text_size="10"
    text_box = TextBox(app, text="", width="fill", height="1")

app=App(title="Un haiku al giorno", bg = "#222255")
intro_box = Box(app, width="fill", align="top", border=True)
intro=Text(intro_box, text="Benvenuto nel Generatore di Haiku!", font='Arial', size='16', color='white')
bottone=PushButton(app, text="Genera Haiku", command=genera_haiku)
bottone.bg="white"
bottone.text_size="12"
bottone.font="Arial"
text_box = TextBox(app, text="", width="fill")
app.display()
