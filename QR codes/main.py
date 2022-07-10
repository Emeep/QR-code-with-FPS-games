import time
import ait  #autoit
import win32api, win32con
import pyautogui
from pynput.mouse import Button, Controller


mouse = Controller()
target_colour = (2, 144, 168)


def aim():
    img = pyautogui.screenshot(region=(802, 362, 315, 355))  # for every 10 decreased, increase by 5
    for x in range(img.width):
        for y in range(img.height):
            if img.getpixel((x, y)) == target_colour:
                apx = x - 157  # for every 10 W decreased, decrease by 5
                apy = y - 177  # for every 10 H decreased, decrease by 5
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, apx, apy - 10)
                ait.click()
                time.sleep(0.01)
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -apx, -apy + 10)
                aim()


while True:
    a = win32api.GetKeyState(0x26)  # up arrow key
    if a < 0:
        break


aim()

