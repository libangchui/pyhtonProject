# -*- coding: utf-8 -*-
# @Time    : 2020/3/26 19:20
# @Author  : 富贵
# @FileName: 简单进制转换器.py

# 导入模块
import tkinter as tk
from tkinter import *

# 创建窗口
win = tk.Tk()

# 设置标题
win.title("进制转换器1.1")

# 设置窗口大小
win.geometry("800x200")

# 设置点击事件
def Click_Me():
    """计算十进制转二进制"""
    n = str(bin(int(text.get()))) # 从text中获取十进制数，转为整型，使用bin方法转为二进制
    m = n.replace("0b","") # 删除转为二进制留下的”0b“
    if len(m) <=8:
        """判断长度，不够8位在前面添加相应的0"""
        m = (8-len(m))*"0"+m
        b7.insert(END, m[0]) # 取出字符串的第一位，下标为0的数，显示到第一个文本框中
        b6.insert(END, m[1])
        b5.insert(END, m[2])
        b4.insert(END, m[3])
        b3.insert(END, m[4])
        b2.insert(END, m[5])
        b1.insert(END, m[6])
        b0.insert(END, m[7])
# 设置项目标题标签
title = tk.Label(win,text="DECIMAL TO BINARY CONVERSION \n--------------------------------------------------")
title.grid(row=0,column=1)

# 输入框标签
t1 = tk.Label(win,text="Insert The Number")
t1.grid(row=1,column=0)

# 输入框
text = tk.Entry(win,bd=5,width=15)
text.grid(row=2,column=0,sticky=W)

# 按钮
butt = tk.Button(win,text="Click Me",command=Click_Me)
butt.grid(row=2,column=1,sticky=W)


# 设置二进制每位的显示框
b7 = tk.Text(win,bd=5,width=5,height=3)
b7.grid(row=2,column=2,sticky=W)
# 设置下方单位
Lb7 = tk.Label(win,text="bit7")
Lb7.grid(row=3,column=2)

b6 = tk.Text(win,bd=5,width=5,height=3)
b6.grid(row=2,column=3,sticky=W)
Lb6 = tk.Label(win,text="bit6")
Lb6.grid(row=3,column=3)

b5 = tk.Text(win,bd=5,width=5,height=3)
b5.grid(row=2,column=4,sticky=W)
Lb5 = tk.Label(win,text="bit5")
Lb5.grid(row=3,column=4)

b4 = tk.Text(win,bd=5,width=5,height=3)
b4.grid(row=2,column=5,sticky=W)
Lb4 = tk.Label(win,text="bit4")
Lb4.grid(row=3,column=5)

b3 = tk.Text(win,bd=5,width=5,height=3)
b3.grid(row=2,column=6,sticky=W)
Lb3 = tk.Label(win,text="bit3")
Lb3.grid(row=3,column=6)

b2 = tk.Text(win,bd=5,width=5,height=3)
b2.grid(row=2,column=7,sticky=W)
Lb2 = tk.Label(win,text="bit2")
Lb2.grid(row=3,column=7)

b1 = tk.Text(win,bd=5,width=5,height=3)
b1.grid(row=2,column=8,sticky=W)
Lb1 = tk.Label(win,text="bit1")
Lb1.grid(row=3,column=8)

b0 = tk.Text(win,bd=5,width=5,height=3)
b0.grid(row=2,column=9,sticky=W)
Lb0 = tk.Label(win,text="bit0")
Lb0.grid(row=3,column=9)

# 循环显示
win.mainloop()