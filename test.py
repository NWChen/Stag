from tkinter import *
import random
 
root = Tk()
w = Canvas(root, width=400, height=300, background="#000000")
w.create_text(200,150,text="Happy Christmas 2006",font="Arial 20",fill="#ff0000")
w.create_text(200,170,text="from kudos",font="Arial 12",fill="#00ff00")
w.pack()
 
flake = [];
moves = []
for i in range(50):
 flake.append(w.create_text(random.randrange(400),random.randrange(300),text="*",fill="#ffffff",font="Times 30"))
 moves.append([0.04 + random.random()/10,0.7 + random.random()])
try:
 while 1:
  for i in range(len(flake)):
   p = w.coords(flake[i])
   p[0]+=moves[i][0]
   p[1]+=moves[i][1]
   w.coords(flake[i],p[0],p[1])
   if(p[1]>310):
    w.coords(flake[i],random.randrange(400),-10)
   root.update_idletasks() # redraw
   root.update() # process events
except:
 pass
 