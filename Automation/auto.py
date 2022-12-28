import os
import pyautogui as pg
import time
os.system("start \"\" https://www.freecodecamp.org/learn/2022/responsive-web-design/#learn-css-colors-by-building-a-set-of-colored-markers")

# time.sleep(6)

# pyautogui.scroll(200)

time.sleep(6)
pg.leftClick(1228, 471,duration=1) 
time.sleep(2)
pg.moveTo(500,671,duration=1)
time.sleep(1)
pg.hotkey('ctrl', 'a')
pg.hotkey('ctrl', 'c')

os.system("start \"\" https://www.freecodecamp.org/learn/2022/responsive-web-design/learn-css-colors-by-building-a-set-of-colored-markers/step-9")

time.sleep(3)

pg.moveTo(500,671,duration=1)

time.sleep(2)
pg.hotkey('ctrl', 'a')

pg.hotkey('ctrl', 'v')

pg.leftClick(440, 784,duration=1)


