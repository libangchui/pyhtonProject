# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 11:10
# @Author  : 富贵
# @FileName: 1.py
import tkinter as tk

# 创建窗口
win = tk.Tk()
# 设置标题
win.title("收银员1.1")
# 设置窗口大小
win.geometry("400x400")
# 定义标签名
stort = tk.Label(win, text="STEGO STORE APPS\n------------------------------------------------------",
                 font=('Arial', 12))
stort.grid(row=0, column=1)
# 项目名称
t1 = tk.Label(win, text="name")
# 定义网格，row为行,column为列，设置显示位置为第一行
t1.grid(row=1)
# 价格
t2 = tk.Label(win, text="Unit Price")
t2.grid(row=2)
# 数量
t3 = tk.Label(win, text="Quantity")
t3.grid(row=3)
# 折扣
t4 = tk.Label(win, text="Discount")
t4.grid(row=4)
# 总折扣价
t5 = tk.Text(win, width=20, height=10)
t5.grid(row=6, column=1)

# 项目输入框
itemE = tk.Entry(win, bd=5)
# 定义网格，row为行,column为列，设置显示位置为第一行，第一列，显示在项目标签后
# padx：设置控件周围水平方向空白区域保留大小； pady：设置控件周围垂直方向空白区域保留大小；
itemE.grid(row=1, column=1, padx=10, pady=5)
# 价格输入框
Price = tk.Entry(win, bd=5)
Price.grid(row=2, column=1, padx=10, pady=5)
# 数量输入框
Quantity = tk.Entry(win, bd=5)
Quantity.grid(row=3, column=1, padx=10, pady=5)
# 折扣输入框
Discount = tk.Entry(win, bd=5, width=5)
Discount.grid(row=4, column=1, padx=10, pady=5)


# 总折扣价
# txtTotalDiscount = tk.Label(win,text="")
# txtTotalDiscount.grid(row=6,column=1,padx=10,pady=5)
# # 总付款
# txtTotaIPaid = tk.Label(win,text="")
# txtTotaIPaid.grid(row=7,column=1,padx=10,pady=5)

def ClickMe():
    """点击按钮计算总折扣价和总付款"""
    price = int(Price.get())  # 获取价格输入框中的数据，需要计算，转为Int类型
    quantity = int(Quantity.get())  # 获取数量输入框中的数据
    discount = int(Discount.get()) * 0.1  # 获取折扣数据，乘以0.1进行折扣计算，输入数值为1~10
    TotalDiscount = (price * discount) * quantity  # 计算总折扣价

    t5.insert("end", TotalDiscount)
    t5.insert("end","\n")


# 定义按钮
butt = tk.Button(win, text="Process", command=ClickMe)
butt.grid(row=5, column=1)
win.mainloop()
