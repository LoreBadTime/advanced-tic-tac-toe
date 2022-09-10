import time,random
from tkinter import *
import tkinter as tk
from itertools import permutations
import secrets 
import gc

global socket,co,Vittoria,num,colorv,pl1vitt,pl2vitt,turn,master,turner,onlineturn
onlineturn = None
turner = 0
retur = False
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

def speedwrite():#this will check for win tryes fo both AI and player
          global AI,pl1list,pl2list,trick,ptot,pl1,pl2
          args = [(0,3),(1,2),(2,1),(3,6),(4,4),(5,5),(6,9),(7,8),(8,7),(9,7),
                            (10,4),(11,1),(12,8),(13,2),(14,5),(15,9),(16,3),(17,6),(18,9),
                            (19,1),(20,5),(21,7),(22,5),(23,3)]
          for elem in args:
            numlist,anothernum = elem
            if check(pl2,anothernum) != True:
                      pl1a = pl1
                      pl2b = pl2
                      s = False
                      for x in pl1a:
                           if x in pl2b:
                              s = True
                      #this will calculate games wins
                      if (check(pl1list,comb2[numlist]) or check(pl2list,comb2[numlist])) and s == False :
                           pl1a.append(anothernum)
                           pl2b.append(anothernum)
                           pl1test = (list(permutations(pl1a,3)))
                           pl2test = (list(permutations(pl2b,3)))
                           pl1a.remove(anothernum)
                           pl2b.remove(anothernum)
                           if (winck(win,pl2test) or winck(win,pl1test)) and check(pl1,anothernum) != True:
                                     AI.append(anothernum)
def gameplaynormal(num):
         global combinations,strategy,combo,cont,pl1,pl2,a,b,c,d,e,f,g,h,i,x,comb2,comb,AI,pl1list,pl2list,trick,ptot
         trick = 0
         pl1.append(num)
         pl1list = (list(permutations(pl1,2)))
         pl2list = (list(permutations(pl2,2)))
         cont = cont + 1
         AI = []
         strategy = True
         if cont < 9:#now there are only specific cases   
              if (winck(comb2,pl1list) or winck(comb2,pl2list)) and strategy:
                  speedwrite()
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
                            
                            if winck(win,pl2test) and check(pl1,x) != True:
                                 
                                 AI = []
                                 AI.append(x)
                                 break
                            elif winck(win,pl1test) and check(pl2,x) != True:
                                 AI = x
                  if check(pl1,AI) or check(pl2,AI) or AI == []:   
                               AI = 1 + secrets.randbelow(9)
                               
                               while check(pl1,AI) or check(pl2,AI):
                                    AI = 1 + secrets.randbelow(9)
              except:
                  pass
          
              try:
                  AI = str(AI)[1]
                  AI = int(AI)
              except:
                  pass
     
              else:
                   if cont < 9:
                        while check(pl1,AI) or check(pl2,AI) or AI == []:
                               AI = 1 + secrets.randbelow(9)
                               
                   else:
                        pass
              cont = cont + 1
              pl2.append(AI)
def destroy():
    global a,b,c,d,e,f,g,h,i
    z = [a,b,c,d,e,f,g,h,i]
    for j in z:
        j.destroy()
        del j
    gc.collect() 
def disable():
          global a,b,c,d,e,f,g,h,i
          z = [a,b,c,d,e,f,g,h,i]
          for y in z:
            if(y.cget("text") == ""):
               y.configure(state=DISABLED)
               y.update()
def enable(Mode):
          global a,b,c,d,e,f,g,h,i
          z = [a,b,c,d,e,f,g,h,i]
          for y in z:
            if(y.cget("text") == ""):
                y.update()
                y.configure(state=NORMAL)
                y.update()
   
def gameplayOnline(num):
        global cont,pl1,pl2,socket
        cl = socket[0]
        serv = socket[1]
        pl1.append(num)
        display()
        disable()
        cl.sendall(str(num).encode("utf-8"))
        if cont < 9:
            AI = int((serv.recv(50)).decode("utf-8"),10)
            if AI not in pl2:
                pl2.append(AI)
        cont += 2
        enable(4)
