import threading
import time
import traceback
import socket
import socket_api
from pathlib import Path

reference = dict()
stopped = False
HOST = "127.0.0.1"
PORT = 65432
file2 = open("/home/raghav/testing-ground/log.txt", "w")
file2.write("help")
file2.flush()


class myThread (threading.Thread):
	def __init__(self, threadID):
		threading.Thread.__init__(self)
		self.threadID = threadID
	def run(self):
		file2.write("beginning logger")
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			def process(input):
				keyboard_path = Path("""/dev/hidg0""")
				file2.write("\nreceived: {}".format(input))
				file2.write("\nlength: {}".format(len(input)))
				op = input[0]
				file2.write("\nop: {}".format(op))
				file2.write("\nkey: {}".format(input[1]))
				key = input[1]
				mods = input[2]
#					file2.write("\nkey: {}\n".format(int(key, 16)))
				if(op == 112):
					try:
						socket_api.fake_keyboard.send_keystroke(keyboard_path, mods, key)
						file2.write("Key was successfully sent!")
					except:
						file2.write("{}".format(traceback.format_exc()))
				elif(op == 114):
					socket_api.fake_keyboard.release_keys(keyboard_path)
				file2.write("\nJust wrote the key: {}\n".format(str(key)))
				file2.flush()

			s.bind((HOST, PORT))
			s.listen()
			while True:
				conn, addr = s.accept()
				with conn:
					file2.write("connected")
					file2.flush()
					while True:
						data = conn.recv(3)
						if data == b'esc':
							file2.write("closing server")
							file2.flush()
							break
						if not data:
							file2.write("closing server due to empty packet")
							file2.flush()
							break
						try:
							process(data)
						except:
							file2.write("{}".format(traceback.format_exc()))
							file2.flush()
