import pyautogui as pag
import os
import  time

#
pag.press('win')
pag.typewrite('cmd')
pag.press('enter')
time.sleep(1)
pag.typewrite('cd Desktop\project')
pag.press('enter')
time.sleep(1)
pag.typewrite('python voice_base.py')
pag.press('enter')
time.sleep(7)
os.system('python mouse-cursor-control.py')

