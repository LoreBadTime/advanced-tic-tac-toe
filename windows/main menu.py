import webbrowser
import tkinter as tk
import local3x3,vs_computer_easy,vs_computer_hard,vs_computer_normal
global root
selection = 0
root = tk.Tk()
root.title("Tick tac toe menu")
root.configure(background='black')
root.geometry("204x180")
root.resizable(False,False)
txt1="Local Multiplayer"
txt2="Against Computer Easy"
txt3="Against Computer Hard"
txt4="Against Computer Normal"
def openwebpage():
    webbrowser.open('https://github.com/LoreBadTime/tkinter-tic-tac-toe', new=2)



def callback(num):
    global selection
    selection = num
    root.destroy()

a = tk.Button(root, text=txt1, height = 1,width = 25,activebackground='black',background='black',foreground='white')
a.configure(command=lambda :callback(1))
a.place(x=10 ,y=20)
b = tk.Button(root, text=txt2, height = 1,width = 25,activebackground='black',background='black',foreground='white')
b.configure(command=lambda :callback(2))
b.place(x=10 ,y=50)                
c = tk.Button(root, text=txt3, height = 1,width = 25,activebackground='black',background='black',foreground='red')
c.configure(command=lambda :callback(3))
c.place(x=10 ,y=110)
d = tk.Button(root, text="Github", height = 1,width = 25,activebackground='black',background='black',foreground='cyan')
d.configure(command=lambda :openwebpage())
d.place(x=10 ,y=140)
e = tk.Button(root, text=txt4, height = 1,width = 25,activebackground='black',background='black',foreground='orange')
e.configure(command=lambda :callback(4))
e.place(x=10 ,y=80)
root.mainloop()

if selection == 1:
    local3x3.local()
elif selection == 2:
    vs_computer_easy.vsAI()
elif selection == 3:
    vs_computer_hard.vsAIh()
elif selection == 4:
    vs_computer_normal.vsAIn()  

