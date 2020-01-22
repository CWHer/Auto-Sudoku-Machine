import time
import win32gui
from pymouse import PyMouse
from pykeyboard import PyKeyboard

grid_len = 57
L = 392
R = 392
U = 159
D = 136


def K_th(i, j):  #计算点击坐标
    x = j * grid_len + grid_len // 2
    y = i * grid_len + grid_len // 2
    return (int(x), int(y))


def click(process_id, pos):  #左键单击
    process_pos = win32gui.GetWindowRect(process_id)
    PyMouse().click(process_pos[0] + pos[0], process_pos[1] + pos[1])
    time.sleep(0.1)


def move(process_id, pos):  #仅移动
    process_pos = win32gui.GetWindowRect(process_id)
    PyMouse().move(process_pos[0] + L + pos[0], process_pos[1] + U + pos[1])
    time.sleep(0.1)


def move_away(process_id):  #移动至窗口左上角，防止干扰截图
    process_pos = win32gui.GetWindowRect(process_id)
    PyMouse().move(process_pos[0], process_pos[1])
    time.sleep(0.1)


def enter_num(process_id, i, j, id):  #输入数字
    move(process_id, K_th(i, j))
    PyKeyboard().tap_key(id)
    time.sleep(0.1)