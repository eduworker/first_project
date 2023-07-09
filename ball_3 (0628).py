import tkinter as t

balls = [{"x" : 400, "y" : 200, "dx" : 1, "dy" : 1, "color" : "red"}, 
         {"x" : 200, "y" : 100, "dx" : -1, "dy" : 1, "color" : "green"},
         {"x" : 100, "y" : 200, "dx" : 1, "dy" : -1, "color" : "blue"}]

def move() :
    global balls

    for b in balls :
        canvas.create_oval(b["x"]-20, b["y"]-20, b["x"]+20, b["y"]+20, fill="white", width="0")
        b["x"]+=b["dx"]
        b["y"]+=b["dy"]
        canvas.create_oval(b["x"]-20, b["y"]-20, b["x"]+20, b["y"]+20, fill=b["color"], width="0")
        if (b["x"]>=canvas.winfo_width()-20) :
            b["dx"] = -1
        if b["x"]<= 20 :
            b["dx"] = 1
        if b["y"] >= canvas.winfo_height()-20 :
            b["dy"] = -1
        if b["y"] <= 20 :
            b["dy"] = 1
    root.after(5, move)

root=t.Tk()
root.geometry("600x400")

canvas=t.Canvas(root, width=600, height=400, bg = "white")
canvas.place(x=0, y=0)

root.after(10, move)

root.mainloop()