# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 12:16
# @Author  : 富贵
# @FileName: 字符串连接器.py
# 导入模块
import tkinter as tk
# 创建窗口
win = tk.Tk()
# 设置标题
win.title("字符串连接器1.1")
# 设置窗口大小
win.geometry("400x300")

# 标题
title = tk.Label(win,text="Concatenation of Two Strings\n------------------------------------------------------")
title.grid(row=0,column=1)
# 创建标签一
Lt1 = tk.Label(win,text="word1")
Lt1.grid(row=1,column=0)
# 创建标签一的输入框
t1 = tk.Entry(win,bd=5)
t1.grid(row=1,column=1)
# 标签二
Lt2 = tk.Label(win,text="word2")
Lt2.grid(row=2,column=0)
# 创建标签二的输入框
t2 = tk.Entry(win,bd=5)
t2.grid(row=2,column=1)
# 定义点击事件
def Click_Me():
    """获取两个输入框的数据，使用字符串性质，用+号连接"""
    one = str(t1.get())
    two = str(t2.get())
    txt = one + two
    text.insert("end",txt)
    text.insert("end","\n")
# 创建按钮
butt = tk.Button(win,text="Concate the Word",command=Click_Me)
butt.grid(row=3,column=1)
# 创建显示本文框，用来显示连接后的数据
text = tk.Text(win,bd=5,width=30,height=8)
text.grid(row=4,column=1)
# 循环显示
win.mainloop()