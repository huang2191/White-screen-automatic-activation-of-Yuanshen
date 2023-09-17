import time
import os
import pyautogui
import cv2
import numpy as np
from PIL import ImageGrab
import win32gui
import win32con
import moviepy.editor as mp


def play_video(file_path):
    # 创建一个无边框的 OpenCV 窗口
    cv2.namedWindow("Video", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # 使用 moviepy 库加载视频文件
    video = mp.VideoFileClip(file_path)

    # 创建一个用于播放视频的窗口
    video.preview()

    hwnd = win32gui.FindWindow('MoviePy', "pygame")
    # hwnd = win32gui.FindWindow('xx.exe', None)
    # 窗口需要正常大小且在后台，不能最小化
    win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
    # 窗口需要最大化且在后台，不能最小化
    # ctypes.windll.user32.ShowWindow(hwnd, 3)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                          win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE | win32con.SWP_NOOWNERZORDER | win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE)
    # 取消置顶
    # win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,win32con.SWP_SHOWWINDOW|win32con.SWP_NOSIZE|win32con.SWP_NOMOVE)
    # 使用 pyautogui 模拟按下 Alt+Space 和 T 键来置顶窗口
    pyautogui.hotkey('alt', 'space')
    pyautogui.press('t')

    # 关闭窗口
    cv2.destroyAllWindows()


# 来自chatGPT
def detect_white_screen():
    # 获取屏幕截图
    screenshot = ImageGrab.grab()

    # 将截图转换为OpenCV图像
    image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # 将图像转换为灰度图
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 计算图像的平均像素值
    average_pixel_value = gray_image.mean()
    print("完整检测值为：" + str(average_pixel_value))
    return int(average_pixel_value)


# 原神启动函数
def yuanshen_start(start_model, yuanshen_lnk):
    if start_model == 1:
        os.statvfs(r'yuanshen_lnk')
    else:
        play_video("video.mp4")

        # 将鼠标移动到屏幕右上角
        pyautogui.moveTo(screenWidth, 0)

        # 模拟按下Alt+F4组合键来关闭当前活动窗口
        pyautogui.hotkey('alt', 'f4')


# 获取屏幕分辨率
screenWidth, screenHeight = pyautogui.size()
print("屏幕分辨率为 %sx%s" % (screenWidth, screenHeight))
yuanshen_lnk = None
# 询问是否有安装原神
start_model = 'none'

while True:
    model = input("是否有安装原神？（yes/no） ")
    if model == "yes":
        start_model = 1
        break
    elif model == "no":
        start_model = 0
        break
    else:
        print("请输入yes/no")
        continue
print("启动模式为" + str(start_model))
# 询问原神ink(如果有）
if start_model == 1:
    yuanshen_lnk = input("请原神输入lnk")
else:
    pass

# 是否有白屏（快速）
while True:
    im = ImageGrab.grab()  # 获取当前屏幕快照
    pix = im.load()  # 用于读取像素
    a1 = min(pix[1, 1])
    a2 = min(pix[screenWidth - 1, 1])
    b1 = min(pix[1, screenHeight - 1])
    b2 = min(pix[screenWidth - 1, screenHeight - 1])
    print("屏幕四个角的RGB值的最小值：", a1, a2, b1, b2)
    s = a1 + a2 + b1 + b2
    print(s)
    if s >= 900:
        s1 = detect_white_screen()
        if s1 >= 254:
            print("原神，启动！")
            yuanshen_start(start_model, yuanshen_lnk)
            break
        else:
            print("快速检测失误")
            continue
    else:
        time.sleep(1)
        continue
pass
