# -*- coding: utf-8 -*-
# @Time    : 2020/3/26 10:09
# @Author  : 富贵
# @FileName: 简单的运算.py
# 导入模块
import tkinter as tk
# 实例化窗口
win = tk.Tk()
# 设置窗口标题
win.title("python GUI")
# 设置窗口大小
win.geometry("400x400")
# 定义加法标签
numaddition = tk.Label(win,text="",font=('Arial', 12))
numaddition.pack()
# 定义减法标签
numsubtraction = tk.Label(win,text="",font=('Arial', 12))
numsubtraction.pack()
# 定义乘法标签
nummultiplication = tk.Label(win,text="",font=('Arial', 12))
nummultiplication.pack()
# 定义除法标签
numdivision = tk.Label(win,text="",font=('Arial', 12))
numdivision.pack()
# 定义次方标签
numExponential= tk.Label(win,text="",font=('Arial', 12))
numExponential.pack()

# 定义函数，点击时运算，显示标签中
def clickMe():
    butt.configure(text="oh") # 点击时更改按钮文本
    # 使用str方法把运算结果的int类型转换为字符串类型，才能显示到标签中
    numaddition.configure(text=str(100+1)) # 加法运算
    numsubtraction.configure(text=str(100-50)) # 减法运算
    nummultiplication.configure(text=str(30*10)) # 乘法运算
    numdivision.configure(text=str(100/2)) # 除法运算
    numExponential.configure(text=str(5**2)) # 次方运算

# 定义按钮，设置点击函数
butt = tk.Button(win,text="click Me",command=clickMe)
butt.pack()

# 循环显示
win.mainloop()