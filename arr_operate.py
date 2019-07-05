# -*- coding: UTF-8 -*-

arr1 = [1, 4, 6, 8, 3]
arr2 = ['hello', 'morning', 'afternoon', 'dog']
# arr2.sort() # order with alphebates
# print(arr2)

class OperateArr(object):

    def multiTwo(num):
        return num ** 2



class OperateNum(object):

    # judge whether the two numbers are relatively prime
    def isTwoNumPrime(self, a, b):
        if(a<b):
            t=a;a=b;b=t;
        while(a%b):
            t=b;
            b=a%b;
            a=t;
        return b


# opetarerArr1 = OperateArr
# operateNum1 = OperateNum
# newArr = list(map(opetarerArr1.multiTwo, arr1))
# print(newArr)
# print(operateNum1.isTwoNumPrime(5, 6))
