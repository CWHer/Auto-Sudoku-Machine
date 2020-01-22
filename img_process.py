import win32gui
from mouse_process import move_away
from PIL import Image, ImageGrab, ImageFilter, ImageEnhance

grid_len = 57
L = 391
R = 391
U = 158
D = 134
gap = 7


def get_process_image(process_id):  #获取Sudoku Universe界面图片
    left, top, right, bottom = win32gui.GetWindowRect(process_id)
    process_side = (left + L, top + U, right - R, bottom - D)  #手动量取|･ω･｀)
    move_away(process_id)
    return ImageGrab.grab().crop(process_side)


def K_th_img(img, i, j):  #裁剪为单个数字单元
    x = j * grid_len
    y = i * grid_len
    grid = img.crop((x, y, x + grid_len, y + grid_len))
    return grid.crop((gap, gap, grid_len - gap, grid_len - gap))
