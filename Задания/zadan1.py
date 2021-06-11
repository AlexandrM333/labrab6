#!/usr/bin/env python3
# -*- coding: utf-8 -*-

mylist = ['мяч', 'палка', 'луна', 'садик', 'дерево', 'небо']
s = input("Введите элемент списка ")

if s not in mylist:
    print("Такого элемента в списке нет")
else:
    print(mylist.index(s))
