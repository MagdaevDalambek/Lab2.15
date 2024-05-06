#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Написать программу, которая считывает из текстового файла три предложения и выводит их в обратном порядке.

if __name__ == "__main__":
    with open("ind1.txt", "r") as txt:
        content = txt.readlines()[0:3]
        content.reverse()
        for line in content:
            print(line)
