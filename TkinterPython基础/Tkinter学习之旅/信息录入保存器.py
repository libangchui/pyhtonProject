# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 11:41
# @Author  : 富贵
# @FileName: 信息录入保存器.py
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import tkinter
import xlwt

win = Tk()
win.geometry("400x400")
f = ttk.Frame(win)
f.grid(row=0)
f1 = ttk.Frame(f)
f1.grid(row=0)
l1 = ttk.Label(f1,text = "MY FRIENDS DATA\n----------------------")
l1.pack()

item_list=[]
# 定义按钮事件
def add():
    global list
    global totalprice
    s = [Ename.get(),comboxlist.get(),EAddress.get(),EPhone.get()]
    treeview.insert('', 'end', values=s)
    item_list.append(s)
a = 0
def save():
    global a
    wb = xlwt.Workbook()
    # 新增表单页
    sh1 = wb.add_sheet('FRIENDS_DATA')
    # 然后按照位置来添加数据,第一个参数是行，第二个参数是列
    # 写入第一个sheet
    for list in item_list:
        for index in range(0,len(list)):
            sh1.write(a, index, list[index])
            wb.save('FRIENDS_DATA.xls')
        a += 1
    messagebox.showinfo(title="保存成功", message="保存成功！")

# 定义f2容器
f2 = ttk.Frame(f)
f2.grid(row=1)
# NAME
Lname = ttk.Label(f2,text="Name")
Lname.grid(row=0,pady=5)
Ename = ttk.Entry(f2)
Ename.grid(row=0,column=1,padx = 100,pady=5)

# sex
Lpull_down = ttk.Label(f2,text="Sex")
Lpull_down.grid(row=1)
comvalue = tkinter.StringVar()  # 窗体自带的文本，新建一个值
comboxlist = ttk.Combobox(f2, textvariable=comvalue,state="readonly",width=10)  # 初始化
comboxlist["values"] = ("Male", "Female")
comboxlist.current(0)  # 选择第一个
comboxlist.bind("<<ComboboxSelected>>")
comboxlist.grid(row=1,column=1,padx = 100,pady=5)

LAddress = ttk.Label(f2,text="Address")
LAddress.grid(row=2,pady=5)
EAddress = ttk.Entry(f2)
EAddress.grid(row=2,column=1,padx = 100,pady=5)
# Phone
LPhone = ttk.Label(f2,text="Phone")
LPhone.grid(row=3,pady=5)
EPhone = ttk.Entry(f2)
EPhone.grid(row=3,column=1,padx = 100,pady=5)


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
columns = ("Name", "Sex","Address","Phone")
treeview = ttk.Treeview(f3, height=20, show="headings", columns=columns)  # 表格

treeview.column("Name", width=85,anchor='center')  # 表示列,不显示
treeview.column("Sex", width=85, anchor='center')
treeview.column("Address", width=85, anchor='center')
treeview.column("Phone", width=85, anchor='center')


treeview.heading("Name", text="Name")  # 显示表头
treeview.heading("Sex", text="Sex")
treeview.heading("Address", text="Address")
treeview.heading("Phone", text="Phone")
treeview.pack()

win.mainloop()
