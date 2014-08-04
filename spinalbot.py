#!/usr/bin/env python

from threading import Thread
import time
import praw
import sys

done = False
username = ' '
password = ' '

def main():
	global username
	global password
	username = sys.argv[1]
	password = sys.argv[2]
	start_listener()
	console()

def start_listener():
	listener = Thread(target = listener_thread)
	listener.setDaemon(True)
	listener.start()

def console():
	while not done:
		cmd = raw_input('>')
		if cmd:
			process_command(cmd)

def process_command(cmd):
	global done
	toks = cmd.split()
	if toks[0] == 'exit':
		done = True
	elif toks[0] == 'accept':
		accept(toks[1:])
	else:
		print 'Command not recognized.'

def accept(names):
	r = get_session(username, password)
	for name in names:
		try:
			r.send_message(name, 'Welcome!', 'Welcome to Spinalcraft! I just added you, [have fun!](/r/spinalcraft)')
		except (praw.errors.InvalidUser):
			print 'User does not exist!'

def get_session(user, pwd):
	r = praw.Reddit('a')
	r.login(username = user, password = pwd)
	return r

def listener_thread():
	r = get_session(username, password)

	while True:
		unread = r.get_unread()	
		for message in unread:
			r.send_message('DoctorSauce', 'Application from ' + message.author.name, message)
			message.mark_as_read()
			message.remove()
		time.sleep(3)

if __name__ == '__main__':
	main()