def gameplayeasy(num):
        global cont,pl1,pl2
        pl1.append(num)
        AI = 1 + secrets.randbelow(9)
        while(check(pl1,AI) or check(pl2,AI)) and cont < 8:
            if cont > 8:
                break
            AI = 1 + secrets.randbelow(9)        
        pl2.append(AI)
        cont += 2
def gameplayhard(num):
         global combinations,strategy,combo,cont,pl1,pl2,a,b,c,d,e,f,g,h,i,x,comb2,comb,AI,pl1list,pl2list,trick,ptot
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
                           if check(comb,num):
                                AI.append(5)
                           elif num == 5:
                                AI.append(random.choice(com))
                           else:
                                AI.append(1 + secrets.randbelow(8))
                                while winck(pl1,AI)  or winck(pl2,AI) :   
                                       AI.append(1 + secrets.randbelow(8))
                           strategy = False
                      elif cont == 3 and (winck(pl1list,comb7) or winck(pl1list,comb6) or winck(pl1list,comb3) or winck(pl1list,comb5)): 
                           if winck(pl1list,comb3):
                                AI.append(random.choice(comb1))
                                 
                           elif winck(pl1list,comb5):
                                if check(pl1list,comb5[0]):
                                     AI.append(9)
                                     if winck(pl1,AI) or winck(pl2,AI):
                                          AI.remove(9)
                                          AI.append(3)
                                elif check(pl1list,comb5[1]):
                                     AI.append(1)
                                     if winck(pl1,AI) or winck(pl2,AI):
                                          AI.remove(1)
                                          AI.append(7)
                                elif check(pl1list,comb5[2]):
                                     AI.append(7)
                                     if winck(pl1,AI) or winck(pl2,AI):
                                          AI.remove(7)
                                          AI.append(9)
                                elif check(pl1list,comb5[3]):
                                     AI.append(3)
                                     if winck(pl1,AI) or winck(pl2,AI):
                                          AI.append(1)
                                          AI.remove(3)
                             
                           elif winck(pl1list,comb7):
                                if check(pl1list,comb7[0]):
                                     AI.append(3)
                                elif check(pl1list,comb7[1]):
                                     AI.append(9)
                                elif check(pl1list,comb7[2]):
                                     AI.append(7)
                                elif check(pl1list,comb7[3]):
                                     AI.append(1)

                                    
                           elif winck(pl1list,comb6):
                                if check(pl1list,comb6[0]) or check(pl1list,comb6[4]) :
                                     AI.append(4)
                                elif check(pl1list,comb6[1]) or check(pl1list,comb6[2]):
                                     AI.append(2)
                                elif check(pl1list,comb6[3]) or check(pl1list,comb6[6]) :
                                     AI.append(6)
                                elif check(pl1list,comb6[5]) or check(pl1list,comb6[7]):
                                     AI.append(8)
                                
                                combinations = True
                           
                      elif cont == 5 and combinations:
                           
                           if check(pl1list,comb6[0]) or check(pl1list,comb6[1]) :
                                AI.append(9)
                           elif check(pl1list,comb6[2]) or check(pl1list,comb6[3]):
                                AI.append(7)
                           elif check(pl1list,comb6[4]) or check(pl1list,comb6[5]):
                                AI.append(3)
                           elif check(pl1list,comb6[6]) or check(pl1list,comb6[7]) :
                                AI.append(1)    
                      if (winck(comb2,pl1list) or winck(comb2,pl2list)) and strategy :
                          speedwrite()
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
                                    if winck(win,pl2test) and check(pl1,x) != True:
                                         AI = []
                                         AI.append(x)
                                         break
                                    elif winck(win,pl1test) and check(pl2,x) != True:
                                         AI = x
                          if check(pl1,AI) or check(pl2,AI) or AI == []:   
                                       AI = 1 + secrets.randbelow(9)
                                       while check(pl1,AI) or check(pl2,AI):
                                            AI = 1 + secrets.randbelow(9)
                      except:
                          pass
                      try:
                          AI = str(AI)[1]
                          AI = int(AI)
                      except:
                          pass
                      else:
                           if cont < 9:
                                while check(pl1,AI) or check(pl2,AI) or AI == []:
                                       AI = 1 + secrets.randbelow(9)
                      cont = cont + 1
                      pl2.append(AI)
