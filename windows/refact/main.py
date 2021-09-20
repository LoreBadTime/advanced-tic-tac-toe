import time,random,numpy,menu
from numpy.random import randint
from tkinter import *
import tkinter as tk
from itertools import permutations

global done,co,Vittoria,num,colorv,pl1vitt,pl2vitt,turn,player1,player2,master,turner
turner = 0
retur = False
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
#combinations
com = (1,3,7,9)
comb = (1,2,3,4,6,7,8,9)
comb1 = (2,4,6,8)
comb2 = [(1,2),(1,3),(2,3),(4,5),(5,6),(4,6),(7,8),(7,9),(8,9),
         (1,4),(1,7),(4,7),(2,5),(5,8),(2,8),(3,6),(6,9),(3,9),
         (1,5),(5,9),(1,9),(3,5),(3,7),(5,7)]
comb3 = [(1,9),(3,7)]
comb4 = ((2,7),(2,9),(3,4),(3,9),(1,8),(8,3),(1,6),(6,7))
comb5 = ((1,5),(5,9),(3,5),(5,7))
comb6 = ((1,8),(1,6),(3,4),(3,8),(7,2),(7,6),(9,2),(9,4))
comb7 = ((2,6),(6,8),(8,4),(4,2))
win = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
def fakeclean():
          global a,b,c,d,e,f,g,h,i
          z = [a,b,c,d,e,f,g,h,i]
          for y in z:
               y.configure(text="")
     # count turn and configure the button text #Change AI to pl2
def speedwrite(numlist,anothernum):#this will check for win tryes fo both AI and player
          global AI,pl1list,pl2list,trick,ptot,pl1,pl2
          if check(pl2,anothernum) != True:
                    pl1a = pl1
                    pl2b = pl2
                    s = False
                    for x in pl1a:
                         for y in pl2b:
                              if y == x:
                                   s = True
                              else :
                                   pass
                    #this will calculate games wins
                    if check(pl1list,comb2[numlist]) == True and s == False or check(pl2list,comb2[numlist]) == True and s == False :
                         pl1a.append(anothernum)
                         pl2b.append(anothernum)
                         pl1test = (list(permutations(pl1a,3)))
                         pl2test = (list(permutations(pl2b,3)))
                         pl1a.remove(anothernum)
                         pl2b.remove(anothernum)
                         if (winck(win,pl2test) == True or winck(win,pl1test) == True) and check(pl1,anothernum) != True:
                                   AI.append(anothernum)
                                   return AI
          else:
               return AI
def gameplaynormal(K,num):
         global combinations,strategy,combo,cont,pl1,pl2,a,b,c,d,e,f,g,h,i,x,comb2,comb,AI,pl1list,pl2list,trick,ptot,fun
         trick = 0
         pl1.append(num)
         pl1list = (list(permutations(pl1,2)))
         pl2list = (list(permutations(pl2,2)))
         cont = cont + 1
         AI = []
         strategy = True
         if cont < 9:#now there are only specific cases   
              if (winck(comb2,pl1list) == True or winck(comb2,pl2list) == True) and strategy == True :
                  speedwrite(0,3)
                  speedwrite(1,2)
                  speedwrite(2,1)
                  speedwrite(3,6)
                  speedwrite(4,4)
                  speedwrite(5,5)
                  speedwrite(6,9)
                  speedwrite(7,8)
                  speedwrite(8,7)
                  speedwrite(9,7)
                  speedwrite(10,4)
                  speedwrite(11,1)
                  speedwrite(12,8)
                  speedwrite(13,2)
                  speedwrite(14,5)
                  speedwrite(15,9)
                  speedwrite(16,3)
                  speedwrite(17,6)
                  speedwrite(18,9)
                  speedwrite(19,1)
                  speedwrite(20,5)
                  speedwrite(21,7)
                  speedwrite(22,5)
                  speedwrite(23,3)
                  
                  
              try:
                  for x in AI:#this will eliminate duplicates and will prefer AI wins
                            x = int(x)
                            pl1a = pl1
                            pl2b = pl2
                            pl1a.append(x)
                            pl2b.append(x)
                            
                            pl1test = (list(permutations(pl1a,3)))
                            pl2test = (list(permutations(pl2b,3)))
                            pl1a.remove(x)
                            pl2b.remove(x)
                            
                            if winck(win,pl2test) == True and check(pl1,x) != True:
                                 
                                 AI = []
                                 AI.append(x)
                                 break
                            elif winck(win,pl1test) == True and check(pl2,x) != True:
                                 AI = x
                  if check(pl1,AI) == True or check(pl2,AI) == True or AI == []:   
                               AI = int(randint(1, 10, 1))
                               
                               while check(pl1,AI) == True or check(pl2,AI) == True:
                                    AI = int(randint(1, 10, 1))
              except:
                  pass
          
              try:
                  AI = str(AI)[1]
                  AI = int(AI)
              except:
                  pass
     
              else:
                   if cont < 9:
                        while check(pl1,AI) == True or check(pl2,AI) == True or AI == []:
                               AI = int(randint(1, 10, 1))
                               
                   else:
                        pass
              cont = cont + 1
              pl2.append(AI)
              return cont,pl1,pl2,combo,combinations
