# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Array_interface
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
size    - 容量

"""

import ctypes


class Array:
    def __init__(self, size):
        assert size > 0, '数组长度必须大于0'
        self._size = size
        PyArrayType = ctypes.py_object *size
        self._elements = PyArrayType()
        self.clear(None)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        assert index >=0 and  index <len(self), '超出索引范围'
        return self._elements[index]

    def __setitem__(self, index, value):
        assert index>=0 and index < len(self), '超出索引范围'
        self._elements[index] = value

    def clear(self, value):
        """ 设置每个元素为value"""
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        return _ArrayIterator(self._elements)

class _ArrayIterator:
    def __init__(self, items):
        self._items = items
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._items):
            value = self._items[self._index]
            self._index +=1
            return value
        else:
            raise StopIteration

