from tkinter import ttk
import time
import pyautogui

# import tkinter as tk
# from tkinter import * 
# root1 = tk.Tk()
# root1.title("Your Playlist")
# root1.configure(bg='black')

# pred = tk.Button(root1, text="Play",
#                 fg="white", bg="black",
#                 width=20, height=3, activebackground="Red",
#                 font=('times', 15, ' bold '))
# pred.place(x=200, y=500)
# root1.mainloop()

pyautogui.press('win')
time.sleep(3)
pyautogui.write('spotify')
time.sleep(1)
pyautogui.press('enter')

time.sleep(9)

row= ["Din Shagna Da", "Daytona","Stars"] 
#for song in list(row):
for curr in range(len(list(row))):
    print (curr)
    pyautogui.hotkey('ctrl','l')
    time.sleep(3)
    pyautogui.write(f"{list(row)[curr]}", interval=0.2)

    for key in ['enter', 'pagedown','tab','enter','enter']:
        time.sleep(2)
        pyautogui.press(key)
    time.sleep(2)