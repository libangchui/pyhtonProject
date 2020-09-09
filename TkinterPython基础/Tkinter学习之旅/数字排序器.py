
# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 11:51
# @Author  : 富贵
# @FileName: a.py
import tkinter as tk

win = tk.Tk()

win.title("数字排序器1.1")

win.geometry("500x300")
f = tk.Frame(win)
f.grid(row=0,column=0)

f1 = tk.Frame(f)
f1.grid(row=0,column=1)

t1 = tk.Text(f1,bd=5,width=20,height=20)
t1.grid(row=0,padx=10,pady=10)

f2 = tk.Frame(f)
f2.grid(row=0,column=2)

condition = False

def Click_Me():
    global condition
    number_list = [10, 1, 9, 12, 3, 6, 6, 3, 11, 15, 20, 2, 20] # 初始列表
    if condition == False:
        for number in number_list:
            t1.insert("end",str(number))
            t1.insert("end","\n")
        condition = True
    elif condition == True:
    #     quick_sort = lambda array: array if len(array) <= 1 else quick_sort([
    #         item for item in array[1:] if item <= array[0]
    #     ]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])
        length = len(number_list)
        while length > 0:
            length -= 1
            cur = 0
            while cur < length:  # 拿到当前元素
                if number_list[cur] < number_list[cur + 1]:
                    number_list[cur], number_list[cur + 1] = number_list[cur + 1], number_list[cur]
                cur += 1
        for num in number_list:
            t2.insert("end",str(num))
            t2.insert("end","\n")

butt = tk.Button(f2,text="Click_Me",bd=3,width=10,height=5,command=Click_Me)
butt.pack(padx=10)

f3 = tk.Frame(f)
f3.grid(row=0,column=3)

t2 = tk.Text(f3,bd=5,width=20,height=20)
t2.grid(row=0,padx=10,pady=10)
win.mainloop()