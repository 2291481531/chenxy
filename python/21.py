#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Students:
    # 所有员工的基类
    empCount = 0

    def __init__(self, name, num , stu_class):
        self.name = name
        self.num = num
        self.stu_class = stu_class
        Students.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Students.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Num: ", self.num, ",stu_class:", self.stu_class)
c = Students("cxy", "02", "05")
s = Students("cy", "03", "05")
c.displayEmployee()
