import pyautogui 
import webbrowser as wb
import time
wb.open("web.whatsapp.com")
time.sleep(10)
for i in range(1000):
    pyautogui.press("hey buddy this is a test message")
    pyautogui.press("enter") 
    pyautogui.press("I am sending this message using python script")
    pyautogui.press("enter")
    pyautogui.press("I hope you are doing well")
    pyautogui.press("enter")
   


























