# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 11:32
# @Author  : 富贵
# @FileName: 简单商店应用程序.py
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

win = Tk()
win.geometry("400x400")
f = ttk.Frame(win)
f.grid(row=0)
f1 = ttk.Frame(f)
f1.grid(row=0)
l1 = ttk.Label(f1,text = "STEGO STORE APP\n----------------------")
l1.pack()
# 定义f2容器
f2 = ttk.Frame(f)
f2.grid(row=1)
# id
Lid = ttk.Label(f2,text="ID")
Lid.grid(row=0,pady=5)
Eid = ttk.Entry(f2)
Eid.grid(row=0,column=1,padx = 100,pady=5)
# item
Litem = ttk.Label(f2,text="ITEM")
Litem.grid(row=1,pady=5)
Eitem = ttk.Entry(f2)
Eitem.grid(row=1,column=1,padx = 100,pady=5)
# price
Lprice = ttk.Label(f2,text="Unit Price")
Lprice.grid(row=2,pady=5)
Eprice = ttk.Entry(f2)
Eprice.grid(row=2,column=1,padx = 100,pady=5)
# quantity
Lquantity = ttk.Label(f2,text="Quantity")
Lquantity.grid(row=3,pady=5)
Equantity = ttk.Entry(f2)
Equantity.grid(row=3,column=1,padx = 100,pady=5)

item_list=[]
# 定义所有物品总价
totalprice = 0
def add():
    global list
    global totalprice
    # 获取输入框数据
    s = [Eid.get(),Eitem.get(),Eprice.get(),Equantity.get(),int(Eprice.get())*int(Equantity.get())]
    # 计算总价
    totalprice = totalprice + int(Eprice.get())*int(Equantity.get())
    # 写入表格
    treeview.insert('', 'end', values=s)
    # 存入商品数据
    item_list.append(s)

def save():
    # 遍历所有商品
    for list in item_list:
        st = ""
        for index in range(0,len(list)):
            st = st + str(list[index])+"\t\t\t"
        # 写入商品到文件
        with open("./stort.txt", "a+", encoding="utf-8") as f:
            f.writelines(st+"\n")
    # 写入总价
    with open("./stort.txt", "a+", encoding="utf-8") as f:
        f.writelines("-------------------------------------------"+"\n")
        f.writelines("TotalPrice:"+str(totalprice)+"\n")
    messagebox.showinfo(title="保存成功", message="保存成功！")


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
columns = ("ID", "Item Name","Unit Price","Quantity","Total Price")
treeview = ttk.Treeview(f3, height=18, show="headings", columns=columns)  # 表格

treeview.column("ID", width=75,anchor='center')
treeview.column("Item Name", width=75, anchor='center')
treeview.column("Unit Price", width=75, anchor='center')
treeview.column("Quantity", width=75, anchor='center')
treeview.column("Total Price", width=75, anchor='center')

treeview.heading("ID", text="ID")  # 显示表头
treeview.heading("Item Name", text="Item Name")
treeview.heading("Unit Price", text="Unit Price")
treeview.heading("Quantity", text="Quantity")
treeview.heading("Total Price", text="Total Price")
treeview.pack()

win.mainloop()