def gameplayhardattack(num):
         global combinations,strategy,combo,cont,pl1,pl2,a,b,c,d,e,f,g,h,i,x,comb2,comb,AI,pl1list,pl2list,trick,ptot
         trick = 0
         if cont == 1 or cont == 3 or cont == 5 or cont == 7 or cont == 9:
                 pl1.append(num)
                 pl1list = (list(permutations(pl1,2)))
                 pl2list = (list(permutations(pl2,2)))
                 cont = cont + 1
                 AI = []
                 strategy = True
                 if cont < 9:
                      if cont == 2:
                           if 1 in pl2:
                               if num == 2:#no
                                   AI.append(7)
                                   strategy = False
                               elif num == 4:#no
                                   AI.append(3)
                                   strategy = False
                               elif num == 3 or num == 7:#si
                                   AI.append(9)
                               elif num == 5:#no
                                   AI.append(random.choice([6,8,9]))
                                   strategy = False
                               elif num == 6 or num == 8:#si
                                   AI.append(5)
                               elif num == 9:#no
                                   AI.append(random.choice([3,7]))
                                   strategy = False
                           elif 3 in pl2:
                               if num == 1 or num == 9:#si
                                   AI.append(7)
                               elif num == 2:#no
                                   AI.append(9)
                                   strategy = False
                               elif num == 6:#no
                                   AI.append(1)
                                   strategy = False
                               elif num == 5:#no
                                   AI.append(random.choice([4,7,8]))
                                   strategy = False
                               elif num == 4 or num == 8:#si
                                   AI.append(7)
                               elif num == 7:#no
                                   AI.append(random.choice([1,9]))
                                   strategy = False
                           elif 7 in pl2:
                               if num == 4:
                                   AI.append(9)
                                   strategy = False
                               elif num == 8:#no
                                   AI.append(1)
                                   strategy = False
                               elif num == 1 or num == 9:#no
                                   AI.append(3)
                               elif num == 5:#no
                                   AI.append(random.choice([2,3,6]))
                                   strategy = False
                               elif num == 2 or num == 6:#si
                                   AI.append(5)
                               elif num == 3:#no
                                   AI.append(random.choice([1,9]))
                                   strategy = False
                           elif 9 in pl2:
                               if num == 6:
                                   AI.append(7)
                                   strategy = False
                               elif num == 8:#no
                                   AI.append(3)
                                   strategy = False
                               elif num == 3 or num == 7:#si
                                   AI.append(1)
                               elif num == 5:#no
                                   AI.append(random.choice([1,2,4]))
                                   strategy = False
                               elif num == 2 or num == 4:#si
                                   AI.append(5)
                               elif num == 1:#no
                                   AI.append(random.choice([3,7]))
                                   strategy = False
                           elif 5 in pl2:
                               if num == 2:
                                   AI.append(random.choice([7,9]))
                               elif num == 6:
                                   AI.append(random.choice([7,1]))
                               elif num == 4:
                                   AI.append(random.choice([3,9]))
                               elif num == 8:#si
                                   AI.append(random.choice([3,1]))
                               elif num == 1 :#no
                                   AI.append(9)
                                   strategy = False
                               elif num == 3 :#no
                                   AI.append(7)
                                   strategy = False
                               elif num == 7 :#no
                                   AI.append(3)
                                   strategy = False
                               elif num == 9 :#no
                                   AI.append(1)
                                   strategy = False
