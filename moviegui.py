from tkinter import *
def show():
    s=list1.curselection()
    if 0 in s:
        text.insert(INSERT, "\n1 pm:Kabil\n5 pm:Dangal")
    elif 1 in s:
        text.delete('1.0', END)
        text.insert(INSERT, "\n1 pm:Raees\n5 pm:Dangal")
       # text.delete("\n1 pm:Raees\n5 pm:Dangal",END)
    elif 2 in s:
        text.delete('1.0', END)
        text.insert(INSERT, "\n1 pm:Dangal\n5 pm:Raees")
window=Tk()
l1=Label(window,text="Welcome to Big Cinemas")
l1.grid(row=0,column=1,rowspan=1,columnspan=2)
l2=Label(window,text="Select a theatre: ")
l2.grid(row=1,column=1)
list1=Listbox(window,selectmode=SINGLE,width=12,height=5)
list1.insert(1,"Big K")
list1.insert(2,"Big Imax")
list1.insert(3,"Big mulund")
list1.grid(row=2,column=1)
text=Text(width=15,height=5)
text.grid(row=2,column=2)
button=Button(window,text="show",command=show)
button.grid(row=2,column=3)
window.mainloop()
