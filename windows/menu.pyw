import socket
import asyncio
import webbrowser
import tkinter as tk
from tkinter import DISABLED, messagebox
import local3x3,main

def startclient(sock,tupl):
    sock.append(socket.create_connection(tupl))
    sock[0].setblocking(True)
    print("connected\n")

def startserver(sock_server,tupl,lista):

    if socket.has_dualstack_ipv6():
        sock_server = socket.create_server(tupl, family=socket.AF_INET6, dualstack_ipv6=True)
    else:
        sock_server = socket.create_server(tupl)
    sock_server.setblocking(True)
    sock_server.listen()
    client, address = sock_server.accept()
    lista.append(client)

async def connect_to_peer(lista_input,IPAddress,Ipversion):
    CL_ADDRESS = IPAddress#IPAddress
    MY_ADDRESS = ""
    MY_PORT = 11000
    lista = []
    socket.setdefaulttimeout(10)
    Ipv = socket.AF_INET
    upla_serv = (MY_ADDRESS,MY_PORT)
    upla_cl = (CL_ADDRESS,MY_PORT)
    if Ipversion:
        Ipv = socket.AF_INET6
        MY_ADDRESS = "::"
        upla_serv = (MY_ADDRESS,MY_PORT)
    try:
        sock_server = None
        sock_cl = []

        await asyncio.gather(
                asyncio.to_thread(startserver,sock_server,upla_serv,lista),
                asyncio.to_thread(startclient,sock_cl,upla_cl))
        lista_input.append(sock_cl[0])
        lista_input.append(lista[0])
        lista_input.append(sock_server)
    except Exception as err:    
        sock_cl[0].close()
        sock_server.close()
        raise ValueError('Errore connessione al peer' + str(err))

def check(string):
    if string == "":
        return False
    lista = []
    tmp = ""
    i = 0
    if getversion(string):
        for el in string:
            if(el == ":"):
                lista.append(tmp)
                tmp = ""
                i = 0
            else:
                tmp = tmp + el
                i += 1
                if i > 4:
                    return False
        i = 0
        for el in lista:
            if(el != ""):
                i += 1
                if int(el,16) > int("ffff",16):
                    return False
        if i > 4:   
            return False 
        return True
    else:
        for el in string:
            if(el == "."):
                lista.append(tmp)
                tmp = ""
                i = 0
            else:
                tmp = tmp + el
                i += 1
                if i > 3:
                    return False
        i = 0
        for el in lista:
            i += 1
            if int(el,10) > 255:
                return False
        if i > 4:   
            return False 
        return True

def getversion(string):
    return (":" in string)

def callback(selection,IPAdd=None,window=None,Button_connect=None):
        global done
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
            elif selection == 5:
                done = True
                IPwindow = tk.Toplevel()
                IPwindow.configure(background='black')
                IPwindow.geometry("170x120")
                IPwindow.title("Remote Play")
                txt = tk.Text(IPwindow,bg='black',fg='white',borderwidth = 0, highlightthickness = 0)
                txt.insert(tk.END, "Insert Opponent IP")
                txt.config(state=DISABLED)
                txt.place(x=10 ,y=10)
                txtInput = tk.Entry(IPwindow)
                txtInput.place(x=10 ,y=40)
                button = tk.Button(IPwindow, text="Connect", command=lambda: callback(6,txtInput.get(),IPwindow,button),activebackground='black',background='black',foreground='green')
                button.place(x=10 ,y=70)
                done = False
            elif selection == 6:
                done = True
                if check(IPAdd):
                    lista_socket = []
                    try:
                        Button_connect.configure(text="Connecting...",foreground='cyan')
                        Button_connect.update()
                        asyncio.run(connect_to_peer(lista_socket,IPAdd,getversion(IPAdd)))
                        main.main(4,lista_socket[0],lista_socket[1],None,window)
                        lista_socket[0].close()
                        lista_socket[2].close()
                    except Exception as err:
                        try:
                           lista_socket[0].close()
                           lista_socket[2].close()
                        except:
                            pass
                        messagebox.showerror('Errore di connessione', 'Connessione interrotta o impossibile stabilire la connessione' + str(err))
                        window.destroy()
                else:
                    Button_connect.configure(text="Invalid IP address",foreground='red')
                done = False
        return done

        
def openwebpage():
        webbrowser.open('https://github.com/LoreBadTime/tkinter-tic-tac-toe', new=2)


def mainmenu():
    global root,pl1vitt,pl2vitt,done,aa,bb,cc,dd,client
    global done
    done = False
    root = tk.Tk()
    root.title("Tick tac toe menu")
    root.configure(background='black')
    root.geometry("204x210")
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
    ff = tk.Button(root, text="Remote Play", height = 1,width = 25,activebackground='black',background='black',foreground='green')
    ff.place(x=10 ,y=140)
    dd = tk.Button(root, text="Github", height = 1,width = 25,activebackground='black',background='black',foreground='cyan')
    dd.configure(command=lambda :openwebpage())
    dd.place(x=10 ,y=170)
    ee = tk.Button(root, text=txt4, height = 1,width = 25,activebackground='black',background='black',foreground='orange')
    aa.configure(command=lambda :callback(1))
    bb.configure(command=lambda :callback(2))
    cc.configure(command=lambda :callback(3))
    ee.configure(command=lambda :callback(4))
    ff.configure(command=lambda :callback(5))
    ee.place(x=10 ,y=80)
    root.mainloop()

mainmenu()
