import pytesseract
import os
import sys
from init import init
from img_process import get_process_image, K_th_img
from mouse_process import move_away, enter_num, click
from ocr import solve

size = 9

process_id, opt, flag = init()
num = [[0 for j in range(size)] for i in range(size)]
print('开始处理图像...')
img = get_process_image(process_id)
fout = open('sudoku.in', 'w')
for i in range(size):
    for j in range(size):
        num[i][j] = solve(K_th_img(img, i, j), opt)  #图像识别
        if not num[i][j]: num[i][j] = '0'
        fout.write(num[i][j] + ' ')
    fout.write('\n')
    print("已完成" + str(i + 1) + "行")
fout.close()
if flag:  #是否需要人工检验
    os.system("sudoku.in")
    os.system("pause")
print("开始求解...")
os.system('sudoku.exe')  #调用更加高效的C++来求解....(懒得再写python
fin = open('sudoku.out', 'r')
print("求解完成,开始填入解...")
click(process_id, (50, 50))  #手动切换窗口....
for i in range(size):
    id = fin.readline().split()
    if id[0] == '0': sys.exit("无解....")
    for j in range(size):
        if num[i][j] == '0': enter_num(process_id, i, j, id[j])
    print("已完成" + str(i + 1) + "行")
print("Q.E.D.")
