#By LoreBadTime,some import are useless(now)
#a little precisation,buttons here are unique,they are only a UI thing,the main process is stored in the callback
import time,random
from numpy.random import randint
from tkinter import *
import tkinter as tk
from itertools import permutations
global restart,co,Vittoria,num,colorv,pl1vitt,pl2vitt,turn,player1,player2,menureturn,turner
#game
turner = 0
player1=None
player2=None
turn=1
pl1vitt=0
pl2vitt=0
num=1
num2=1
color=None
colorlist = ['gray','silver','whitesmoke','rosybrown','firebrick','red','darksalmon','gold','chartreuse','darkgreen','lightseagreen','darkcyan','navy','mediumpurple','palevioletred']
Vittoria = None
colorv= None
colorc= None
colorpl1=None
colorpl2=None
end = 0
co = 0
cont = 2
pl1 = []
pl2 = []
win = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
def vsAI():
    global menureturn,master,pl1box,pl2box,Restart
    menureturn = False
    #just start tk
    master = Tk()
    master.title("Vs AI-easy")
    master.configure(background='black')
    master.geometry("280x200")
    master.resizable(False,False)
    Restart = Button (master,text="Restart", command= lambda :start(master,pl1box,pl2box) ,state=ACTIVE,background='black',activebackground='black',foreground='white',activeforeground='white')
    Restart.place(height=20, width=50 ,y=15, x=200)#the restart button
    #win counters
    pl1box = Button(master, text=pl1vitt,foreground='cyan',disabledforeground='cyan',state=DISABLED,activebackground='black',background='black' )
    pl1box.place(height=30 ,width=30,y=169, x=15)
    pl2box = Button(master, text=pl2vitt,foreground='red',disabledforeground='red',state=DISABLED,activebackground='black',background='black' )
    pl2box.place(height=30 ,width=30,y=169, x=130)
    #spaghetti code launch
    # count turn and configure the button text

    def gameplay(K,num):
        global cont,pl1,pl2,a,b,c,d,e,f,g,h,i,x
        pl1.append(num)
        AI = randint(1, 10, 1)
        while(check(pl1,AI) == True or check(pl2,AI) == True) and cont < 8:
            if cont > 8:
                break
            AI = randint(1, 10, 1)          
        pl2.append(AI)
        cont += 2
        for y in pl1:
            if y == 1:
                a.configure(text="X", foreground=colorpl1)
            elif y == 2:
                b.configure(text="X", foreground=colorpl1)
            elif y == 3:
                c.configure(text="X", foreground=colorpl1)
            elif y == 4:
                d.configure(text="X", foreground=colorpl1)
            elif y == 5:
                e.configure(text="X", foreground=colorpl1)
            elif y == 6:
                f.configure(text="X", foreground=colorpl1)
            elif y == 7:
                g.configure(text="X", foreground=colorpl1)
            elif y == 8:
                h.configure(text="X", foreground=colorpl1)
            elif y == 9:
                i.configure(text="X", foreground=colorpl1)
        master.update()
        if cont <= 8 and Vittoria != True:
            for z in pl2:
                if z == 1:
                    a.configure(text="O", foreground=colorpl2, activeforeground=colorpl2)
                elif z == 2:
                    b.configure(text="O", foreground=colorpl2, activeforeground=colorpl2)
                elif z == 3:
                    c.configure(text="O", foreground=colorpl2, activeforeground=colorpl2)
                elif z == 4:
                    d.configure(text="O", foreground=colorpl2, activeforeground=colorpl2)
                elif z == 5:
                    e.configure(text="O", foreground=colorpl2, activeforeground=colorpl2)
                elif z == 6:
                    f.configure(text="O", foreground=colorpl2, activeforeground=colorpl2)
                elif z == 7:
                    g.configure(text="O", foreground=colorpl2, activeforeground=colorpl2)
                elif z == 8:
                    h.configure(text="O", foreground=colorpl2, activeforeground=colorpl2)
                elif z == 9:
                    i.configure(text="O", foreground=colorpl2, activeforeground=colorpl2)

        return cont,pl1,pl2


    def callback(K,num):#already tryed outside
        global cont,Vittoria,co,color,pl1vitt,pl2vitt,turn,btn,a,b,c,d,e,f,g,h,i,x,turner

        #disable btn when pressed more times and prevent other clicks
        if Vittoria == True:
                cont = -2
        if check(pl1,num) == True or check(pl2,num) == True:
            K.config(command=0)
        #normal game (i separated it for other propouses)
        else:
                gameplay(K,num)

            
        #win conditions (since i cant program every possibility i used permutations)
        pl1win = list(permutations(pl1,3))
        pl2win = list(permutations(pl2,3))
        # stupid ass win screen i am too bored to rewrite it
        if winck(win,pl1win) == True:
            Vittoria = True
            if co == 0:
                    fakeclean()
                    co = -2
                    win1 = tk.Toplevel()
                    win1.title("winner")
                    sos = tk.Text(win1, height=3,width=25)
                    sos.grid(column=3,row=0)
                    if turn % 2 == 0:
                            pl1vitt=pl1vitt + 1 #you shouldn't touch this,it will break the counter
                            sos.insert(tk.END, "You Won")
                    try:    #used this try/except since all the code stop executing if win window get closed
                            Flashyflash(sos)
                    except:
                            pass
                    win1.destroy()
                    pl1box.configure(text=pl1vitt) #counter update
                    pl2box.configure(text=pl2vitt)
                    turner += 1
                    start(master,pl1box,pl2box)
        elif winck(win,pl2win) == True:
            
            Vittoria = True
            if co == 0:
                    fakeclean()
                    co = -2
                    win2 = tk.Toplevel()
                    win2.title("Looser")
                    sos = tk.Text(win2, height=3,width=25)
                    sos.grid(column=3,row=0)
                    if turn % 2 == 0:
                            pl2vitt=pl2vitt + 1#and this
                            sos.insert(tk.END, "You lost to the easiest mode ever")
                    try :   
                            Flashyflash(sos)
                    except:
                            pass
                    win2.destroy()
                    pl1box.configure(text=pl1vitt)
                    pl2box.configure(text=pl2vitt)
                    turner += 1
                    start(master,pl1box,pl2box)
        if cont >= 9 and Vittoria == None:#stupid ass lose screen
            if co == 0:
                fakeclean()
                co = -2
                loose = tk.Toplevel()
                loose.title("Looser")
                txtloose = tk.Text(loose, height=3,width=25)
                txtloose.insert(tk.END, "Tie")
                txtloose.grid(column=3,row=0)
                try :
                        Flashyflash(txtloose)
                except:
                        pass
                turner += 1
                loose.destroy()
                start(master,pl1box,pl2box)
        return cont,Vittoria,co,color,pl1vitt,pl2vitt,True
    def fakeclean():
        global x
        for y in x:
            y.configure(text = "")
    def winck(a, b) :#check for combinations
            for x in a :
                for y in b :
                    if x == y :
                        return True
    def Flashyflash(window):#just color display
            global colorlist
            x=0
            while x != 13:#if you want more or less colors in win\lose window
                    window.configure(bg=random.choice(colorlist))
                    window.update()
                    time.sleep(0.2)
                    x = x + 1        
    def check(a,b): #another check
            for x in a:
                    if x == b:
                            return True

    def checkbx(a): #change color background mechanism (try to unite it with the other below)
            global num,colorv
            num = num + 1
            if num % 2 == 0:
                    a.config(background='black',foreground='green',activeforeground='white')
                    colorv = True
            else:
                    a.config(background='black',foreground='white',activeforeground='green')
                    colorv = False
            master.update()
            return num,colorv
    def checkbx2(a): #change player color mechanism try to unite it
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
    def checkbx3(a,b,c,d): #reset all colors
        global color,colorpl1,colorpl2,colorc,colorv,num,num2
        color='black'
        colorpl1='cyan'
        colorpl2='red'
        a.config(background='black',foreground='white',activeforeground='green')
        b.config(background='black',foreground='white',activeforeground='green')
        c.config(foreground='yellow',activeforeground='yellow')
        d.config(foreground='yellow',activeforeground='yellow')
        colorc=None
        colorv=None
        num=1
        num2=1
        master.update()
        return color,colorpl1,colorpl2,colorc,colorv,num,num2
    def start(l,a1,a2): #main play and reset values for win possibilities
            global Restart
            Restart.configure(command=0)
            global turner,a,b,c,d,e,f,g,h,i,x,Vittoria,pl1vitt,pl2vitt,turn,end,co,cont,pl1,pl2,win,color,colorv,colorc,colorpl1,colorpl2
    #values reset
            Vittoria = None
            end = 0
            co = 0
            cont = 0
            pl1 = []
            pl2 = []
            if colorv == True: #see checkbx, i need to change the backgroun color before creating those bottons
                    color=random.choice(colorlist)
                    while color == colorpl1 or color == colorpl2:
                        color=random.choice(colorlist)
            elif colorv == None:
                    color='Black'
            else:
                    pass
    #adding numbers will increase games possibilities,(new tabs 4x4,5x5)(need to change also the table)
            win = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
            turn = 2
            a = Button(master, text="",font=('arial','20'), state=ACTIVE, height = 1,width = 3,activebackground=color,background=color)
            a.configure(command=lambda :callback(a,1))
            a.grid(row=0 ,column=0)
            b = Button(master, text="",font=('arial','20'), state=ACTIVE, height = 1,width = 3,activebackground=color,background=color)
            b.configure(command=lambda :callback(b,2))
            b.grid(row=0 ,column=1)
            c = Button(master, text="",font=('arial','20'), state=ACTIVE, height = 1,width = 3,activebackground=color,background=color)
            c.configure(command=lambda :callback(c,3))
            c.grid(row=0 ,column=2)
            d = Button(master, text="",font=('arial','20'), state=ACTIVE, height = 1,width = 3,activebackground=color,background=color)
            d.configure(command=lambda :callback(d,4))
            d.grid(row=1 ,column=0)
            e = Button(master, text="",font=('arial','20'), state=ACTIVE, height = 1,width = 3,activebackground=color,background=color)
            e.configure(command=lambda :callback(e,5))
            e.grid(row=1 ,column=1)
            f = Button(master, text="",font=('arial','20'), state=ACTIVE, height = 1,width = 3,activebackground=color,background=color)
            f.configure(command=lambda :callback(f,6))
            f.grid(row=1 ,column=2)
            g = Button(master, text="",font=('arial','20'), state=ACTIVE, height = 1,width = 3,activebackground=color,background=color)
            g.configure(command=lambda :callback(g,7))
            g.grid(row=2 ,column=0)
            h = Button(master, text="",font=('arial','20'), state=ACTIVE, height = 1,width = 3,activebackground=color,background=color)
            h.configure(command=lambda :callback(h,8))
            h.grid(row=2 ,column=1)
            i = Button(master, text="",font=('arial','20'), state=ACTIVE, height = 1,width = 3,activebackground=color,background=color)
            i.configure(command=lambda :callback(i,9))
            i.grid(row=2 ,column=2)
            x = (a,b,c,d,e,f,g,h,i)
            if turn % 2 == 0 : #only god knows how this color bullshit works,but its bugless (idk why)
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
            if (turner % 2) == 1:
                pl2.append(randint(1, 9, 1))
                cont += 1
                for z in pl2:
                    if z == 1:
                        a.configure(text="O", foreground=colorpl2, activeforeground=colorpl2)
                    elif z == 2:
                        b.configure(text="O", foreground=colorpl2, activeforeground=colorpl2)
                    elif z == 3:
                        c.configure(text="O", foreground=colorpl2, activeforeground=colorpl2)
                    elif z == 4:
                        d.configure(text="O", foreground=colorpl2, activeforeground=colorpl2)
                    elif z == 5:
                        e.configure(text="O", foreground=colorpl2, activeforeground=colorpl2)
                    elif z == 6:
                        f.configure(text="O", foreground=colorpl2, activeforeground=colorpl2)
                    elif z == 7:
                        g.configure(text="O", foreground=colorpl2, activeforeground=colorpl2)
                    elif z == 8:
                        h.configure(text="O", foreground=colorpl2, activeforeground=colorpl2)
                    elif z == 9:
                        i.configure(text="O", foreground=colorpl2, activeforeground=colorpl2)

            master.update()
            Restart.configure(command=lambda :start(master,pl1box,pl2box))
            return color,x,a,b,c,d,e,f,g,h,i

    def checkbx4(a,b): #reset and reconfigure counter 
            global pl1vitt,pl2vitt
            pl1vitt=0
            pl2vitt=0
            a.configure(text=pl1vitt)
            b.configure(text=pl2vitt)
            master.update()
            return pl1vitt,pl2vitt
    def out():
            pl1vitt=0
            pl2vitt=0
            master.destroy()
    #other buttons (see the text configured)
    checkbox3 = Button(master, text="reset colors", font=('italic','7'),foreground='white',activeforeground='white',command= lambda :checkbx3(checktext,checktext2,Restart,checkbox3) ,state=ACTIVE,activebackground='black',background='black' )
    checkbox3.place(y=110, x=200) #the reset color botton
    checkbox4 = Button(master, text="reset counter", font=('italic','7'),foreground='white',activeforeground='white',command= lambda :checkbx4(pl1box,pl2box) ,state=ACTIVE,activebackground='black',background='black' )
    checkbox4.place(y=135, x=200)
    checktext = Button(master,text="random background",command= lambda :checkbx(checktext),font=('italic','7') ,state=ACTIVE,background="black",foreground='white',activebackground='Black',activeforeground='white')
    checktext.place(y=60, x=186)
    checktext2 = Button(master,text="random player color",font=('italic','7'),command= lambda :checkbx2(checktext2) ,state=ACTIVE,foreground='white',background="black",activebackground='Black',activeforeground='white')
    checktext2.place(y=80, x=186)
    start(master,pl1box,pl2box)
    master.protocol("WM_DELETE_WINDOW", out)
    master.mainloop()
#vsAI()#uncomment this to make it work alone 