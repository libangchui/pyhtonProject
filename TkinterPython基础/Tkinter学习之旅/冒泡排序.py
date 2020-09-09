# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 11:13
# @Author  : 富贵
# @FileName: 冒泡排序.py
target = [10, 1, 9, 12, 3, 6, 6, 3, 11, 15, 20, 2, 20]
length = len(target)
while length > 0:
    length -= 1
    cur = 0
    while cur < length: #拿到当前元素
        if target[cur] < target[cur + 1]:
            target[cur], target[cur + 1] = target[cur + 1], target[cur]
        cur += 1
print(target)
