#By LoreBadTime,some import are useless(now)
#a little precisation,buttons here are unique,they are only a UI thing,the main process is stored in the callback
import time,random,menu
from tkinter import *
import tkinter as tk
from itertools import permutations
global co,Vittoria,num,colorv,pl1vitt,pl2vitt,turn,menureturn,pl1box,pl2box,master
#game
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



def local():
    global menureturn,pl1box,pl2box,pl1vitt,pl2vitt,master
    menureturn = False  
     
  
    #just start tk
    master = Tk()
    master.title("Tick tac toe")
    master.configure(background='black')
    master.geometry("280x200")
    master.resizable(False,False)
    pl1box = Button(master, text=pl1vitt,foreground='cyan',disabledforeground='cyan',state=DISABLED,activebackground='black',background='black' )
    pl1box.place(height=30 ,width=30,y=169, x=15)
    pl2box = Button(master, text=pl2vitt,foreground='red',disabledforeground='red',state=DISABLED,activebackground='black',background='black' )
    pl2box.place(height=30 ,width=30,y=169, x=130)
    Restart = Button (master,text="Restart", command= lambda :start(master,pl1box,pl2box) ,state=ACTIVE,background='black',activebackground='black',foreground='white',activeforeground='white')
    Restart.place(height=20, width=50 ,y=15, x=200)#the restart button
            
    # count turn and configure the button text
    def gameplay(K,num):
        global cont
        if cont == 0 or cont == 2 or cont == 4 or cont == 6 or cont == 8:
                K.configure(text="X", foreground=colorpl1)
                master.update()
                pl1.append(num)
        elif cont == 1 or cont == 3 or cont == 5 or cont == 7:
                K.configure(text="O", foreground=colorpl2)
                master.update()
                pl2.append(num)
        cont = cont + 1
        return cont



    class btn():
            def design(self,ascissa,ordinata,num,master):#its just a way to write btn propreties
                    def callback(K,num):#already tryead outside
                        global cont,Vittoria,co,color,pl1vitt,pl2vitt,turn,btn

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
                                    co = -2
                                    win1 = tk.Toplevel()
                                    win1.title("winner")
                                    sos = tk.Text(win1, height=3,width=25)
                                    sos.grid(column=3,row=0)
                                    if turn % 2 == 0:
                                            pl1vitt=pl1vitt + 1 #you shouldn't touch this,it will break the counter
                                            sos.insert(tk.END, "player 1 won!")
                                    else:
                                            pl2vitt=pl2vitt + 1 #also this
                                            sos.insert(tk.END, "player 2 won!")
                                    try:    #used this try/except since all the code stop executing if win window get closed
                                            Flashyflash(sos)
                                    except:
                                            pass
                                    pl1box.configure(text=pl1vitt) #counter update
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
                                        if turn % 2 == 0:
                                                pl2vitt=pl2vitt + 1#and this
                                                sos.insert(tk.END, "player 2 won !")
                                        else:
                                                pl1vitt=pl1vitt + 1#and this
                                                sos.insert(tk.END, "player 1 won !")
                                        try :   
                                                Flashyflash(sos)
                                        except:
                                                pass
                                        pl1box.configure(text=pl1vitt)
                                        pl2box.configure(text=pl2vitt)
                                        master.update() 
                                        win2.destroy()
                        if cont >= 9 and Vittoria == None:#stupid ass lose screen
                            if co == 0:
                                co = -2
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

                    global color #btns config and lambda
                    self = Button(master, text="",font=('arial','20'), state=ACTIVE, height = 1,width = 3,activebackground=color,background=color)
                    self.configure(command=lambda :callback(self,num))
                    self.grid(row=ascissa ,column=ordinata)
                    return self

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
                    time.sleep(0.3)
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
            global Vittoria,pl1vitt,pl2vitt,turn,end,co,cont,pl1,pl2,win,color,colorv,colorc,colorpl1,colorpl2
    #values reset
            if colorv == True: #see checkbx, i need to change the backgroun color before creating those bottons
                    color=random.choice(colorlist)
                    while color == colorpl1 or color == colorpl2:
                        color=random.choice(colorlist)
            elif colorv == None:
                    color='Black'
            else:
                    pass

            Vittoria = None
            end = 0
            co = 0
            cont = 0
            pl1 = []
            pl2 = []
    #adding numbers will increase games possibilities,(new tabs 4x4,5x5)(need to change also the table)
            win = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
            turn = turn + 1
            btn.design(btn,0,0,1,master)
            btn.design(btn,0,1,2,master)
            btn.design(btn,0,2,3,master)
            btn.design(btn,1,0,4,master)
            btn.design(btn,1,1,5,master)
            btn.design(btn,1,2,6,master)
            btn.design(btn,2,0,7,master)
            btn.design(btn,2,1,8,master)
            btn.design(btn,2,2,9,master)
            
            
            
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
            master.update()

            return color

    def checkbx4(a,b): #reset and reconfigure counter 
            global pl1vitt,pl2vitt
            pl1vitt=0
            pl2vitt=0
            a.configure(text=pl1vitt)
            b.configure(text=pl2vitt)
            master.update()
            return pl1vitt,pl2vitt
    def out():
            global pl1vitt,pl1box,pl2vitt,pl2box,retur,master
            pl1vitt=0
            pl2vitt=0
            pl1box.config(text=pl1vitt)
            pl2box.config(text=pl2vitt)
            master.destroy()
            menu.mainmenu()
            
    #other buttons (see the text configured)
    checkbox3 = Button(master, text="reset colors", font=('italic','7'),foreground='white',activeforeground='white',command= lambda :checkbx3(checktext,checktext2,Restart,checkbox3) ,state=ACTIVE,activebackground='black',background='black' )
    checkbox3.place(y=110, x=200) #the reset color botton
    checkbox4 = Button(master, text="reset counter", font=('italic','7'),foreground='white',activeforeground='white',command= lambda :checkbx4(pl1box,pl2box) ,state=ACTIVE,activebackground='black',background='black' )
    checkbox4.place(y=135, x=200)
    checktext = Button(master,text="random background",command= lambda :checkbx(checktext),font=('italic','7') ,state=ACTIVE,background="black",foreground='white',activebackground='Black',activeforeground='white')
    checktext.place(y=60, x=186)
    checktext2 = Button(master,text="random player color",font=('italic','7'),command= lambda :checkbx2(checktext2) ,state=ACTIVE,foreground='white',background="black",activebackground='Black',activeforeground='white')
    checktext2.place(y=80, x=186)
    #win counters
    #spaghetti code launch
    start(master,pl1box,pl2box)
    master.protocol("WM_DELETE_WINDOW", out)
    master.mainloop()

#local()#remove this comment to make it work alone

