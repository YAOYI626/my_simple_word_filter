#!/usr/bin/env python
# -*- coding: utf-8 -*-


def my_filter():
    sensitivity = set()
    with open("敏感词.txt", "r") as sword_file:
        for line in sword_file.readlines():
            word = line.replace("\n", "")
            if word not in sensitivity:
                sensitivity.add(word)

    lth = len(original_txt)
    number = range(lth)
    bool_string = [True] * (lth + 1)
    re_string = ""
    original_file.close()

    for i in number:
        for i_i in range(5):
            if original_txt[i:i + i_i + 1] in sensitivity:
                bool_string[i:i_i + i + 1] = [False] * (i_i + 1)
                number = range(i + i_i + 1, lth)

    for j in range(lth):
        if bool_string[j]:
            re_string += original_txt[j]
        elif bool_string[j] != bool_string[j + 1]:
            re_string += "[-1s]"

    with open("re_%s.txt" % original_file_name, "w", encoding="utf-8") as new_file:
        new_file.write(re_string)


original_file_name = input("请将待过滤文本文件文件放置在此目录下并输入文件名：")

try:
    original_file = open("%s.txt" % original_file_name)
    original_txt = original_file.read()
    my_filter()
    print("Done")

except UnicodeDecodeError:
    original_file = open("%s.txt" % original_file_name, encoding="utf-8")
    original_txt = original_file.read()
    my_filter()
    print("您输入的文本文件为GBK编码\nDone")

except FileNotFoundError:
    print("您输入的文件不存在于当前目录下")

input("请按回车键以结束程序")
