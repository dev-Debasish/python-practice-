import pyautogui
import time

pyautogui.click(x=1317,y=1043,interval=0.1)   
time.sleep(1)
pyautogui.click(x=396,y=400,interval=0.1)   
# pyautogui.press("enter")
n=10
while n>1:
    pyautogui.press("G")
    time.sleep(0.001)
    pyautogui.press("A")
    time.sleep(0.001)
    pyautogui.press("N")
    time.sleep(0.001)
    pyautogui.press("D")
    time.sleep(0.001)
    pyautogui.press("U")
    time.sleep(0.001)
    pyautogui.press("enter")
    time.sleep(0.1)
    n-=1

pyautogui.press("enter")





