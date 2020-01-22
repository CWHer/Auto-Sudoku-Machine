import pytesseract
from PIL import ImageGrab, Image


def filter(threshold, opt):  #转化为黑白图像
    img = []
    for i in range(256):
        if i < threshold:
            img.append(0 ^ opt)
        else:
            img.append(1 ^ opt)
    return img


def solve(grid, opt):
    grid = grid.convert('L')  #转化为灰度模式
    binary_image = grid.point(filter(140, opt), "1")
    cnt = 0
    for i in range(binary_image.height):
        for j in range(binary_image.width):
            cnt += binary_image.getpixel((j, i)) > 0  #判断是否为空，优化OCR效率
    if cnt > binary_image.height * binary_image.width - 10: return ""
    return pytesseract.image_to_string(
        binary_image,
        config='--psm 10 --oem 3 -c tessedit_char_whitelist=123456789')
