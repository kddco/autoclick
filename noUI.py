from pynput import mouse, keyboard
import threading
import time

# 連點的間隔時間（毫秒）
interval = 0.5

# 是否開始連點
start_clicking = False

# 建立滑鼠控制器
mouse_controller = mouse.Controller()

# 建立鍵盤監聽器
keyboard_listener = None

def click_mouse():
    global start_clicking, mouse_controller, interval
    while True:
        if start_clicking:
            # 按下並釋放滑鼠左鍵
            mouse_controller.press(mouse.Button.left)
            mouse_controller.release(mouse.Button.left)
        time.sleep(interval)  # 休眠

def on_press(key):
    global start_clicking
    if key == keyboard.Key.f10:
        # 按下F10鍵開始連點
        print("按下F10鍵開始連點")
        start_clicking = True
    elif key == keyboard.Key.f12:
        # 按下F12鍵停止連點
        print("按下F12鍵開始連點")
        start_clicking = False

def start_listening():
    global keyboard_listener
    with keyboard.Listener(on_press=on_press) as keyboard_listener:
        keyboard_listener.join()

# 建立並啟動鍵盤監聽器和滑鼠連點的線程
threading.Thread(target=start_listening).start()
threading.Thread(target=click_mouse).start()