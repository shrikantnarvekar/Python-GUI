from tkinter import *
def menu1():
    c.delete("all")
    c.create_rectangle(200,25,800,150,fill="Blue")
def menu4():
    c.delete("all")
    c.create_rectangle(200,25,700,150,fill="Red")
def menu2():
    c.delete("all")
    c.create_line(200,100,75,600)
def menu5():
    c.delete("all")
    c.create_line(200,100,75,600,fill="Purple",dash=(5,5))
def menu3():
    c.delete("all")
    c.create_oval(300,100,500,300,fill="White")
def menu6():
    c.delete("all")
    c.create_oval(300,100,500,300,fill="Grey")
root=Tk()
c=Canvas(root,width=1000,height=650)
c.pack()

menubar=Menu(root)
filename1=Menu(menubar)
filename2=Menu(menubar)
filename3=Menu(menubar)

filename1.add_command(label="Blue-Rectangle",command=menu1)
filename1.add_command(label="Red-Rectangle",command=menu4)
filename2.add_command(label="Plane-Line",command=menu2)
filename2.add_command(label="Dash-Line",command=menu5)
filename3.add_command(label="plane-Circle",command=menu3)
filename3.add_command(label="Grey-Circle",command=menu6)

menubar.add_cascade(label="Rectangle",menu=filename1)
menubar.add_cascade(label="line",menu=filename2)
menubar.add_cascade(label="Circle",menu=filename3)

root.config(menu=menubar)
root.mainloop()
