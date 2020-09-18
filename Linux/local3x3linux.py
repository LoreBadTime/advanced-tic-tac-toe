#By LoreBadTime,some import are useless(now)
import time, sys, traceback, os ,socket,random
from tkinter import *
import tkinter as tk
from itertools import permutations
global co,Vittoria,x,a,b,c,d,e,f,g,h,i,num,colorv,pl1vitt,pl2vitt,turn

#game
turn=1
pl1vitt=0
pl2vitt=0
num=1
num2=1
color='black'
colorlist = ['black','gray','silver','whitesmoke','rosybrown','firebrick','red','darksalmon','gold','darkkhaki','chartreuse','darkgreen','lightseagreen','darkcyan','navy','mediumpurple','palevioletred']
Vittoria = None
colorv= None
colorc= None
colorpl1='cyan'
colorpl2='red'
end = 0
co = 0
cont = 0
pl1 = []
pl2 = []
win = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
a = ""
b = ""
c = ""
d = ""
e = ""
f = ""
g = ""
h = ""
i = ""
#just start tk
master = Tk()
master.title("Tick tac toe")
master.configure(background='black')
master.geometry("410x200")
master.resizable(False,False)
def winck(a, b) :
        for x in a :
            for y in b :
                if x == y :
                    return True
def Flashyflash(window):
        global colorlist
        x=0
        while x != 13:
                window.configure(bg=random.choice(colorlist))
                window.update()
                time.sleep(0.3)
                x = x + 1        
def check(a,b):
        for x in a:
                if x == b:
                        return True
def btn(a,ascissa,ordinata,num):
    global color
    a = Button(master, text="",font=('arial','20'), state=ACTIVE, height = 1,width = 1,activebackground=color,background=color)
    a.configure(command=lambda :callback(a,num))
    a.grid(row=ascissa ,column=ordinata)
def tris(a,b,c,d,e,f,g,h,i):
    a = btn(a,0,0,1)
    b = btn(b,0,1,2)
    c = btn(c,0,2,3)
    d = btn(d,1,0,4)
    e = btn(e,1,1,5)
    f = btn(f,1,2,6)
    g = btn(g,2,0,7)
    h = btn(h,2,1,8)
    i = btn(i,2,2,9)
def callback(K,num):
    global cont
    global Vittoria
    global x,co,color,pl1vitt,pl2vitt,turn

    if Vittoria == True:
            cont = -2
    if check(pl1,num) == True or check(pl2,num) == True:
        K.config(command=0)

    else:
            if cont == 2 or cont == 4 or cont == 6 or cont == 8 or cont == 10:
                    K.configure(text="X", foreground=colorpl1)
                    master.update()
                    pl1.append(num)
            elif cont == 3 or cont == 5 or cont == 7 or cont == 9:
                    K.configure(text="O", foreground=colorpl2)
                    master.update()
                    pl2.append(num)
            cont = cont + 1
    pl1win = list(permutations(pl1,3))
    pl2win = list(permutations(pl2,3))
    if winck(win,pl1win) == True:
        Vittoria = True
        if co == 0:
                co = -2
                win1 = tk.Toplevel()
                win1.title("winner")
                sos = tk.Text(win1, height=3,width=25)
                sos.grid(column=3,row=0)

                if turn % 2 == 0:
                        pl1vitt=pl1vitt + 1
                        sos.insert(tk.END, "ha vinto il giocatore 1")
                else:
                        pl2vitt=pl2vitt + 1
                        sos.insert(tk.END, "ha vinto il giocatore 2")
                try:
                        Flashyflash(sos)
                except:
                        pass
                pl1box.configure(text=pl1vitt)
                pl2box.configure(text=pl2vitt)
                master.update()
                win1.destroy()      
    elif winck(win,pl2win) == True:
            Vittoria = True
            if co == 0:
                    co = -2
                    win2 = tk.Toplevel()
                    win2.title("winner")
                    sos = tk.Text(win2, height=3,width=25)
                    sos.grid(column=3,row=0)
                    print(turn)
                    if turn % 2 == 0:
                            pl2vitt=pl2vitt + 1
                            sos.insert(tk.END, "ha vinto il giocatore 2")
                    else:
                            pl1vitt=pl1vitt + 1
                            sos.insert(tk.END, "ha vinto il giocatore 1")
                    try :
                            Flashyflash(sos)
                    except:
                            pass
                    pl1box.configure(text=pl1vitt)
                    pl2box.configure(text=pl2vitt)
                    master.update() 
                    win2.destroy()
    if cont >= 10 and Vittoria == None:
            loose = tk.Toplevel()
            loose.title("loosers")
            txtloose = tk.Text(loose, height=3,width=25)
            txtloose.insert(tk.END, "ya all loosers")
            txtloose.grid(column=3,row=0)
            try :
                    Flashyflash(txtloose)
            except:
                    pass
            loose.destroy()
    
    return cont,Vittoria,co,color,pl1vitt,pl2vitt
