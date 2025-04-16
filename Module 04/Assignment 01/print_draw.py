import pyautogui
import time

N = int(input())
star = 1

for i in range(1,N+1):
    line = '#' * star
    pyautogui.typewrite(line)
    pyautogui.press('Enter')
    star += 1


