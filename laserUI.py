import tkinter
from tkinter.constants import *
tk = tkinter.Tk()
Main = tkinter.Frame(tk, relief=RIDGE, width=800, height=480)
Main.pack()


Exit = tkinter.Button(tk, text="Exit", command=tk.destroy)
Exit.pack(side=BOTTOM)
tk.mainloop()
