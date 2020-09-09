# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 11:01
# @Author  : 富贵
# @FileName: zhang.py
from tkinter import ttk
from tkinter import *

win = Tk()
win.geometry("500x500")
l1 = ttk.Label(win,text = "STUDENTS OF MATARAM UNIVERSITY")
l1.pack()

treeview = ttk.Treeview(win, height=18, show="headings", columns=("Name", "Faculty"))  # 表格

treeview.column("Name", width=200, anchor='center')
treeview.column("Faculty", width=200, anchor='center')

treeview.heading("Name", text="Name")  # 显示表头
treeview.heading("Faculty", text="Faculty")
treeview.pack()

def display():
    list = ["张浩天","20"]
    treeview.insert("", "end", values=list)

b1 = ttk.Button(win,text = "Display Data",command = display)
b1.pack(side = "left")

b2 = ttk.Button(win,text = "Display Data")
b2.pack(side = "right")


win.mainloop()