def gameplayeasy(K,num):
        global cont,pl1,pl2
        pl1.append(num)
        AI = randint(1, 10, 1)
        while(check(pl1,AI) == True or check(pl2,AI) == True) and cont < 8:
            if cont > 8:
                break
            AI = randint(1, 10, 1)          
        pl2.append(AI)
        cont += 2
        return cont,pl1,pl2
def gameplayhard(K,num):
         global combinations,strategy,combo,cont,pl1,pl2,a,b,c,d,e,f,g,h,i,x,comb2,comb,AI,pl1list,pl2list,trick,ptot,fun
         trick = 0
         if cont == 0 or cont == 2 or cont == 4 or cont == 6 or cont == 8:
                 pl1.append(num)
                 pl1list = (list(permutations(pl1,2)))
                 pl2list = (list(permutations(pl2,2)))
                 cont = cont + 1
                 AI = []
                 strategy = True
                 if cont < 9:#now there are only specific cases
                      if cont == 1:
                           if check(comb,num) == True:
                                AI.append(5)
                           elif num == 5:
                                AI.append(random.choice(com))
                           else:
                                AI.append(randint(1, 9, 1))
                                while winck(pl1,AI) == True  or winck(pl2,AI) == True :   
                                       AI.append(randint(1, 9, 1))
                           strategy = False
                      elif cont == 3 and (winck(pl1list,comb7) == True or winck(pl1list,comb6) == True or winck(pl1list,comb3) == True or winck(pl1list,comb5) == True): 
                           if winck(pl1list,comb3) == True:
                                AI.append(random.choice(comb1))
                                 
                           elif winck(pl1list,comb5) == True:
                                if check(pl1list,comb5[0]) == True:
                                     AI.append(9)
                                     if winck(pl1,AI) == True or winck(pl2,AI) == True:
                                          AI.remove(9)
                                          AI.append(3)
                                elif check(pl1list,comb5[1]) == True:
                                     AI.append(1)
                                     if winck(pl1,AI) == True or winck(pl2,AI) == True:
                                          AI.remove(1)
                                          AI.append(7)
                                elif check(pl1list,comb5[2]) == True:
                                     AI.append(7)
                                     if winck(pl1,AI) == True or winck(pl2,AI) == True:
                                          AI.remove(7)
                                          AI.append(9)
                                elif check(pl1list,comb5[3]) == True:
                                     AI.append(3)
                                     if winck(pl1,AI) == True or winck(pl2,AI) == True:
                                          AI.append(1)
                                          AI.remove(3)
                             
                           elif winck(pl1list,comb7) == True:
                                if check(pl1list,comb7[0]) == True:
                                     AI.append(3)
                                elif check(pl1list,comb7[1]) == True:
                                     AI.append(9)
                                elif check(pl1list,comb7[2]) == True:
                                     AI.append(7)
                                elif check(pl1list,comb7[3]) == True:
                                     AI.append(1)

                                    
                           elif winck(pl1list,comb6) == True:
                                if check(pl1list,comb6[0]) == True or check(pl1list,comb6[4]) == True :
                                     AI.append(4)
                                elif check(pl1list,comb6[1]) == True or check(pl1list,comb6[2]) == True:
                                     AI.append(2)
                                elif check(pl1list,comb6[3]) == True or check(pl1list,comb6[6]) == True :
                                     AI.append(6)
                                elif check(pl1list,comb6[5]) == True or check(pl1list,comb6[7]) == True:
                                     AI.append(8)
                                
                                combinations = True
                           
                      elif cont == 5 and combinations == True:
                           
                           if check(pl1list,comb6[0]) == True or check(pl1list,comb6[1]) == True :
                                AI.append(9)
                           elif check(pl1list,comb6[2]) == True or check(pl1list,comb6[3]) == True:
                                AI.append(7)
                           elif check(pl1list,comb6[4]) == True or check(pl1list,comb6[5]) == True:
                                AI.append(3)
                           elif check(pl1list,comb6[6]) == True or check(pl1list,comb6[7]) == True :
                                AI.append(1)    
                      if (winck(comb2,pl1list) == True or winck(comb2,pl2list) == True) and strategy == True :
                          speedwrite(0,3)
                          speedwrite(1,2)
                          speedwrite(2,1)
                          speedwrite(3,6)
                          speedwrite(4,4)
                          speedwrite(5,5)
                          speedwrite(6,9)
                          speedwrite(7,8)
                          speedwrite(8,7)
                          speedwrite(9,7)
                          speedwrite(10,4)
                          speedwrite(11,1)
                          speedwrite(12,8)
                          speedwrite(13,2)
                          speedwrite(14,5)
                          speedwrite(15,9)
                          speedwrite(16,3)
                          speedwrite(17,6)
                          speedwrite(18,9)
                          speedwrite(19,1)
                          speedwrite(20,5)
                          speedwrite(21,7)
                          speedwrite(22,5)
                          speedwrite(23,3)
                          
                          
                      try:
                          for x in AI:#this will eliminate duplicates and will prefer AI wins
                                    x = int(x)
                                    pl1a = pl1
                                    pl2b = pl2
                                    pl1a.append(x)
                                    pl2b.append(x)
                                    pl1test = (list(permutations(pl1a,3)))
                                    pl2test = (list(permutations(pl2b,3)))
                                    pl1a.remove(x)
                                    pl2b.remove(x)
                                    if winck(win,pl2test) == True and check(pl1,x) != True:
                                         AI = []
                                         AI.append(x)
                                         break
                                    elif winck(win,pl1test) == True and check(pl2,x) != True:
                                         AI = x
                          if check(pl1,AI) == True or check(pl2,AI) == True or AI == []:   
                                       AI = int(randint(1, 10, 1))
                                       while check(pl1,AI) == True or check(pl2,AI) == True:
                                            AI = int(randint(1, 10, 1))
                      except:
                          pass
                      try:
                          AI = str(AI)[1]
                          AI = int(AI)
                      except:
                          pass
                      else:
                           if cont < 9:
                                while check(pl1,AI) == True or check(pl2,AI) == True or AI == []:
                                       AI = int(randint(1, 10, 1))
                      cont = cont + 1
                      pl2.append(AI)
                      return cont,pl1,pl2,combo,combinations
