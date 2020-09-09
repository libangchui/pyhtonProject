# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 10:41
# @Author  : 富贵
# @FileName: 奇偶分析器.py
import tkinter as tk

win = tk.Tk()

win.title("奇偶排序器1.1")

win.geometry("650x300")
f = tk.Frame(win)
f.grid(row=0,column=0)

f1 = tk.Frame(f)
f1.grid(row=0,column=1)

l1 = tk.Label(f1,text="Full Iteration")
l1.grid(row=0,padx=10,pady=10)

t1 = tk.Text(f1,bd=5,width=20,height=15)
t1.grid(row=1,padx=10,pady=10)

f2 = tk.Frame(f)
f2.grid(row=0,column=2)

condition = False

def Click_Me():
    global condition
    number_list = [10, 1, 9, 12, 3, 6, 6, 3, 11, 15, 20, 2, 20,4,7,18,]
    if condition == False:
        for number in number_list:
            t1.insert("end",str(number))
            t1.insert("end","\n")
        condition = True
    elif condition == True:
        for num in number_list:
            if num%2 == 0:
                t2.insert("end",str(num))
                t2.insert("end", "\n")
                continue
            else:
                t3.insert("end",str(num))
                t3.insert("end", "\n")
                continue

butt = tk.Button(f2,text="Click_Me",bd=3,width=10,height=5,command=Click_Me)
butt.pack(padx=10)

f3 = tk.Frame(f)
f3.grid(row=0,column=3)

l2 = tk.Label(f3,text="Odd Numbers")
l2.grid(row=0,padx=10,pady=10)

t2 = tk.Text(f3,bd=5,width=20,height=15)
t2.grid(row=1,padx=10,pady=10)

f4 = tk.Frame(f)
f4.grid(row=0,column = 4)
l3 = tk.Label(f4,text="Even Numbers")
l3.grid(row=0,padx=10,pady=10)

t3 = tk.Text(f4,bd=5,width=20,height=15)
t3.grid(row=1,padx=10,pady=10)

win.mainloop()