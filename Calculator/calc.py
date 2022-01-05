from tkinter import *

root=Tk()
root.title("Simple Calculator")
f_num =int()
a=Entry(root, width=35, borderwidth=5)
a.grid(row=0, column =0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = a.get()
    a.delete(0,END)
    a.insert(0, str(current) + str(number))

def button_clear():
    a.delete(0,END)

def button_add():
    first_number = a.get()
    global f_num
    f_num = int(first_number)
    

def button_equal():
    second_number = a.get()
    a.delete(0,END)
    a.insert(0, f_num + int(second_number))


b=Button(root, text="1", padx=40, pady=20, command=lambda : button_click(1))
c=Button(root, text="2", padx=40, pady=20, command=lambda : button_click(2))
d=Button(root, text="3", padx=40, pady=20, command=lambda : button_click(3))
e=Button(root, text="4", padx=40, pady=20, command=lambda : button_click(4))
f=Button(root, text="5", padx=40, pady=20, command=lambda : button_click(5))
g=Button(root, text="6", padx=40, pady=20, command=lambda : button_click(6))
h=Button(root, text="7", padx=40, pady=20, command=lambda : button_click(7))
i=Button(root, text="8", padx=40, pady=20, command=lambda : button_click(8))
j=Button(root, text="9", padx=40, pady=20, command=lambda : button_click(9))
k=Button(root, text="0", padx=40, pady=20, command=lambda : button_click(0))
add=Button(root, text="+", padx=39, pady=20,command=button_add)
equal=Button(root, text="=", padx=91, pady=20, command=button_equal)
clear=Button(root, text="AC", padx=79, pady=20, command=button_clear)
b.grid(row=3,column=0)
c.grid(row=3,column=1)
d.grid(row=3,column=2)
e.grid(row=2,column=0)
f.grid(row=2,column=1)
g.grid(row=2,column=2)
h.grid(row=1,column=0)
i.grid(row=1,column=1)
j.grid(row=1,column=2)
k.grid(row=4,column=0)
clear.grid(row=4,column=1,columnspan=2)
add.grid(row=5,column=0)
equal.grid(row=5,column=1,columnspan=2)

root.mainloop()