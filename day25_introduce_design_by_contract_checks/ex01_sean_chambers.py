#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""


# 引入契约式设计
# 契约式设计(DBC，Design By Contract)定义了方法应该包含输入和输出验证。
# 因此，可以确保所有的工作都是基于可用的数据，并且所有的行为都是可预料的。
# 否则，将返回异常或错误并在方法中进行处理。要了解更多关于 DBC 的内容，可以访问 wikipedia。
# 在我们的示例中，输入参数很可能为 null。
# 由于没有进行验证，该方法最终会抛出 NullReferenceException。
# 在方法最后，我们也并不确定是否为用户返回了一个有效的 decimal，这可能导致在别的地方引入其他方法。

class CashRegister:
    def total_order(self, products, customer):
        order_total = sum([p.price for p in products])
        customer.balance += order_total
        return order_total


# 在此处引入 DBC 验证是十分简单的。
# 首先，我们要声明 customer 不能为 null，并且在计算总值时至少要有 一个 product。
# 在返回订单总值时，我们要确定其值是否有效。
# 如果此例中任何一个验证失败，我们将以友好的方式抛出相应的异常来描述具体信息，而不是抛出一个晦涩的 NullReferenceException。

class CashRegister:
    def total_order(self, products, customer):
        if customer is None:
            raise Exception('customer cannot be none')
        if len(products) == 0:
            raise Exception('at least one product to total')
        order_total = sum([p.price for p in products])
        customer.balance += order_total
        if order_total == 0:
            raise Exception('order total should not be zero')
        return order_total

# 在验证过程中确实增加了不少代码，你也许会认为过度使用了 DBC。
# 但我认为在大多数情况下，处理这些棘手的问题所做的努力都是值得的。
# 追踪无详细内容的 NullReferenceException 的确不是什么美差。
