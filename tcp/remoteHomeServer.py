#!/usr/bin/python
import os
import sys
import socket
import semtics
import cmde
from time import sleep
from mail import readMail
from mail import sendMail
from random import randint

lastMessage = readMail()

def Server():
    host = 'localhost'
    port = 5001

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('',port))

    print("tcp server started ("+str(sys.argv[1])+")")
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

def Mail():
    print("mail server started")
    print("")

    while True:
        if(chkNewMail()):
            message = readMail()
            isCommand, outp = cmdInput(message)
            if(isCommand):
                print("server: "+outp)
                sendMail(outp)
            else:
                print "from client: "+message
                sendMail("received") 
        countdown(11)                      

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

def chkNewMail():
    global lastMessage
    newMessage = readMail()
    if(newMessage != lastMessage):
        print("new mail")
        lastMessage = newMessage
        return True
    else:
        print("no new mail")
        return False

def countdown(minutes):
    count = 0
    while(count<=minutes):
        print("updating in "+str(minutes-count)+" minute(s)")
        sleep(60)
        count += 1

if __name__ == '__main__':
    if(sys.argv[1]=='--server'):
        Server()
    elif(sys.argv[1]=='--mail'):
        Mail()
    else:
        print("")
        print("Input one of the following options as argument")
        print("  --server")
        print("  --mail")    
        print("")
