from itertools import count
import pyautogui
import time
time.sleep(5)
count=0
while count<=5:
    pyautogui.typewrite("mohi" +str(count))
    pyautogui.press("enter")
    count=count+1