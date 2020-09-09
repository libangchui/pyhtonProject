# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 15:49
# @Author  : 富贵biubiu！！
# @FileName: tkinter_1.py

# 导包
import tkinter as tk
# 实例化窗口
window=tk.Tk()
# 设置窗口的标题
window.title('My window')
# 设置窗口的尺寸
window.geometry('400x400')
# 字符串变量
var=tk.StringVar()
# 变量赋值
var.set('Guess who I am?')
# 设置一个标签控件，
l=tk.Label(window,textvariable=var,bg='pink',font=('Arial',12),width=30,height=2)

# 将标签对齐放置
l.pack()

on_hit=False

def hit_me():#点击按钮的事件
    global on_hit#引用全局变量
    if on_hit==False:
        on_hit=True
        var.set('national defense handsome boy!')
    else:
        on_hit=False
        var.set('')
b=tk.Button(window,text='hit me',width=15,height=2,command=hit_me)
b.pack()#将标签对齐放置
window.mainloop()#循环显示
