# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 15:25
# @Author  : 富贵
# @FileName: 下拉列表.py
# state='readonly'
# import
# number = ttk.StringVar()
# numberChosen = ttk.Combobox(f2, width=12, textvariable=number,state='readonly')
# numberChosen['values'] = ("Male", "Female")     # 设置下拉列表的值
# numberChosen.grid(column=0, row=1)      # 设置其在界面中出现的位置  column代表列   row 代表行
# numberChosen.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值\
import tkinter
from  tkinter import ttk


def go(*args):  # 处理事件，*args表示可变参数
    print(comboxlist.get())  # 打印选中的值

win = tkinter.Tk()  # 构造窗体
comvalue = tkinter.StringVar()  # 窗体自带的文本，新建一个值
comboxlist = ttk.Combobox(win, textvariable=comvalue)  # 初始化
comboxlist["values"] = ("1", "2", "3", "4")
comboxlist.current(0)  # 选择第一个
comboxlist.bind("<<ComboboxSelected>>", go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
comboxlist.pack()

win.mainloop()  # 进入消息循环