def display():
         global pl1,pl2
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

         return cont,pl1,pl2,combo,combinations
def callback(K,num,mode):#already tryed outside
         global combo,cont,Vittoria,co,color,pl1vitt,pl2vitt,turn,btn,a,b,c,d,e,f,g,h,i,x,ptot,AI,pl1win,pl2win,turner
         AI = []
         combo = False
         #disable btn when pressed more times and prevent other clicks
         if Vittoria == True:
                 cont = -2
         if check(pl1,num) == True or check(pl2,num) == True:
             K.config(command=0)
         #normal game (i separated it for other propouses)
         else:
             if mode == 1:
                 gameplaynormal(K,num)
             elif mode == 2:
                 gameplayhard(K,num)
             elif mode == 3:
                 gameplayeasy(K,num)
             display()
         #win conditions (since i can't programm every possibility i used permutations)
         pl1win = list(permutations(pl1,3))
         pl2win = list(permutations(pl2,3))
         # stupid ass win screen i am too bored to rewrite it
         if winck(win,pl1win) == True:
             Vittoria = True
             if co == 0:
                     co = -2
                     win1 = tk.Toplevel()
                     win1.title("Winner")
                     sos = tk.Text(win1, height=7,width=25)
                     sos.grid(column=3,row=0)
                     if turn % 2 == 0:
                             pl1vitt=pl1vitt + 1 
                             sos.insert(tk.END, "You Won!")
                     try:   
                             Flashyflash(sos)
                     except:
                             pass
                     pl1box.configure(text=pl1vitt) #counter update
                     pl2box.configure(text=pl2vitt)
                     turner += 1
                     master.update()
                     win1.destroy()      
         elif winck(win,pl2win) == True:
             Vittoria = True
             if co == 0:
                     co = -2
                     win2 = tk.Toplevel()
                     win2.title("Looser")
                     sos = tk.Text(win2, height=3,width=25)
                     sos.grid(column=3,row=0)
                     if turn % 2 == 0:
                             pl2vitt=pl2vitt + 1#and this
                             sos.insert(tk.END, "You lost,keep trying")
                     try :   
                             Flashyflash(sos)
                     except:
                             pass
                     pl1box.configure(text=pl1vitt)
                     pl2box.configure(text=pl2vitt)
                     turner += 1
                     master.update() 
                     win2.destroy()
         if cont >= 9 and Vittoria == None:#stupid ass lose screen
             if co == 0:
                 co = -2
                 loose = tk.Toplevel()
                 loose.title("Loosers")
                 txtloose = tk.Text(loose, height=3,width=25)
                 txtloose.insert(tk.END, "Try again")
                 txtloose.grid(column=3,row=0)
                 try :
                         Flashyflash(txtloose)
                 except:
                         pass
                 turner += 1
                 loose.destroy()
         return cont,Vittoria,co,color,pl1vitt,pl2vitt,True
    
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
def start(l,a1,a2,mode): #main play and reset values for win possibilities
             global Restart
             Restart.configure(command=0)
             global combinations,master,ptot,a,b,c,d,e,f,g,h,i,x,Vittoria,pl1vitt,pl2vitt,turn,end,co,cont,pl1,pl2,win,color,colorv,colorc,colorpl1,colorpl2
     #values reset
             
             if colorv == True: #see checkbx, i need to change the backgroun color before creating those bottons
                     color=random.choice(colorlist)
                     while color == colorpl1 or color == colorpl2:
                         color=random.choice(colorlist)
             elif colorv == None:
                     color='Black'
             else:
                     pass
             ptot = []
             Vittoria = None
             end = 0
             co = 0
             cont = 0
             pl1 = []
             pl2 = []
             combinations = False
     #adding numbers will increase games possibilities,(new tabs 4x4,5x5)(need to change also the table)
             win = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
             turn = 2
             a = Button(master, text="",font=('arial','20'), state=ACTIVE, height = 1,width = 3,activebackground=color,background=color)
             a.configure(command=lambda :callback(a,1,mode))
             a.grid(row=0 ,column=0)
             b = Button(master, text="",font=('arial','20'), state=ACTIVE, height = 1,width = 3,activebackground=color,background=color)
             b.configure(command=lambda :callback(b,2,mode))
             b.grid(row=0 ,column=1)
             c = Button(master, text="",font=('arial','20'), state=ACTIVE, height = 1,width = 3,activebackground=color,background=color)
             c.configure(command=lambda :callback(c,3,mode))
             c.grid(row=0 ,column=2)
             d = Button(master, text="",font=('arial','20'), state=ACTIVE, height = 1,width = 3,activebackground=color,background=color)
             d.configure(command=lambda :callback(d,4,mode))
             d.grid(row=1 ,column=0)
             e = Button(master, text="",font=('arial','20'), state=ACTIVE, height = 1,width = 3,activebackground=color,background=color)
             e.configure(command=lambda :callback(e,5,mode))
             e.grid(row=1 ,column=1)
             f = Button(master, text="",font=('arial','20'), state=ACTIVE, height = 1,width = 3,activebackground=color,background=color)
             f.configure(command=lambda :callback(f,6,mode))
             f.grid(row=1 ,column=2)
             g = Button(master, text="",font=('arial','20'), state=ACTIVE, height = 1,width = 3,activebackground=color,background=color)
             g.configure(command=lambda :callback(g,7,mode))
             g.grid(row=2 ,column=0)
             h = Button(master, text="",font=('arial','20'), state=ACTIVE, height = 1,width = 3,activebackground=color,background=color)
             h.configure(command=lambda :callback(h,8,mode))
             h.grid(row=2 ,column=1)
             i = Button(master, text="",font=('arial','20'), state=ACTIVE, height = 1,width = 3,activebackground=color,background=color)
             i.configure(command=lambda :callback(i,9,mode))
             i.grid(row=2 ,column=2)
             #needs developing attack and defense mode
             if ((turner % 2) == 1) and (mode == 1 or mode == 3):
                tmpAI = 0
                if mode == 1:##or mode == 2:
                    tmpAI = randint(1, 5, 1)
                    if tmpAI == 1:
                         pass
                    elif tmpAI == 2:
                         tmpAI = 3
                    elif tmpAI == 3:
                         tmpAI = 5
                    elif tmpAI == 4:
                         tmpAI = 7
                    elif tmpAI == 5:
                         tmpAI = 9
                else:
                    tmpAI = randint(1, 10, 1)
                pl2.append(tmpAI)
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
             master.update()
             l.geometry("280x200")
             Restart.configure(command=lambda :start(master,pl1box,pl2box,mode))

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
    global pl1vitt,pl1box,pl2vitt,pl2box,retur,master
    pl1vitt=0
    pl2vitt=0
    pl1box.config(text=pl1vitt)
    pl2box.config(text=pl2vitt)
    master.destroy()
    menu.mainmenu()
    
    
            
 #other buttons (see the text configured)
