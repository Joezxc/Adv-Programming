from tkinter import *
root = Tk()
root.title("Widget example")

mylabel= Label(root, text="I am a label widget")
mylabel.pack()
mybutton = Button(root, text="I am a button")
mybutton.pack()

root.geometry('350x600')
root.resizable(0,0)
root.mainloop()

