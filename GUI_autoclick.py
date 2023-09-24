import tkinter as tk
import threading
import time
import pyautogui
import keyboard

# 全局变量来跟踪程序状态
is_clicking = False
click_interval = 0.01  # 默认点击间隔为0.5秒

# 函数用于开始点击
def start_clicking():
    global is_clicking
    if not is_clicking:
        is_clicking = True
        print("连点已启动")
        clicking_thread = threading.Thread(target=auto_click)
        clicking_thread.start()
        # 提升窗口到顶层
        window.lift()

# 函数用于停止点击
def stop_clicking():
    global is_clicking
    if is_clicking:
        is_clicking = False
        print("连点已停止")

# 函数用于连续点击
def auto_click():
    while is_clicking:
        pyautogui.click()
        time.sleep(click_interval)

# 函数用于设置点击间隔
def set_click_interval():
    global click_interval
    new_interval = entry.get()
    try:
        click_interval = float(new_interval)
    except ValueError:
        pass

# 函数用于检测F10和F12按键
def check_hotkeys():
    while True:
        if keyboard.is_pressed('F8'):
            start_clicking()
        elif keyboard.is_pressed('F9'):
            stop_clicking()
            # break

# 函数用于周期性地更新UI状态
def update_status():
    if is_clicking:
        status_label.config(text="正在连点")
    else:
        status_label.config(text="未启动")
    window.after(100, update_status)

# 创建GUI窗口
window = tk.Tk()
window.title("连点程序")

# 创建标签和按钮
status_label = tk.Label(window, text="未启动")
start_button = tk.Button(window, text="启动连点", command=start_clicking)
stop_button = tk.Button(window, text="停止连点", command=stop_clicking)
entry_label = tk.Label(window, text="点击间隔（秒）:")
entry = tk.Entry(window)
set_interval_button = tk.Button(window, text="设置间隔", command=set_click_interval)

# 布局窗口组件
status_label.pack()
start_button.pack()
stop_button.pack()
entry_label.pack()
entry.pack()
set_interval_button.pack()

# 创建检测热键的线程
hotkey_thread = threading.Thread(target=check_hotkeys)
hotkey_thread.start()

# 周期性地更新UI状态
update_status()

# 运行GUI界面
window.mainloop()