def checkbx(a):
        global num
        global color
        global colorv
        num = num + 1
        if num % 2 == 0:
                a.config(background='black',foreground='green',activeforeground='white')
                colorv = True
        else:
                a.config(background='black',foreground='white',activeforeground='green')
                colorv = False
        master.update()
        return num,color,colorv
def checkbx2(a):
        global num2,colorc
        num2 = num2 + 1
        if num2 % 2 == 0:
                a.config(background='black',foreground='green',activeforeground='white')
                colorc = True
        else:
                a.config(background='black',foreground='white',activeforeground='green')
                colorc = False
        master.update()
        return num2,colorc
def checkbx3(a,b):
    global color,colorpl1,colorpl2,colorc,colorv
    color='black'
    colorpl1='cyan'
    colorpl2='red'
    a.config(background='black',foreground='white',activeforeground='green')
    b.config(background='black',foreground='white',activeforeground='green')
    colorc=False
    colorv=False
    master.update()
    return color,colorpl1,colorpl2,colorc,colorv
def start(l,a1,a2):
        global Vittoria,pl1vitt,pl2vitt,turn,end,co,cont,pl1,pl2,win,x,a,b,c,d,e,f,g,h,i ,color,colorv,colorc,colorpl1,colorpl2
#values reset
        Vittoria = None
        end = 0
        co = 0
        cont = 2
        pl1 = []
        pl2 = []
#adding numbers will increase games possibilities,(new tabs 4x4,5x5)(need to change also the table and winck)
        win = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
        x = ""
        a = ""
        b = ""
        c = ""
        d = ""
        e = ""
        f = ""
        g = ""
        h = ""
        i = ""
        turn = turn + 1
        if colorv == True:
                color=random.choice(colorlist)
        
        if turn % 2 == 0 :
                if colorc == None:
                        colorpl1='cyan'
                        colorpl2='red'
                elif colorc == True:
                        colorpl1=random.choice(colorlist)
                        colorpl2=random.choice(colorlist)
                        while colorpl1 == colorpl2 or colorpl1 == color or colorpl2 == color:
                                colorpl1=random.choice(colorlist)
                                colorpl2=random.choice(colorlist)
                elif colorc == False:
                        colorpl1,colorpl2 = colorpl2,colorpl1
                pl1box.configure(foreground=colorpl1,disabledforeground=colorpl1)
                pl2box.configure(foreground=colorpl2,disabledforeground=colorpl2)
        else:
                if colorc == None:
                        colorpl1='red'
                        colorpl2='cyan'
                elif colorc == True:
                        colorpl1=random.choice(colorlist)
                        colorpl2=random.choice(colorlist)
                        while colorpl1 == colorpl2 or colorpl1 == color or colorpl2 == color:
                                colorpl1=random.choice(colorlist)
                                colorpl2=random.choice(colorlist)
                elif colorc == False :
                        colorpl1,colorpl2 = colorpl2,colorpl1
                pl2box.configure(foreground=colorpl1,disabledforeground=colorpl1)
                pl1box.configure(foreground=colorpl2,disabledforeground=colorpl2)
        
        tris(a,b,c,d,e,f,g,h,i)
        l.geometry("300x169")
        Restart = Button (master,text="Restart", command= lambda :start(master,pl1box,pl2box) ,state=ACTIVE,background='black',activebackground='black',foreground='white',activeforeground='white')
        Restart.place(height=20, width=60 ,y=10, x=180)
        return color
def checkbx4(a,b):
        global pl1vitt,pl2vitt
        pl1vitt=0
        pl2vitt=0
        a.configure(text=pl1vitt)
        b.configure(text=pl2vitt)
        master.update()
        return pl1vitt,pl2vitt
checkbox3 = Button(master, text="reset colors", font=('italic','6'),foreground='white',activeforeground='white',command= lambda :checkbx3(checkbox,checkbox2) ,state=ACTIVE,activebackground='black',background='black' )
checkbox3.place(y=105, x=170)
checkbox4 = Button(master, text="reset counter", font=('italic','6'),foreground='white',activeforeground='white',command= lambda :checkbx4(pl1box,pl2box) ,state=ACTIVE,activebackground='black',background='black' )
checkbox4.place(y=130, x=170)
checktext = Button(master,text="random background",command= lambda :checkbx(checktext),font=('italic','7') ,state=ACTIVE,background="black",foreground='white',activebackground='Black',activeforeground='white')
checktext.place(y=50, x=170)
checktext2 = Button(master,text="random player color",font=('italic','7'),command= lambda :checkbx2(checktext2) ,state=ACTIVE,foreground='white',background="black",activebackground='Black',activeforeground='white')
checktext2.place(y=70, x=170)
pl1box = Button(master, text=pl1vitt,foreground='cyan',disabledforeground='cyan',state=DISABLED,activebackground='black',background='black' )
pl1box.place(height=20 ,width=20,y=144, x=13)
pl2box = Button(master, text=pl2vitt,foreground='red',disabledforeground='red',state=DISABLED,activebackground='black',background='black' )
pl2box.place(height=20 ,width=20,y=144, x=103)
start(master,pl1box,pl2box)
master.mainloop()
