'''
import tkinter as t

root=t.Tk()
root.geometry("600x400")

canvas=t.Canvas(root, width=600, height=400, bg = "white")
canvas.place(x=0, y=0)

canvas.create_oval(300-20, 200-20, 300+20, 200+20, fill="blue", width="3", outline="black")
root.mainloop()


x=300
y=200

def click(event) :
    global x, y
    canvas.create_oval(x-20, y-20, x+20, y+20, fill="white", width="0")
    x =event.x
    y= event.y
    canvas.create_oval(x-20, y-20, x+20, y+20, fill="green", width="0")

root=t.Tk()
root.geometry("600x400")

canvas=t.Canvas(root, width=600, height=400, bg = "blue")
canvas.place(x=0, y=0)

canvas.bind("<Button-1>",click)

root.mainloop()
'''

import tkinter as t

class ball : 
    def __init__(self, x, y, dx, dy, color) :
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color

    def move(self, canvas) :
        canvas.create_oval(self.x-20, self.y-20, self.x+20, self.y+20, fill="white", width="0")
        self.x+=self.dx
        self.y+=self.dy
        canvas.create_oval(self.x-20, self.y-20, self.x+20, self.y+20, fill=self.color, width="0")
        if (self.x>=canvas.winfo_width()-20) :
            self.dx = -1
        if self.x<= 20 :
            self.dx = 1
        if self.y >= canvas.winfo_height()-20 :
            self.dy = -1
        if self.y <= 20 :
            self.dy = 1

balls =[ball(200, 200, 1, 1, "red"),
        ball(200, 200, -1, -1, "blue"),
        ball(200, 200, 1, -1, "black"),
        ball(200, 200, -1, 1, "green")]

def loop() :
    for b in balls :
        b.move(canvas)
    root.after(10,loop)

root=t.Tk()
root.geometry("600x400")

canvas=t.Canvas(root, width=600, height=400, bg = "white")
canvas.place(x=0, y=0)

root.after(5,loop)

root.mainloop()
