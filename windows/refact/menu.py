import webbrowser
import tkinter as tk
import local3x3,main
def mainmenu():
    global root,pl1vitt,pl2vitt,done,aa,bb,cc,dd
    global done
    done = False
    selection = 0

    def callback(selection):
        global done
        print(done)
        root.destroy()
        if done == False:
            if selection == 1:
                done = True
                local3x3.local()
                done = False
            elif selection == 2:
                done = True
                main.main(3)
                done = False
            elif selection == 3:
                done = True
                main.main(2)
                done = False
            elif selection == 4:
                done = True
                main.main(1)
                done = False
        
        return done

        
    def openwebpage():
        webbrowser.open('https://github.com/LoreBadTime/tkinter-tic-tac-toe', new=2)


    root = tk.Tk()
    root.title("Tick tac toe menu")
    root.configure(background='black')
    root.geometry("204x180")
    root.resizable(False,False)
    txt1="Local Multiplayer"
    txt2="Against Computer Easy"
    txt3="Against Computer Hard"
    txt4="Against Computer Normal"
    aa = tk.Button(root, text=txt1, height = 1,width = 25,activebackground='black',background='black',foreground='white')
    aa.place(x=10 ,y=20)
    bb = tk.Button(root, text=txt2, height = 1,width = 25,activebackground='black',background='black',foreground='white')
    bb.place(x=10 ,y=50)                
    cc = tk.Button(root, text=txt3, height = 1,width = 25,activebackground='black',background='black',foreground='red')
    cc.place(x=10 ,y=110)
    dd = tk.Button(root, text="Github", height = 1,width = 25,activebackground='black',background='black',foreground='cyan')
    dd.configure(command=lambda :openwebpage())
    dd.place(x=10 ,y=140)
    ee = tk.Button(root, text=txt4, height = 1,width = 25,activebackground='black',background='black',foreground='orange')
    aa.configure(command=lambda :callback(1))
    bb.configure(command=lambda :callback(2))
    cc.configure(command=lambda :callback(3))
    ee.configure(command=lambda :callback(4))
    ee.place(x=10 ,y=80)
    root.mainloop()


