import sys
sys.path.append("/home/raghav/.local/lib/python3.9/site-packages/")
import threading
from threading import Event
import keyboard
import time
import curses
import socket
import keycodes as HexCodes
import keyarr as KeyStates
sys.path.append("/opt/tinypilot/app/")
import hid.keycodes as agh
import pins

stopped = False
file = open("/home/raghav/stream.txt", "w")
HOST = "127.0.0.1"
PORT = 65432
stopevent = Event()

SavedStrokes = []
recording = 0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	class myThread (threading.Thread):
		def sendStroke(key, index):
			mods = 0
			if(myThread.CheckPressed('ctrl', index) == 1):
				mods = mods +1 #1
			if(myThread.CheckPressed('shift', index) == 1):
				mods = mods+2
			if(myThread.CheckPressed('alt', index) == 1):
				mods = mods+4
				print("alted")
			if(myThread.CheckPressed('command', index) == 1):
				mods = mods + 8
				print('comanded')
			file.write("\nmods: {:b}".format(mods))
			s.sendall(b'p' + bytes.fromhex(HexCodes.reference[key]) + mods.to_bytes(1, 'little'))
			file.write("\nsent {}".format(key))
			file.write("\nin form: {}\n".format(b'p' + bytes.fromhex(HexCodes.reference[key])))
		def CheckPressed(mod, index):
			global SavedStrokes
			idx = index
			while idx >= 0 and SavedStrokes[idx][1:len(SavedStrokes[idx])] != mod:
				idx = idx - 1
			if idx < 0 or SavedStrokes[idx][0] == 'r':
				return 0
			return 1
		def PlayBack():
			global SavedStrokes
			for index, val in enumerate(SavedStrokes):
				key = val[1:len(val)]
				if val[0] == 'p':
					myThread.sendStroke(key, index)

		def __init__(self, threadID):
			threading.Thread.__init__(self)
			self.threadID = threadID
		def run(self):
			global recording
			global SavedStrokes
			while True:
				if stopevent.is_set():
					break
				pin29 = pins.CheckPin(29)
				pin31 = pins.CheckPin(31)
				if pin29 == 1:
					if recording == 0:
						pins.SetLight(0)
						recording = 1
						print("began")
						SavedStrokes = []
					else:
						pins.SetLight(1)
						recording = 0
						print("ended")
				if pin31 == 1:
					print(SavedStrokes)
					myThread.PlayBack()


	class bufferClearThread (threading.Thread):
		def __init__(self, threadID):
			threading.Thread.__init__(self)
			self.threadID=threadID
		def run(self):
			curses.initscr()
			while (stopevent.is_set() == False):
				curses.flushinp()
#				print("hello")
			curses.nocbreak()
			stdscr.keypad(False)
			curses.echo()
			curses.endwin()
	def set_bit(value, bit):
		return value | (1<<bit)
	def clear_bit(value, bit):
		return value & ~(1<<bit)
	def key_press(key):
		mods = 0
		if(KeyStates.getKey('ctrl') == 1):
			mods = mods +1  # 1
			print('ctrl')
		if(KeyStates.getKey('shift') == 1):
			mods = mods + 2
			print('shift')
		if(KeyStates.getKey('alt') == 1):
			mods = mods + 4
			print('alt')
		if(KeyStates.getKey('command') == 1):
			mods = mods + 8
			print('command')
		file.write("\nmods: {:b}".format(mods))
#		print(mods)
		s.sendall(b'p' + bytes.fromhex(HexCodes.reference[key]) + mods.to_bytes(1, 'little'))
		file.write("\nsent {}".format(key))
		file.write("\nin form: {}\n".format(b'p' + bytes.fromhex(HexCodes.reference[key])))
	def key_release(key):
		s.sendall(b'r' + bytes.fromhex(HexCodes.reference[key]))
		file.write("released {}".format(key))
		file.write("\nin form: {}\n".format(b'r' + bytes.fromhex(HexCodes.reference[key])))
	x = 0
	x |= 1
	print(x)
	x|= 0
	print(x)
	x|= 1
	print(x)
	print(type(0b00000000))
	s.connect((HOST, PORT))
	Thread1 = myThread(1)
	Thread1.start()
	pins.SetLight(1)
	while stopped == False:
		recording
		SavedStrokes
		event = keyboard.read_event()
		val = event.name
		if event.scan_code == 125:
			val = 'command'
		if event.scan_code == 12:
			val = '-'
		op = event.event_type
		print(event.scan_code)
		if op == keyboard.KEY_DOWN:
			if KeyStates.getKey(val) == 0 or (val != 'shift' and val != 'ctrl' and val != 'alt' and val != 'command'):
				if(recording == True):
					SavedStrokes.append('p' + val)
				key_press(val)
				KeyStates.reference[val] = 1
				if(val == 'end'):
					stopped = True
					stopevent.set()
					pins.SetLight(0)
				if(val == 'insert'):
					Thread2 = bufferClearThread(2)
					Thread2.start()
		elif op == keyboard.KEY_UP:
#			if KeyStates.getKey(val) == 1:
				if(recording == True):
					SavedStrokes.append('r' + val)
#				key_release(val)
				KeyStates.reference[val] = 0


#			if stopped == True:
#				break


#		Thread1 = bufferClearThread(1)
#		Thread1.start()
#		while(stopped==False):
#			for val in reference:
#				if(keyboard.is_pressed(val)):
#					if(reference[val]==0):
#						key_press(val)
#						reference[val]=1
#				else:
#					if(reference[val]==1):
##						key_release(val)
#						reference[val]=0
#		file.close()
#
#def key_press(key):
#		file.write("p{}".format(key))
#		file.write(";00000000\n")
#def key_release(key):
#		file.write("r{}\n".format(key))
#		if(key == 'esc'):
#			global stopped
#			stopped = True
#			file.write("c\n")
#			file.close()
#
#