##                                
##                      elif cont == 3 and (winck(pl1list,comb7) == True or winck(pl1list,comb6) == True or winck(pl1list,comb3) == True or winck(pl1list,comb5) == True): 
##                           if winck(pl1list,comb3) == True:
##                                AI.append(random.choice(comb1))
##                                 
##                           elif winck(pl1list,comb5) == True:
##                                if check(pl1list,comb5[0]) == True:
##                                     AI.append(9)
##                                     if winck(pl1,AI) == True or winck(pl2,AI) == True:
##                                          AI.remove(9)
##                                          AI.append(3)
##                                elif check(pl1list,comb5[1]) == True:
##                                     AI.append(1)
##                                     if winck(pl1,AI) == True or winck(pl2,AI) == True:
##                                          AI.remove(1)
##                                          AI.append(7)
##                                elif check(pl1list,comb5[2]) == True:
##                                     AI.append(7)
##                                     if winck(pl1,AI) == True or winck(pl2,AI) == True:
##                                          AI.remove(7)
##                                          AI.append(9)
##                                elif check(pl1list,comb5[3]) == True:
##                                     AI.append(3)
##                                     if winck(pl1,AI) == True or winck(pl2,AI) == True:
##                                          AI.append(1)
##                                          AI.remove(3)
##                             
##                           elif winck(pl1list,comb7) == True:
##                                if check(pl1list,comb7[0]) == True:
##                                     AI.append(3)
##                                elif check(pl1list,comb7[1]) == True:
##                                     AI.append(9)
##                                elif check(pl1list,comb7[2]) == True:
##                                     AI.append(7)
##                                elif check(pl1list,comb7[3]) == True:
##                                     AI.append(1)
##
##                                    
##                           elif winck(pl1list,comb6) == True:
##                                if check(pl1list,comb6[0]) == True or check(pl1list,comb6[4]) == True :
##                                     AI.append(4)
##                                elif check(pl1list,comb6[1]) == True or check(pl1list,comb6[2]) == True:
##                                     AI.append(2)
##                                elif check(pl1list,comb6[3]) == True or check(pl1list,comb6[6]) == True :
##                                     AI.append(6)
##                                elif check(pl1list,comb6[5]) == True or check(pl1list,comb6[7]) == True:
##                                     AI.append(8)
##                                
##                                combinations = True
##                           
##                      elif cont == 5 and combinations == True:
##                           
##                           if check(pl1list,comb6[0]) == True or check(pl1list,comb6[1]) == True :
##                                AI.append(9)
##                           elif check(pl1list,comb6[2]) == True or check(pl1list,comb6[3]) == True:
##                                AI.append(7)
##                           elif check(pl1list,comb6[4]) == True or check(pl1list,comb6[5]) == True:
##                                AI.append(3)
##                           elif check(pl1list,comb6[6]) == True or check(pl1list,comb6[7]) == True :
##                                AI.append(1)    
                      if (winck(comb2,pl1list) or winck(comb2,pl2list)) and strategy :
                          speedwrite()
                          
                          
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
                                    if winck(win,pl2test) and check(pl1,x) != True:
                                         AI = []
                                         AI.append(x)
                                         break
                                    elif winck(win,pl1test) and check(pl2,x) != True:
                                         AI = x
                          if check(pl1,AI) or check(pl2,AI) or AI == []:   
                                       AI = 1 + secrets.randbelow(9)
                                       while check(pl1,AI) or check(pl2,AI):
                                            AI = 1 + secrets.randbelow(9)
                      except:
                          pass
                      try:
                          AI = str(AI)[1]
                          AI = int(AI)
                      except:
                          pass
                      else:
                           if cont < 9:
                                while check(pl1,AI) or check(pl2,AI) or AI == []:
                                       AI = 1 + secrets.randbelow(9)
                      cont = cont + 1
                      pl2.append(AI)
