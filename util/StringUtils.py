#!/usr/bin/env python2
# coding=utf-8

__author__ = 'zero.liu'
__date__ = 14 - 10 - 27

import re


# 去除字符串中所有空白字符[<空格>\t\r\n\f\v]
def subtract_blank(string_):
    if type(string_) != str:
        string_ = str(string_)
    return re.sub(r'\s', '', string_)


# 去除所有不可打印字符[\t\r\n\f\v]
def subtract_unprintable(string_):
    if type(string_) != str:
        string_ = str(string_)
    return re.sub(r'\t|\r|\n|\f', '', string_)


# 将一个字符串按给定的数组分割
# 比如将 'abc,d e,f.g.h' 按 [',', ' ', '.'] 分割，结果就是 ['abc','d','e','f','g','h']
# 支持分隔符是多个字符，如按['中国', '..']分割
def split_plus(string_, separator_array_):
    if separator_array_ is None or len(separator_array_) <= 0:
        # 默认按逗号空格分割
        separator_array_ = [',', ' ']

    if string_ is None or string_ == '':
        return []

    len_ = len(string_)
    start_index_ = 0
    result_str_array = []
    while start_index_ <= len_:
        min_index = len_
        cur_separator_len_ = 1
        is_end = True
        for item_ in separator_array_:
            min_index_temp_ = string_.find(item_, start_index_)
            if min_index_temp_ >= 0:
                is_end = False
            if min_index_temp_ != -1 and min_index_temp_ < min_index:
                min_index = min_index_temp_
                cur_separator_len_ = len(item_)
        if min_index > start_index_ and min_index != len_:
            result_str_array.append(string_[start_index_:min_index])
        if is_end:
            result_str_array.append(string_[start_index_:])
            break
        start_index_ = min_index + cur_separator_len_
    return result_str_array

