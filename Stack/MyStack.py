# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     MyStack
   Description :
   Author :       bing
   date：          2021/7/3
-------------------------------------------------
   Change Activity:
                   2021/7/3:
-------------------------------------------------
"""
__author__ = 'bing'
"""
接口设计
1、size  - 容量
2、push  - 将元素压入栈内
3、pop   - 将元素弹出栈外
4、is_empty  - 判断栈是否为空
5、peek  - 查看栈顶元素

设计理念：采用python自带的数据结构列表来实现栈
"""


class Stack:
    def __init__(self, limit: int):
        self.stack = []
        self.limit = limit

    def size(self) -> int:
        return len(self.stack)

    def push(self, data):
        if data and self.size() < self.limit:
            self.stack.append(data)
        elif self.size() >= self.limit:
            raise IndexError('超出容量极限')
        else:
            raise ValueError('该值不符合')

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            raise IndexError('不能从空栈返回')

    def peek(self):
        if self.size() > 0:
            return self.stack[-1]
        else:
            raise IndexError('栈为空')

    def is_empty(self) -> bool:
        if self.size() == 0:
            return True
        else:
            return False

    def __str__(self):
        return self.stack

    def __repr__(self):
        return self.__str__()


mystack = Stack(20)
mystack.push(2)
mystack.push(4)
mystack.push(5)
mystack.push(6)
mystack.push(3)
for i in range(mystack.size()):
    print(mystack.stack[i])
mystack.pop()
mystack.pop()
print('_____________________________________')
for i in range(mystack.size()):
    print(mystack.stack[i])
mystack.pop()
print(mystack.size())
print(mystack.is_empty())
