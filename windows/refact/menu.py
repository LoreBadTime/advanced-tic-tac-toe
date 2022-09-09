import socket
import asyncio
from typing import final
import webbrowser
import tkinter as tk
import local3x3,main

def startclient(sock,tupl):
    sock.setblocking(True)
    print("client in connect\n")
    sock.connect(tupl)
    print("client connected\n")

def startserver(sock_server,tupl,lista):

    sock_server.setblocking(True)
    sock_server.bind(tupl)
    sock_server.listen()
    print("server in accept\n")
    client, address = sock_server.accept()
    lista.append(client)

async def connect_to_peer(lista_input):
    CL_ADDRESS = "192.168.43.82" #indirizzo IP
    MY_ADDRESS = ""
    MY_PORT = 11000
    lista = []
    try:
        sock_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock_cl = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        await asyncio.gather(
                asyncio.to_thread(startserver,sock_server,(MY_ADDRESS,MY_PORT),lista),
                asyncio.to_thread(startclient,sock_cl,(CL_ADDRESS,MY_PORT)))
        server = sock_server
        client = lista[0]

        lista_input.append(sock_cl)
        lista_input.append(client)
        lista_input.append(sock_server)
        
    except:    
        sock_cl.close()
        sock_server.close()
        raise ValueError('Errore connessione al peer')
    


def mainmenu():
    global root,pl1vitt,pl2vitt,done,aa,bb,cc,dd,client
    global done
    done = False
    selection = 0

    def callback(selection):
        global done
        print(done)
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
                lista_socket = []
                try:
                    asyncio.run(connect_to_peer(lista_socket))
                    main.main(4,lista_socket[0],lista_socket[1])
                    lista_socket[0].close()
                    lista_socket[2].close()
                except:
                    raise ValueError('Errore connessione al peer')
                done = False
        return done

        
    def openwebpage():
        webbrowser.open('https://github.com/LoreBadTime/tkinter-tic-tac-toe', new=2)


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
def online():
                lista_socket = []
                try:
                    asyncio.run(connect_to_peer(lista_socket))
                    main.main(4,lista_socket[0],lista_socket[1],lista_socket[3],lista_socket[4])
                    lista_socket[0].close()
                    lista_socket[2].close()
                except:
                    raise ValueError('Errore connessione al peer')
#online()