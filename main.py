mun = 0


def land():
    global mun
    mun = int(mun + 1)
    a = mun / 12
    a = "%.2f" % a
    print("\r正在载入第三方库", "[", a, "]", end='')


import subprocess

land()
import time

land()
import cv2

land()
import numpy as np

land()
import pyautogui

land()
from PIL import ImageGrab

land()
import threading

land()
from playsound import playsound
#import mp3play
land()
import win32gui

land()
import win32con

land()
import win32com.client

land()
import pythoncom

land()
print("\r载入第三方库完毕""\n""开始载入视频", end=" ")
cap = cv2.VideoCapture("video.mp4")
# 打开我们要播放的文件
print("\r载入视频完成，开始检测")


def run_top():
    #奇怪的bug，这个param必须有，否则报错
   # def get_all_hwnd(hwnd, param):
    def get_all_hwnd(hwnd, param):
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            hwnd_map.update({hwnd: win32gui.GetWindowText(hwnd)})

    hwnd_map = {}
    win32gui.EnumWindows(get_all_hwnd, 0)

    for h, t in hwnd_map.items():
        if t:
            if t == 'video':
                win32gui.BringWindowToTop(h)
                pythoncom.CoInitialize()
                shell = win32com.client.Dispatch("WScript.Shell")
                shell.SendKeys('%')

                win32gui.SetForegroundWindow(h)

                win32gui.ShowWindow(h, win32con.SW_RESTORE)


def video():
    cap.get(cv2.CAP_PROP_FPS)
    while True:
        ret, frame = cap.read()
        cv2.namedWindow("video", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("video", frame)
        run_top()
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()

    cv2.destroyAllWindows()


def music():
    playsound("video.mp3")



def run():
    vd = threading.Thread(target=video)
    mc = threading.Thread(target=music)
    vd.start()
    mc.start()


def old_play_video():
    # 加大力度
    pyautogui.hotkey('esc')
    # 模拟按下Alt+F4组合键来关闭当前活动窗口
    pyautogui.hotkey('alt', 'f4')
    # 播放视频
    proc = subprocess.Popen(['start', 'Video.mp4'], shell=True)
    proc.communicate()
    # 自动点击
    # 将鼠标移动到屏幕右上角
    pyautogui.moveTo(screenWidth, 100)
    time.sleep(0.8)
    pyautogui.hotkey('F11')
    pyautogui.click()
    time.sleep(15)
    pyautogui.hotkey('alt', 'F4')


# 完整屏幕是否白屏检查
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
def yuanshen_start(start_model):
    if start_model == 1:
        pass
    else:
        run()
run()
# 获取屏幕分辨率
screenWidth, screenHeight = pyautogui.size()
# print("屏幕分辨率为 %sx%s" % (screenWidth, screenHeight))
# 询问是否有安装原神
start_model = 'none'

# while True:
#     model = input("是否有安装原神？（yes/no） ")
#     if model == "yes":
#         start_model = 1
#         break
#     elif model == "no":
#         start_model = 0
#         break
#     else:
#         print("请输入yes/no")
#         continue
# print("启动模式为" + str(start_model))
# # 询问原神ink(如果有）
# if start_model == 1:
#     yuanshen_lnk = input("请原神输入lnk")
# else:
#     pass

# 是否有白屏（快速）
while True:
    im = ImageGrab.grab()  # 获取当前屏幕快照
    pix = im.load()  # 用于读取像素
    a1 = min(pix[1, 1])
    a2 = min(pix[screenWidth - 1, 1])
    b1 = min(pix[1, screenHeight - 1])
    b2 = min(pix[screenWidth - 1, screenHeight - 1])
    print("\r屏幕四个角的RGB值的最小值：", a1, a2, b1, b2, end='')
    s = a1 + a2 + b1 + b2
    if s >= 900:
        s1 = detect_white_screen()
        if s1 >= 254:
            print("原神，启动！")
            yuanshen_start(start_model)
            break
        else:
            print("\r快速检测失误")
            time.sleep(0.1)
            continue
    else:
        time.sleep(0.05)
        continue
pass
