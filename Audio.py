import pyautogui
import os
import time


pyautogui.press('win')
time.sleep(1)
pyautogui.write('spotify')
time.sleep(1)
pyautogui.press('enter')

time.sleep(9)

pyautogui.hotkey('ctrl','l')
time.sleep(3)
pyautogui.write('Desi Kalakaar', interval=0.2)

for key in ['enter', 'pagedown','tab','enter','enter']:
    time.sleep(2)
    pyautogui.press(key)