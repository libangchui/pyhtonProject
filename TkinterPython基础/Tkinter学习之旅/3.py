# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 10:43
# @Author  : 富贵
# @FileName: 3.py
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
    global list4
    list1 = ["张浩天","20"]
    list2=["帐号","2"]
    list3 = ["张天","3"]
    treeview.insert("", "end", values=list1)
    treeview.insert("", "end", values=list2)
    treeview.insert("", "end", values=list3)
    list4 = list1+list2+list3




b1 = ttk.Button(win,text = "Display Data",command = display)
b1.pack(side = "left")

def save():
    st=""
    for i in range(0,len(list4)):
        st = st+str(list4[i])+"\t\t"
    with open("student" + ".text", "w", encoding="utf-8") as f:
        f.write(st)



b2 = ttk.Button(win,text = "Display Data",command=save)
b2.pack(side = "right")


win.mainloop()