def display():
         global pl1,pl2,a,b,c,d,e,f,g,h,i
         for y in pl1:
             if y == 1:
                 a.configure(text="X", foreground=colorpl1)
                 a.update()
             elif y == 2:
                 b.configure(text="X", foreground=colorpl1)
                 b.update()
             elif y == 3:
                 c.configure(text="X", foreground=colorpl1)
                 c.update()
             elif y == 4:
                 d.configure(text="X", foreground=colorpl1)
                 d.update()
             elif y == 5:
                 e.configure(text="X", foreground=colorpl1)
                 e.update()
             elif y == 6:
                 f.configure(text="X", foreground=colorpl1)
                 f.update()
             elif y == 7:
                 g.configure(text="X", foreground=colorpl1)
                 g.update()
             elif y == 8:
                 h.configure(text="X", foreground=colorpl1)
                 h.update()
             elif y == 9:
                 i.configure(text="X", foreground=colorpl1)
                 i.update()
         if cont <= 8 and Vittoria != True:
             for z in pl2:
                 if z == 1:
                     a.configure(text="O", foreground=colorpl2, activeforeground=colorpl2)
                     a.update()
                 elif z == 2:
                     b.configure(text="O", foreground=colorpl2, activeforeground=colorpl2)
                     b.update()
                 elif z == 3:
                     c.configure(text="O", foreground=colorpl2, activeforeground=colorpl2)
                     c.update()
                 elif z == 4:
                     d.configure(text="O", foreground=colorpl2, activeforeground=colorpl2)
                     d.update()
                 elif z == 5:
                     e.configure(text="O", foreground=colorpl2, activeforeground=colorpl2)
                     e.update()
                 elif z == 6:
                     f.configure(text="O", foreground=colorpl2, activeforeground=colorpl2)
                     f.update()
                 elif z == 7:
                     g.configure(text="O", foreground=colorpl2, activeforeground=colorpl2)
                     g.update()
                 elif z == 8:
                     h.configure(text="O", foreground=colorpl2, activeforeground=colorpl2)
                     h.update()
                 elif z == 9:
                     i.configure(text="O", foreground=colorpl2, activeforeground=colorpl2)
                     i.update()
def callback(K,num,mode):#already tryed outside
         global turner,combo,cont,Vittoria,co,color,pl1vitt,pl2vitt,turn,a,b,c,d,e,f,g,h,i,x,ptot,AI,pl1win,pl2win,turner,Restart
         AI = []
         combo = False
         #disable btn when pressed more times and prevent other clicks
         if Vittoria:
                 cont = -2
         if check(pl1,num) or check(pl2,num):
             K.config(command=0)
         else:
             if mode == 1:
                 gameplaynormal(num)
             elif mode == 2:
               if (turner % 2) == 0:
                 gameplayhard(num)
               else:
                 gameplayhardattack(num)
             elif mode == 3:
                 gameplayeasy(num)
             elif mode == 4:
                 gameplayOnline(num)
             display()
         #win conditions (since i can't programm every possibility i used permutations)
         pl1win = list(permutations(pl1,3))
         pl2win = list(permutations(pl2,3))
         # stupid ass win screen i am too bored to rewrite it
         if winck(win,pl1win):
             Vittoria = True
             disable()
             if co == 0:
                     Restart.configure(state=DISABLED)
                     Restart.update()
                     co = -2
                     destroy()
                     win1 = tk.Toplevel()
                     try:   
                        win1.title("Winner")
                        sos = tk.Text(win1, height=7,width=25)
                        sos.grid(column=3,row=0)
                        if turn % 2 == 0:
                             pl1vitt=pl1vitt + 1 
                             sos.insert(tk.END, "You Won!")
                        Flashyflash(sos)
                        win1.destroy()
                     except:
                        win1.destroy()
                     Restart.update()
                     Restart.configure(state=NORMAL)
                     Restart.update() 
                     pl1box.configure(text=pl1vitt) #counter update
                     pl2box.configure(text=pl2vitt)
                     turner += 1
                     master.update()
                     
         elif winck(win,pl2win):
             Vittoria = True
             disable()
             if co == 0:
                     destroy()
                     if mode == 4:
                        socket[0].send(str(1 + secrets.randbelow(9)).encode("utf-8"))
                     co = -2
                     Restart.configure(state=DISABLED)
                     Restart.update()
                     win2 = tk.Toplevel()
                     
                     try:
                        win2.title("Looser")
                        sos = tk.Text(win2, height=3,width=25)
                        sos.grid(column=3,row=0)
                        if turn % 2 == 0:
                            pl2vitt=pl2vitt + 1#and this
                            sos.insert(tk.END, "You lost,keep trying")
                        Flashyflash(sos)
                        win2.destroy()
                     except:
                        win2.destroy()
                     Restart.update()
                     Restart.configure(state=NORMAL)
                     Restart.update() 
                     pl1box.configure(text=pl1vitt)
                     pl2box.configure(text=pl2vitt)
                     turner += 1
                     master.update() 
                     
                     
         if cont >= 9 and Vittoria == None:#stupid ass lose screen
             disable()
             if co == 0:
                 Restart.configure(state=DISABLED)
                 Restart.update()
                 destroy()
                 
                 if mode == 4:
                    if 11 not in pl2:
                        socket[0].send(str(11).encode("utf-8"))
                 co = -2
                 
                 loose = tk.Toplevel()
                 try :
                        loose.title("Loosers")
                        txtloose = tk.Text(loose, height=3,width=25)
                        txtloose.insert(tk.END, "Try again")
                        txtloose.grid(column=3,row=0)
                        Flashyflash(txtloose)
                        loose.destroy()
                 except:
                        loose.destroy()
                 Restart.update()
                 Restart.configure(state=NORMAL)
                 Restart.update() 
                 turner += 1     
