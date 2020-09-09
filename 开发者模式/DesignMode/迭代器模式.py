# if __name__=="__main__":
#     lst=["hello Alice","hello Bob","hello Eve"]
#     lst_iter=iter(lst)
#     for i in lst_iter:
#         print (i)
# #   print (lst_iter.next())

#使用迭代器模式构造可迭代对象
class MyIter(object):
    def __init__(self, n):
        self.index = 0
        self.n = n
    def __iter__(self):
        return  MyIter(self.n)
    def __next__(self):
        if self.index < self.n:
            value = self.index**2
            self.index += 1
            return value
        else:
            raise StopIteration()
if __name__=="__main__":
    x_square=MyIter(10)
    for x in x_square:
        print (x)
    for x in x_square: #__iter__方法中的返回值，由于直接返回了self，因而该迭代器是无法重复迭代的
        print (x)
    #解决方法：
    # def __iter__(self):
    #     return MyIter(self.n)

#使用生成器来迭代
def MyGenerater(n):
    index=0
    while index<n:
        yield index**2
        index+=1
if __name__=="__main__":
    x_square=MyGenerater(10)
    for x in x_square:
        print('=======')
        print (x)