import poplib
import string
import StringIO, rfc822
import smtplib
import urllib2
import re
import time
import os
import sys

lastSubj = ""

def readMail():
	server = poplib.POP3_SSL("pop.gmail.com")
	server.user("moriartie.kr@gmail.com")
	server.pass_("gabs2gab")

	global lastSubj
	resp, items, octets = server.list()
		
	try:
		t=items[0]
	except:
		return	lastSubj
	else:	
		id, size = string.split(items[0])
		resp, text, octets = server.retr(id)
		text = string.join(text, "\n")
		file = StringIO.StringIO(text)
		message = rfc822.Message(file)	
		subj = message['Subject']
		lastSubj = subj	
		return subj

def readMail2():
	pop3_host = 'pop.gmail.com'
	pop3_user = 'moriartie.kr@gmail.com'
	pop3_pass = 'gabs2gab'
	
	pop3_mail = poplib.POP3_SSL(pop3_host)
	pop3_mail.user(pop3_user)
	pop3_mail.pass_(pop3_pass)
	pop3_stat = pop3_mail.stat()
	
	latest_email = pop3_mail.retr(1)
	
	return latest_email
	
def sendMail(message):
	toaddr = "gabrieainha@gmail.com"
	fromaddr = "moriartie.kr@gmail.com"
	username = "moriartie.kr@gmail.com"
	password = "gabs2gab"
	msg = "\r\n".join([
	"From: moriartie.kr@gmail.com",
	"To: "+toaddr,
	"Subject: Bot Message",
	"",
	message
	])
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr,toaddr,msg)

#date = message['Date']
#raw_txt = message.fp.read()
#start = "<div dir=\"ltr\">"
#end = "<"
#txt = raw_txt.split(start)[1].split(end)[0]
#sender = message['From']
