#!/usr/bin/python
import os
import sys
import socket
import semtics
import cmde
from random import randint

def Main():
    if(len(sys.argv)==1):
        sys.argv.append(5001)
    host = 'localhost'
    port = sys.argv[1]

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('',port))

    print("server started ("+str(socket.gethostbyname(socket.gethostname()))+")")
    s.listen(1)
    c, addr = s.accept()
    print "Connection from: " + str(addr)
    while True:
        data = c.recv(1024)
        if not data:
            break
        isCommand, outp = cmdInput(str(data))
        if(isCommand):
            print("server: "+outp)
            c.send(outp)
        else:
            print "from connected user: " + str(data)
            c.send("received")
    c.close()

def cmdInput(str_inputed):
    str_inputed = str_inputed.split()
    cmdList = cmde.loadCommandsFromFile('commands.txt')
    winner = semtics.findWinner(str_inputed, cmdList)
    #exit
    if(winner==0):
        print("server shutdown by command from client")
        sys.exit()
    #test
    elif(winner==1):
        return (True, "test command received")
    #lock pc
    elif(winner==2):
        os.system("gnome-screensaver-command -l")
        return (True, "lock command received")
    #rnd
    elif(winner==3):
        return (True, str(randint(0,9)))
    #salute
    elif(winner==4):
        return (True, "hello")
    #cmd list
    elif(winner==5):
        return (True, "test; lock computer; tell me a random number; hi; command list;")
    #not a command	
    elif(winner==(-1)):
	return(False, " ")
    else:
        return (False, " ")

if __name__ == '__main__':
    Main()
