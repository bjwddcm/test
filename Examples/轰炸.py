import pyautogui as gui

# 打开QQ快捷键 ctrl+alt+z
gui.hotkey('ctrl', 'alt', 'z')
# 发送次数 100，可以修改didi
for i in range(1, 100):
    # 修改message的内容，来修改发送内容
    gui.typewrite(message='lk')
    # 将打出的内容，放到输入窗口
    gui.hotkey(' ')
    # 按回车键发送，这个和自己qq设置的有关系
    gui.hotkey('Enter')lk