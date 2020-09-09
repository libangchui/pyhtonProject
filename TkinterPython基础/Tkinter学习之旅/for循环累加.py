# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 10:47
# @Author  : 富贵
# @FileName: for循环累加.py

import tkinter as tk

win = tk.Tk()

win.title("for循环累加器")

win.geometry("300x300")

# 设置窗口部件
""" 
Frame：框架，用来承载放置其他GUI元素，就是一个容器，是一个在 Windows 上分离小区域的部件, 
它能将 Windows 分成不同的区,然后存放不同的其他部件. 同时一个 Frame 上也能再分成两个 Frame, 
Frame 可以认为是一种容器.
"""
frame1 = tk.Frame(win)
frame1.grid(row=0,column=0,padx=10)

l1 = tk.Label(frame1,text="Enter the Number")
l1.grid(row=0,pady=2)

e1 = tk.Entry(frame1,bd=5,width=10)
e1.grid(row=1,pady=20)

l2 = tk.Label(frame1,text="TOTAL")
l2.grid(row=3,pady=7)

t1 = tk.Text(frame1,bg="pink",state="normal",width = 10,height=10)
t1.grid(row=4)

def Click_Me():
    """
    返回一个对象，该对象会从开始数字(包括)到停止数字(不包括)按步长生成一个整数序列。
    range(i, j)会产生i, i+1, i+2，…，j-1。开始数字默认为0，停止数字被省略!range(4)会产生0,1,2,3。
    这些正是一个4元素列表的有效索引。当给定一个步长时，它指定了递增数(或递减数)。
    """
    num = int(e1.get())# 获取文本框中数字
    count = 0
    for i in range(0,num+1):
        t2.insert("end",f"{i}") # 按步长分别显示到右边文本框中
        t2.insert("end","\n")
        count = count + i # 相加从0到输入的数字
    t1.insert("end",f"{count}")
frame2 = tk.Frame(win)
frame2.grid(row=0,column=1)
t2 = tk.Text(frame2,state="normal",width=20,height=15)
t2.grid(row=0,column=1,pady=10)
butt = tk.Button(frame2,text="Click_Me",bd=3,width = 17,height =2,command=Click_Me)
butt.grid(row=1,column=1,padx=5,pady=20)
win.mainloop()