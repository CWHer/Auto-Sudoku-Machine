import win32gui
import sys


def check_process():  #检查程序是否运行
    process_id = win32gui.FindWindow("UnityWndClass", "Sudoku Universe")
    if not process_id: sys.exit("请先运行Sudoku Universe....")
    return process_id


def check_opt(opt):  #判断操作(Y/N)
    if opt.find("Y") != -1: return 1
    if opt.find("N") != -1: return 0
    return -1


def init():
    ret = []
    process_id = check_process()
    print("请勿将Sudoku Universe中央数字界面遮盖")
    print("默认分辨率:1280x768,如有需要请手动调节参数(真·手动,指改代码)")
    opt = input("是否需要反转颜色?(白色数字需勾选)(Y/N)\n")
    while check_opt(opt.upper()) == -1:
        opt = input("是否需要反转颜色?(白色数字需勾选)(Y/N)\n")
    ret.append(check_opt(opt.upper()))
    opt = input("是否需要人工检验数字识别结果?(若已填部分需继续,建议勾选)(Y/N)\n")
    while check_opt(opt.upper()) == -1:
        opt = input("是否需要人工检验数字识别结果?(若已填部分需继续,建议勾选)(Y/N)\n")
    ret.append(check_opt(opt.upper()))
    opt = input("Ready?(Y/N)\n")
    while check_opt(opt.upper()) == -1:
        opt = input("Ready?(Y/N)\n")
    if not check_opt(opt.upper()): sys.exit("Farewell")
    return process_id, ret[0], ret[1]
