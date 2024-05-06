#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Данная программа cоздает файл "newfile.txt" и записывает в него информацию об имени текущего пользователя и текущей
# директории. После этого проверяет существует ли файл с именем "ind3.txt". Если файл "ind3.txt" не существует,
# то переименовывает файл "newfile.txt" в "ind3.txt". В противном случае выводится сообщение "Файл уже существует".

import os

if __name__ == "__main__":
    with open("newfile.txt", "w") as f:
        f.write("Имя текущего пользователя: ")
        f.write(os.getlogin())
        f.write("\nТекущая дериктория: ")
        f.write(os.getcwd())
    ch = os.path.exists("ind3.txt")
    if not ch:
        os.rename("newfile.txt", "ind3.txt")
    else:
        print("Файл уже существует")
