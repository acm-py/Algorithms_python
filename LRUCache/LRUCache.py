# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     LRUCache
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
LRU -> 是一种缓存剔除策略，当缓存空间不够的时候需要一种方式剔除key
LRU -> Least-Recently-Used 替换掉最近最少使用的
LFU -> Least-Frequently-Used 替换掉最近使用次数最少的
LRU 通过使用一个循环双端队列不断把最新访问的key 放到表头实现
"""
# 字典用来缓存，循环双端链表用来记录访问顺序
# 利用Python内置的dict + collections.OrderedDict实现
# dict用来当做k/v键值对的缓存
# OrderedDict用来实现更新最近访问的key
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity=128):
        self.od = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.od:
            val = self.od[key]
            self.od.move_to_end(key)
            return val
        else:
            return -1

    def put(self, key, value):
        if key in self.od:
            del self.od[key]
            self.od[key] = value
        else: # 插入
            self.od[key] = value
            if len(self.od) > self.capacity:
                self.od.popitem(last=False) # 删除最早的元素


