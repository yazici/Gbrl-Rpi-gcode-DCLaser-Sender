import Gbrl_Rpi_gcode_DcLaser_Sender


from tkinter import *


def getFile():
    print(gcodeSender.getFileInfo())
    
def Framedisable():


root = Tk()
root.geometry("800x480+100+100")

gcodeSender = Gbrl_Rpi_gcode_DcLaser_Sender.LaserCom()

Userinfo = Frame(root, relief=RIDGE, width=700, height=120, bg="blue")
Userinfo.place(y=0,x=100)

NavC = Frame(root, relief=SUNKEN, width=100, bg="red", height=480)
NavC.place(y=0,x=0)
open = Button(NavC, text="Open",command = getFile)
open.place(y=0, x=10)
Ncsend = Button(NavC, text="Send", relief=RAISED, bg="blue")
Ncsend.place(y=10, x=20)
Ncstart = Button(Userinfo, text="Start", relief=SUNKEN, fg="black")
Ncstart.place(y=20, x=30)
Exit = Button(NavC, fg="green", bg="black",text="Exit", command=root.destroy)
Exit.place(y=50, x=10)
Send = Frame(root,width=700, bg="yellow", height=360)
Send.place(y=120, x=100)
#Exit.place(height=20, width=40, x=800, y=480)

root.mainloop()
