from tkinter import *

window = Tk()
window.title("Let us learn")

var = StringVar()
var2 = StringVar()

label = Label( window, padx=10,pady =10,textvariable=var, relief=RAISED )
label2 = Label( window,padx=10,pady =10,textvariable=var2, relief=RAISED )

var.set("Hey!? How are you doing?")
var2.set(" :) Happy New Year 2025!!")
label.pack()
label2.pack()


window.mainloop()