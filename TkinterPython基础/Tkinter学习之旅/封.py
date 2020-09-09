# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 12:48
# @Author  : 富贵
# @FileName: 封.py
# encoding:utf-8
import tkinter as tk
from tkinter import messagebox
window=tk.Tk()#实例化窗口
window.title('my window')#窗口的标题
window.geometry('500x200')#窗口的尺寸
var=tk.StringVar()
tk.Label(window, bg='yellow', width=20,height=4 ,textvariable=var).grid(row=0,column=1)

def text1():
    # ty=4<3
    # if ty==False:
    #     ty='False'
    # else:
    #     ty='True'
    var.set('True')
def text2():
    var.set('False')

tk.Button(window,text='4>1',width = 15,height = 2,command=text1).grid(row=2,column=0)
tk.Button(window,text='3<2',width = 15,height = 2,command=text2).grid(row=2,column=1)
tk.Button(window,text='10>=10',width = 15,height = 2,command=text2).grid(row=2,column=2)
tk.Button(window,text='15<=14',width = 15,height = 2,command=text2).grid(row=1,column=0)
tk.Button(window,text='20!=10',width = 15,height = 2,command=text1).grid(row=1,column=1)
tk.Button(window,text='A==a',width = 15,height = 2,command=text2).grid(row=1,column=2)

window.mainloop()