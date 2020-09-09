# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 11:00
# @Author  : 富贵
# @FileName: messagebox.py
import tkinter as tk
from tkinter import messagebox

win = tk.Tk()

win.title("1")

def click():
    tk.messagebox.showinfo(title=None, message="保存成功！")
button = tk.Button(text="sd",command=click)
button.pack()

tk.mainloop()