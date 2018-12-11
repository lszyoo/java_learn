#!/user/env/bin python3
# -*- coding: utf-8 -*-


import tkinter as tk        # 导入 tkinter 模块
from tkinter import ttk

# 窗口主题框架
window = tk.Tk()                    # 主窗口
window.title('my window')           # 窗口标题
window.geometry('400x200')          # 窗口尺寸，尺寸只能这么写，不能用*，不能有空格

var = tk.StringVar()                  # 文字变量储存器
var.set('OMG! this is TK!')
label = tk.Label(
    window,
    textvariable = var,                # 使用 textvariable 替换 text, 因为这个是可以变化的
    bg = 'green',
    font = ('Arial', 12),
    width = 15, height = 2
)

on_hit = False                      # 默认初始状态为 False
def hit_me():
    global on_hit                   # on_hit为全局变量
    if on_hit == False:
        on_hit = True
        var.set('you hit me')       # 设置标签的文字为 'you hit me'
        label.config(bg = 'blue')   # 更改label的背景颜色，也可以更改其他选项
    else:
        on_hit = False
        var.set('')
        label.config(bg = 'red')

# 按钮
button = tk.Button(
    window,
    text = 'hit me',                # 显示按钮上的文字
    width = 15, height = 2,
    command = hit_me                # 点击按钮执行的命令
)
button.pack()                       # 按钮位置

window.mainloop()                   # 循环消息，让窗口活起来

# 窗口控件

# label = tk.Label(
#     window,
#     text = 'OMG! this is TK!',      # 标签的文字
#     bg = 'green',                   # 背景颜色
#     font = ('Arial', 12),           # 字体和字体大小
#     width = 15, height = 2          # 标签长宽
# )
# label.pack()                        # 固定窗口位置

# var = tk.StringVar()                  # 文字变量储存器
# var.set('OMG! this is TK!')
# label = tk.Label(
#     window,
#     textvariable = var,                # 使用 textvariable 替换 text, 因为这个是可以变化的
#     bg = 'green',
#     font = ('Arial', 12),
#     width = 15, height = 2
# )

# 按钮
# button = tk.Button(
#     window,
#     text = 'hit me',                # 显示按钮上的文字
#     width = 15, height = 2,
#     command = hit_me                # 点击按钮执行的命令
# )
# button.pack()                       # 按钮位置
# 
# on_hit = False                      # 默认初始状态为 False
# def hit_me():
#     global on_hit                   # on_hit为全局变量
#     if on_hit == False:
#         on_hit = True
#         var.set('you hit me')       # 设置标签的文字为 'you hit me'
#         label.config(bg = 'blue')   # 更改label的背景颜色，也可以更改其他选项
#     else:
#         on_hit = False
#         var.set('')
#         label.config(bg = 'red')

# 创建输入框 entry，用户输入任何内容都显示为*
entry = tk.Entry(window, show = '*')    # 输入框，输入时显示
entry.pack()

# 创建文本框，用户可输入内容
txt = tk.Text(window, height = 2)       # 创建文本框，用户可输入内容