def main(mode):
     global Restart,master,pl1box,pl2box
     #just start tk
     master = Tk()
     master.title("Tick tac toe")
     master.configure(background='black')
     master.geometry("280x200")
     master.resizable(False,False)
     Restart = Button (master,text="Restart", command= lambda :start(master,pl1box,pl2box,mode) ,state=ACTIVE,background='black',activebackground='black',foreground='white',activeforeground='white')
     Restart.place(height=20, width=50 ,y=15, x=200)#the restart button
     pl1box = Button(master, text=pl1vitt,foreground='cyan',disabledforeground='cyan',state=DISABLED,activebackground='black',background='black' )
     pl1box.place(height=30 ,width=30,y=169, x=15)
     pl2box = Button(master, text=pl2vitt,foreground='red',disabledforeground='red',state=DISABLED,activebackground='black',background='black' )
     pl2box.place(height=30 ,width=30,y=169, x=130)
     checkbox4 = Button(master, text="reset counter", font=('italic','7'),foreground='white',activeforeground='white',command= lambda :checkbx4(pl1box,pl2box) ,state=ACTIVE,activebackground='black',background='black' )
     checkbox4.place(y=135, x=200)
     checktext = Button(master,text="random background",command= lambda :checkbx(checktext),font=('italic','7') ,state=ACTIVE,background="black",foreground='white',activebackground='Black',activeforeground='white')
     checktext.place(y=60, x=186)
     checktext2 = Button(master,text="random player color",font=('italic','7'),command= lambda :checkbx2(checktext2) ,state=ACTIVE,foreground='white',background="black",activebackground='Black',activeforeground='white')
     checktext2.place(y=80, x=186)
     checkbox3 = Button(master, text="reset colors", font=('italic','7'),foreground='white',activeforeground='white',command= lambda :checkbx3(checktext,checktext2,Restart,checkbox3) ,state=ACTIVE,activebackground='black',background='black' )
     checkbox3.place(y=110, x=200) #the reset color botton
     start(master,pl1box,pl2box,mode)
     master.protocol("WM_DELETE_WINDOW", out)
     master.mainloop()

     
     


