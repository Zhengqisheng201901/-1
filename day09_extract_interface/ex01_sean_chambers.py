#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

# 提取接口
# 今天我们来介绍一个常常被忽视的重构:提取接口。
# 如果你发现多于一个类使用另外一个类的某些方法，引入接口解除这种依赖往往十分有用。
# 该重构实现起来非常简单，并且能够享受到松耦合带来的好处。
from abc import ABCMeta, abstractmethod


class ClassRegistration:
    def __init__(self, total):
        self.__total = total

    @property
    def total(self): return self.__total

    def create(self): pass

    def transfer(self): pass


class RegistrationProcessor:
    @staticmethod
    def process_registration(class_registration):
        class_registration.create()
        return class_registration.total


# 在下面的代码中，你可以看到我提取出了消费者所使用的两个方法，并将其置于一个接口中。
# 现在消费者不必关心和了解实现了这些方法的类。
# 我们解除了消费者与实际实现之间的耦合，使其只依赖于我们创建的契约。

class IClassRegistration(metaclass=ABCMeta):
    def __init__(self, total):
        self.__total = total

    @property
    def total(self): return self.__total

    @abstractmethod
    def create(self): pass


class ClassRegistration(IClassRegistration):
    def create(self): pass

    def transfer(self): pass


class RegistrationProcessor:
    @staticmethod
    def process_registration(class_registration):
        class_registration.create()
        return class_registration.total
