# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 15:16
# @Author  : 富贵
# @FileName: 企业家.py
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import tkinter

win = Tk()
win.geometry("400x400+500+200")
win.resizable(0, 0)
f = ttk.Frame(win)
f.grid(row=0)
f1 = ttk.Frame(f)
f1.grid(row=0)
l1 = ttk.Label(f1,text = "ENTREPRENEUR’S DATA\n------------------------------")
l1.pack()

item_list=[]
# 定义按钮事件
def add():
    global list
    global totalprice
    s = [Ename.get(),EAddress.get(),comboxlist.get(),]
    treeview.insert('', 'end', values=s)
    item_list.append(s)

def save():
    for list in item_list:
        st=""
        for index in range(0,len(list)):
            st = st + str(list[index]) + "\t\t\t"
        with open("./entrepreneurdata.txt", "a+", encoding="utf-8") as f:
            f.writelines(st + "\n")
    messagebox.showinfo(title="保存成功", message="保存成功！")

# 定义f2容器
f2 = ttk.Frame(f)
f2.grid(row=1)
# NAME
Lname = ttk.Label(f2,text="Name")
Lname.grid(row=0,pady=5)
Ename = ttk.Entry(f2)
Ename.grid(row=0,column=1,padx = 100,pady=5)

LAddress = ttk.Label(f2,text="Address")
LAddress.grid(row=1,pady=5)
EAddress = ttk.Entry(f2)
EAddress.grid(row=1,column=1,padx = 100,pady=5)

# type

Lpull_down = ttk.Label(f2,text="Business Type")
Lpull_down.grid(row=2)
comvalue = tkinter.StringVar()  # 窗体自带的文本，新建一个值
comboxlist = ttk.Combobox(f2, textvariable=comvalue,state="readonly",width=18)  # 初始化
comboxlist["values"] = ("one", "two","three","four","five")
comboxlist.current(0)  # 选择第一个
comboxlist.bind("<<ComboboxSelected>>")
comboxlist.grid(row=2,column=1,padx = 100,pady=5)





fb = ttk.Frame(f)
fb.grid(row=2)
# 定义添加按钮
AddButton = ttk.Button(fb,text="Add",command=add)
AddButton.grid(row=0,column=0,pady=10,padx=10)
# 定义保存按钮
SaveButton = ttk.Button(fb,text="save",command=save)
SaveButton.grid(row=0,column=1)

# 定义f3容器
f3 = ttk.Frame(f)
f3.grid(row=3)
# 定义表格
columns = ("Name","Address", "Business Type")
treeview = ttk.Treeview(f3, height=20, show="headings", columns=columns)  # 表格

treeview.column("Name", width=120,anchor='center')  # 表示列,不显示
treeview.column("Business Type", width=110, anchor='center')
treeview.column("Address", width=100, anchor='center')


treeview.heading("Name", text="Name")  # 显示表头
treeview.heading("Business Type", text="Business Type")
treeview.heading("Address", text="Address")
treeview.pack()

win.mainloop()