def winck(a, b) :#check for combinations
    for x in a :
        if x in b:
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
    if b in a:
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
def checkbx3(a,b,c,d): #reset all colors
         global color,colorpl1,colorpl2,colorc,colorv,num,num2
         color='black'
         colorpl1='cyan'
         colorpl2='red'
         a.config(background='black',foreground='white',activeforeground='green')
         b.config(background='black',foreground='white',activeforeground='green')
         colorc=None
         colorv=None
         num=1
         num2=1
         master.update()
def start(l,a1,a2,mode,online=None,intnum=None): #main play and reset values for win possibilities
             global Restart,onlineturn
             Restart.configure(command=0,foreground='white',activeforeground='white')
             global turner,combinations,master,ptot,a,b,c,d,e,f,g,h,i,x,Vittoria,pl1vitt,pl2vitt,turn,end,co,cont,pl1,pl2,win,color,colorv,colorc,colorpl1,colorpl2
     #values reset
             try:
                destroy()
             except:
                pass
             if mode == 4:
                Restart.configure(state=DISABLED)
                while True:
                   num = 10 + secrets.randbelow(89)
                   socket[0].sendall(str(num).encode("utf-8"))
                   client_num = int((socket[1].recv(100)).decode("utf-8"),10)
                   if(client_num < 10 or client_num < num):
                            online = 0
                            break
                   elif client_num == num:
                            pass
                   else:
                            online = 1
                            break
                    
             if online == None and turner == None:
                turner = 1
             if mode == 4 and online != None:
                turner = online
             if colorv: #see checkbx, i need to change the backgroun color before creating those bottons
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
             texttest = ["","","","","","","","",""]
             if(intnum != None):
                texttest[intnum-1] = "O"
             combinations = False
     #adding numbers will increase games possibilities,(new tabs 4x4,5x5)(need to change also the table)
             win = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
             turn = 2
             if turn % 2 == 0 : #only god knows how this color bullshit works,but its bugless (idk why)
                     if colorc == None:
                             colorpl1='cyan'
                             colorpl2='red'
                     elif colorc:
                             colorpl1=random.choice(colorlist)
                             colorpl2=random.choice(colorlist)
                             while colorpl1 == colorpl2 or colorpl1 == color or colorpl2 == color:
                                     colorpl1=random.choice(colorlist)
                                     colorpl2=random.choice(colorlist)
                     elif colorc == False:
                             colorpl1,colorpl2 = colorpl2,colorpl1
                     pl1box.configure(foreground=colorpl1,disabledforeground=colorpl1)
                     pl2box.configure(foreground=colorpl2,disabledforeground=colorpl2)
             
             
             
             
             a = Button(master, text=texttest[0],font=('arial','20'), state=NORMAL, height = 1,width = 3,activebackground=color,background=color)
             
             a.grid(row=0 ,column=0)
             b = Button(master, text=texttest[1],font=('arial','20'), state=NORMAL, height = 1,width = 3,activebackground=color,background=color)
             
             b.grid(row=0 ,column=1)
             c = Button(master, text=texttest[2],font=('arial','20'), state=NORMAL, height = 1,width = 3,activebackground=color,background=color)
             
             c.grid(row=0 ,column=2)
             d = Button(master, text=texttest[3],font=('arial','20'), state=NORMAL, height = 1,width = 3,activebackground=color,background=color)
             
             d.grid(row=1 ,column=0)
             e = Button(master, text=texttest[4],font=('arial','20'), state=NORMAL, height = 1,width = 3,activebackground=color,background=color)
             
             e.grid(row=1 ,column=1)
             f = Button(master, text=texttest[5],font=('arial','20'), state=NORMAL, height = 1,width = 3,activebackground=color,background=color)
             
             f.grid(row=1 ,column=2)
             g = Button(master, text=texttest[6],font=('arial','20'), state=NORMAL, height = 1,width = 3,activebackground=color,background=color)
             
             g.grid(row=2 ,column=0)
             h = Button(master, text=texttest[7],font=('arial','20'), state=NORMAL, height = 1,width = 3,activebackground=color,background=color)
             
             h.grid(row=2 ,column=1)
             i = Button(master, text=texttest[8],font=('arial','20'), state=NORMAL, height = 1,width = 3,activebackground=color,background=color)
             
             i.grid(row=2 ,column=2)
             #needs developing attack mode
             if ((turner % 2) == 1):
                tmpAI = 0
                if mode == 1 or mode == 2:
                    tmpAI = 1 + secrets.randbelow(5)
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
                elif mode == 4:
                    try:
                        socket[1].settimeout(5.0)
                        tmpAI = int((socket[1].recv(50)).decode("utf-8"),10)
                        socket[1].setblocking(True)
                    except:
                        while True:
                            socket[1].setblocking(True)
                            num = 10 + secrets.randbelow(89)
                            socket[0].sendall(str(num).encode("utf-8"))
                            client_num = int((socket[1].recv(100)).decode("utf-8"),10)
                            if(client_num < 10 or client_num < num):
                                     online = 0
                                     break
                            elif client_num == num:
                                     pass
                            else:
                                     online = 1
                                     break
                        if ((online % 2) == 1):
                            tmpAI = int((socket[1].recv(50)).decode("utf-8"),10)
                else:
                    tmpAI = 1 + secrets.randbelow(9)
                pl2.append(tmpAI)
                cont += 1
                for z in pl2:
                    if z == 1:
                        a.configure(text="O", foreground=colorpl2, activeforeground=colorpl2,command=0)
                    elif z == 2:
                        b.configure(text="O", foreground=colorpl2, activeforeground=colorpl2,command=0)
                    elif z == 3:
                        c.configure(text="O", foreground=colorpl2, activeforeground=colorpl2,command=0)
                    elif z == 4:
                        d.configure(text="O", foreground=colorpl2, activeforeground=colorpl2,command=0)
                    elif z == 5:
                        e.configure(text="O", foreground=colorpl2, activeforeground=colorpl2,command=0)
                    elif z == 6:
                        f.configure(text="O", foreground=colorpl2, activeforeground=colorpl2,command=0)
                    elif z == 7:
                        g.configure(text="O", foreground=colorpl2, activeforeground=colorpl2,command=0)
                    elif z == 8:
                        h.configure(text="O", foreground=colorpl2, activeforeground=colorpl2,command=0)
                    elif z == 9:
                        i.configure(text="O", foreground=colorpl2, activeforeground=colorpl2,command=0)
                display()
             if online == 1:
                online = 0
             else:
                online = 1 
             a.configure(command=lambda :callback(a,1,mode))
             b.configure(command=lambda :callback(b,2,mode))
             c.configure(command=lambda :callback(c,3,mode))
             d.configure(command=lambda :callback(d,4,mode))
             e.configure(command=lambda :callback(e,5,mode))
             f.configure(command=lambda :callback(f,6,mode))
             g.configure(command=lambda :callback(g,7,mode))
             h.configure(command=lambda :callback(h,8,mode))
             i.configure(command=lambda :callback(i,9,mode))
             x = [a,b,c,d,e,f,g,h,i]
             Restart.configure(command=lambda :start(master,pl1box,pl2box,mode))
             l.geometry("280x200")
