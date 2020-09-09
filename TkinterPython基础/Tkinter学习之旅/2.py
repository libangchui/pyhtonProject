# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 12:32
# @Author  : 富贵
# @FileName: 2.py
import tkinter as tk
from tkinter import *
# 创建窗口
win = tk.Tk()
# 设置标题
win.title("收银员1.1")
# 设置窗口大小
win.geometry("400x400")
# 定义标签名
stort = tk.Label(win,text="CITIZEN DATA FORM\n------------------------------------------------------",font=('Arial', 12))
stort.grid(row=0,column=1)
"""
"ID","Name","Title","Place/Date of Birth","Address"and"Latest Aducation "。
然后添加六个文本字段，并使用以下名称更改每个变量的名称：txtID、txtName txtTitle、txtPDB 、txtAddress和txtEducation。
"""
t1 = tk.Label(win,text="id")
t1.grid(row=1)
# 价格
t2 = tk.Label(win,text="Name")
t2.grid(row=2)
# 数量
t3 = tk.Label(win,text="Title")
t3.grid(row=3)
# 折扣
t4 = tk.Label(win,text="pDB")
t4.grid(row=4)
# 总折扣价
t5 = tk.Label(win,text="address")
t5.grid(row=5)
# 总付款
t6 = tk.Label(win,text="eduction")
t6.grid(row=6)

e1 = tk.Entry()
e1.grid(row=1,column=1)
e2 = tk.Entry()
e2.grid(row=2,column=1)
e3 = tk.Entry()
e3.grid(row=3,column=1)
e4 = tk.Entry()
e4.grid(row=4,column=1)
e5 = tk.Entry()
e5.grid(row=5,column=1)
e6 = tk.Entry()
e6.grid(row=6,column=1)



stort = tk.Label(win,text="DETAIL\n------------------------------------------------------",font=('Arial', 12))
stort.grid(row=8,column=1)

t7 = tk.Label(win,text="id              :")
t7.grid(row=9,sticky=W)

t8 = tk.Label(win,text="Name        :")
t8.grid(row=10,sticky=W)

t9 = tk.Label(win,text="Title           :")
t9.grid(row=11,sticky=W)

t10 = tk.Label(win,text="pDB           :")
t10.grid(row=12,sticky=W)

t11 = tk.Label(win,text="address      :")
t11.grid(row=13,sticky=W)

t12 = tk.Label(win,text="eduction     :")
t12.grid(row=14,sticky=W)

l1 = tk.Label(win)
l1.grid(row=9, column=1,sticky=W)
l2 = tk.Label(win)
l2.grid(row=10, column=1,sticky=W)
l3 = tk.Label(win)
l3.grid(row=11, column=1,sticky=W)
l4 = tk.Label(win)
l4.grid(row=12, column=1,sticky=W)
l5 = tk.Label(win)
l5.grid(row=13, column=1,sticky=W)
l6 = tk.Label(win)
l6.grid(row=14, column=1,sticky=W)
def go():
    l1.configure(text=e1.get())
    l2.configure(text=e2.get())
    l3.configure(text=e3.get())
    l4.configure(text=e4.get())
    l5.configure(text=e5.get())
    l6.configure(text=e6.get())





b = tk.Button(win,text = "process",command=go)
b.grid(row=7,column=1)
win.mainloop()

