#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""


# 分离职责
# 把一个类的多个职责进行拆分，这贯彻了 SOLID 中的单一职责原则(SRP)。
# 尽管对于如何划分职责经常存在争论，但应用这项重构还是十分简单的。
# 我这里并不会回答划分职责的问题，只是演示一个结构清晰的示例，将类划分为多个负责具体职责的类。

class Customer:
    def __init__(self):
        self.latefees = []
        self.videos = []


class Video:
    def payfee(self, fee): pass

    def rent_video(self, video, customer):
        customer.videos.append(video)

    def calculate_balance(self, customer):
        return sum(customer.latefees)


# 如你所见，Video 类包含两个职责，一个负责处理录像租赁，另一个负责管理管理用户的租赁总数。
# 要分离职责，我们可以将用户的逻辑转移到用户类中。

class Customer:
    def __init__(self):
        self.latefees = []
        self.videos = []

    def payfee(self, fee): pass

    def calculate_balance(self):
        return sum(self.latefees)


class Video:
    def rent_video(self, video, customer):
        customer.videos.append(video)