def checkbx4(a,b): #reset and reconfigure counter 
             global pl1vitt,pl2vitt
             pl1vitt=0
             pl2vitt=0
             a.configure(text=pl1vitt)
             b.configure(text=pl2vitt)
             master.update()
def out():
    global pl1vitt,pl1box,pl2vitt,pl2box,retur,master,socket
    pl1vitt=0
    pl2vitt=0
    pl1box.config(text=pl1vitt)
    pl2box.config(text=pl2vitt)
    master.destroy()
    master.quit()
    
            
 #other buttons (see the text configured)
def main(mode,sock=None,sock1=None,turnation=None):
     global Restart,master,pl1box,pl2box,socket,onlineturn
     onlineturn = turnation
     if(turnation == None):
        turnation = 0
     #just start tk
     socket = [sock,sock1]
     
     master = tk.Toplevel()
     #w = Frame(master)
     master.title("Tick tac toe")
     master.configure(background='black')
     master.geometry("280x200")
     master.resizable(False,False)
     Restart = Button(master,text="Restart", command= lambda :start(master,pl1box,pl2box,mode,turnation) ,state=NORMAL,background='black',activebackground='black',foreground='white',activeforeground='white')
     Restart.place(height=20, width=50 ,y=15, x=200)#the restart button
     pl1box = Button(master, text=pl1vitt,foreground='cyan',disabledforeground='cyan',state=DISABLED,activebackground='black',background='black' )
     pl1box.place(height=30 ,width=30,y=169, x=15)
     pl2box = Button(master, text=pl2vitt,foreground='red',disabledforeground='red',state=DISABLED,activebackground='black',background='black' )
     pl2box.place(height=30 ,width=30,y=169, x=130)
     checkbox4 = Button(master, text="reset counter", font=('italic','7'),foreground='white',activeforeground='white',command= lambda :checkbx4(pl1box,pl2box) ,state=NORMAL,activebackground='black',background='black' )
     checkbox4.place(y=135, x=200)
     checktext = Button(master,text="random background",command= lambda :checkbx(checktext),font=('italic','7') ,state=NORMAL,background="black",foreground='white',activebackground='Black',activeforeground='white')
     checktext.place(y=60, x=186)
     checktext2 = Button(master,text="random player color",font=('italic','7'),command= lambda :checkbx2(checktext2) ,state=NORMAL,foreground='white',background="black",activebackground='Black',activeforeground='white')
     checktext2.place(y=80, x=186)
     checkbox3 = Button(master, text="reset colors", font=('italic','7'),foreground='white',activeforeground='white',command= lambda :checkbx3(checktext,checktext2,Restart,checkbox3) ,state=NORMAL,activebackground='black',background='black' )
     checkbox3.place(y=110, x=200) #the reset color botton
     start(master,pl1box,pl2box,mode,turnation)
     master.protocol("WM_DELETE_WINDOW", out)
     master.update()
     master.mainloop()

     
     


