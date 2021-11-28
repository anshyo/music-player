import pygame
from pygame import mixer
from tkinter import *
import os

from pygame.constants import DOUBLEBUF, DROPFILE





def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pausesong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Paused")
    mixer.music.pause()

def stopsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Stopped")
    mixer.music.stop()

def resumesong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Resuming")
    mixer.music.unpause()    

root=Tk()
root.title('Music player')

mixer.init()
songstatus=StringVar()
songstatus.set("choosing")


#playlist---------------

playlist=Listbox(root,selectmode=SINGLE,bg="Black",fg="White", width=48,font=('arial',15))
playlist.grid(columnspan=4)

os.chdir(r'musics/')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)

playbtn=Button(root,text="PLAY",command=playsong)
playbtn.config(font=('arial',20),bg="Black",fg="white",padx=16,pady=16)
playbtn.grid(row=1,column=0)

pausebtn=Button(root,text="PAUSE",command=pausesong)
pausebtn.config(font=('arial',20),bg="Black",fg="white",padx=16,pady=16)
pausebtn.grid(row=1,column=1)

stopbtn=Button(root,text="STOP",command=stopsong)
stopbtn.config(font=('arial',20),bg="Black",fg="white",padx=16,pady=16)
stopbtn.grid(row=1,column=2)

Resumebtn=Button(root,text="RESUME",command=resumesong)
Resumebtn.config(font=('arial',20),bg="Black",fg="white",padx=16,pady=16)
Resumebtn.grid(row=1,column=3)


mainloop()