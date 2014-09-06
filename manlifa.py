#-*- coding: UTF-8 -*-
dic = dict()
string = input("物品的重量， 价值")
key = int(string[0:1])
value = int(string[1])
dic.setdefault(key,value)
print(dic)