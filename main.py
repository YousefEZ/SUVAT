from tkinter import *
from tkinter import messagebox
from suvat import *

def Tracer(*args):
    global Start
    global Unknowns
    Values = [S.get(), U.get(), V.get(), A.get(), T.get()]
    Passes = 0 
    Unknowns = 5
    Start = True
    for i in range(len(Values)):
        if Values[i] != "?":
            Unknowns -= 1
            try:
                float(Values[i])
            except ValueError:
                Start = False
            else:
                Passes += 1

def Solve(*args):
    global Start
    global Unknowns
    Tracer()
    if Unknowns > 2:
        pass
    elif Start == False:
        pass
    else:
        s = S.get()
        u = U.get()
        v = V.get()
        a = A.get()
        t = T.get()
        suvat(s,u,v,a,t)
        S.set(s)
        U.set(u)
        V.set(v)
        A.set(a)
        T.set(t)



window1 = Tk()
window1.title('Yousef Zaher / SyberProjects - SUVAT Calculator')

S = StringVar()
U = StringVar()
V = StringVar()
A = StringVar()
T = StringVar()

Displacement_Label = Label(window1,text = "Displacement").grid(row = 1,column = 1)
IVelocity_Label = _Label = Label(window1, text = "Initial Velocity").grid(row = 2,column = 1)
UVelocity_Label = Label(window1, text = "Final Velocity").grid(row = 3,column = 1)
Acceleration_Label = Label(window1, text = "Acceleration").grid(row = 4,column = 1)
Time_Label = Label(window1, text = "Time").grid(row = 5,column = 1)

Displacement_Entry = Entry(window1, textvariable = S).grid(row = 1, column = 2)
IVelocity_Entry = Entry(window1, textvariable = U).grid(row = 2, column = 2)
FVelocity_Entry = Entry(window1, textvariable = V).grid(row = 3, column = 2)
Acceleration_Entry = Entry(window1, textvariable = A).grid(row = 4, column = 2)
Time_Entry = Entry(window1, textvariable = T).grid(row = 5, column = 2)

SignDisplacement_Label = Label(window1,text = "m").grid(row = 1,column = 3)
SignIVelocity_Label = _Label = Label(window1, text = "ms^-1").grid(row = 2,column = 3)
SignUVelocity_Label = Label(window1, text = "ms^-1").grid(row = 3,column = 3)
SignAcceleration_Label = Label(window1, text = "ms^-2").grid(row = 4,column = 3)
SignTime_Label = Label(window1, text = "s").grid(row = 5,column = 3)

Solve = Button(window1, text = "Solve", command = Solve).grid(row = 6, column = 2)

S.trace("w",Tracer)
U.trace("w",Tracer)
V.trace("w",Tracer)
A.trace("w",Tracer)
T.trace("w",Tracer)

window1.mainloop()
