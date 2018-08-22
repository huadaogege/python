#!/usr/local/python
# -*- coding:UTF-8 -*-

print 'hello world!'

# 创建类

class Employee(object):
    '所有员工的基类'
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total employee ", Employee.empCount

    def displayEmployee(self):
        print "Name:", self.name, "salary:", self.salary

# 创建实例

employee1 = Employee("cuiyuguan", 200000)
employee1.displayCount()
employee1.displayEmployee()

employee2 = Employee("qianhao", 100000)
employee2.displayCount()
employee2.displayEmployee()

# 为类添加属性
employee1.age = 27
employee2.height = 165

# 访问对象的属性方法
if hasattr(employee1, 'age'):
    print getattr(employee1, 'age')
if hasattr(employee2, 'height'):
    print getattr(employee2, 'height')

# python内置类属性
# __doc__:类的文档字符串
print "Employee.__doc__:", Employee.__doc__
# __dict__:类的属性
print "Employee.__dict__:", Employee.__dict__
# __name__:类型
print "Employee.__name__:", Employee.__name__
# __module__:模块
print "Employee.__module__:", Employee.__module__

# 对象销毁（垃圾回收）