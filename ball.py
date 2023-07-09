import tkinter as t
'''
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

x=400
y=200
dx=10

def move() :
    global x, y, dx
    canvas.create_oval(x-20, y-20, x+20, y+20, fill="white", width="0")
    x+=dx
    canvas.create_oval(x-20, y-20, x+20, y+20, fill="blue", width="0")
    if (x>=canvas.winfo_width()-20) :
        dx = -10
    if x<= 20 :
        dx = 10
    root.after(5, move)

root=t.Tk()
root.geometry("600x400")

canvas=t.Canvas(root, width=600, height=400, bg = "white")
canvas.place(x=0, y=0)

root.after(10, move)

root.mainloop()