import win32api, win32con
from pynput.keyboard import Key, Controller

keyboard = Controller()

text_keyboard = [
['move_forward', 'w'],
['move_backward', 's'],
['move_left', 'a'],
['move_right', 'd']
]

text_mouse = [
['mouse_up', 0, -1],
['mouse_down', 0, 1],
['mouse_left', -1, 0],
['mouse_right', 1, 0]
]

text_action = [
['left_click', win32con.MOUSEEVENTF_LEFTDOWN],
['right_click', win32con.MOUSEEVENTF_RIGHTDOWN],
['stop_left', win32con.MOUSEEVENTF_LEFTUP],
['stop_right', win32con.MOUSEEVENTF_RIGHTUP]
]

keys = ['w', 'a', 's', 'd']

print('asdg')

alrp = 'sadfasdfasf'
alrc = 'shasjfopgdu'

sensitivity = 50

def inputs(text):
    global text_keyboard
    global alrp
    global sensitivity
    global keys

    if text == 'release':
        for k in keys:
            keyboard.release(k)

    for tke in text_keyboard:
        if tke[0] == text:
            if text != alrp:
                for tk in text_keyboard:
                    if text == str(tk[0]) and text != alrp:
                        print('initial = ' + alrp)
                        alrp = str(tk[0])
                        print('after = ' + alrp)
                        keyboard.press(tk[1])
                    
                        for k in keys:
                            if k != tk[1]:
                                keyboard.release(k)
    
    for tmo in text_mouse:
        if tmo[0] == text:
            for tm in text_mouse:
                if text == str(tm[0]):
                    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, tm[1] * sensitivity, tm[2] * sensitivity)
    
    for tac in text_action:
        if tac[0] == text:
            if text != alrc:
                for ta in text_action:
                    if text == str(ta[0]) and text != alrc:
                        print('initial = ' + alrc)
                        alrp = str(ta[0])
                        print('after = ' + alrc)
                        win32api.mouse_event(ta[1], 0, 0, 0, 0)
                        break
