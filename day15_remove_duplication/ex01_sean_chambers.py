#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

# 消除冗余
# 这大概是处理一个方法在多处使用时最常见的重构。
# 如果不加以注意的话，你会慢慢地养成重复的习惯。
# 开发者常常由于懒惰或者在想要尽快生成尽可能多的代码时，向代码中添加很多重复的内容。
# 我想也没必要过多解释了吧，直接看代码把。
import time


class MedicalRecord:
    def __init__(self, data_arrived, archived):
        self.__data_arrived = data_arrived
        self.__archived = archived

    @property
    def data_arrived(self): return self.__data_arrived

    @property
    def archived(self): return self.__archived

    def archive_record(self):
        self.__archived = True
        self.__data_arrived = time.localtime()

    def close_record(self):
        self.__archived = True
        self.__data_arrived = time.localtime()


# 我们用共享方法的方式来删除重复的代码。
# 看!没有重复了吧?
# 请务必在必要的时候执行这项重构。
# 它能有效地减少 bug，因为你不会将有 bug 的代码复制/粘贴到各个角落。

class MedicalRecord:
    def __init__(self, data_arrived, archived):
        self.__data_arrived = data_arrived
        self.__archived = archived

    @property
    def data_arrived(self): return self.__data_arrived

    @property
    def archived(self): return self.__archived

    def archive_record(self):
        self.switch_to_archived()

    def close_record(self):
        self.switch_to_archived()

    def switch_to_archived(self):
        self.__archived = True
        self.__data_arrived = time.localtime()
