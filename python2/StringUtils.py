#!/usr/bin/env python2
# coding=utf-8

__author__ = 'zero.liu'
__date__ = '14 - 10 - 27'

import re


# 去除字符串中所有空白字符[<空格>\t\r\n\f\v]
# example:
# subtract_blank('''ab \t\n gda\d''') = 'abgda\d'
# subtract_blank(' a ') = 'a'
def subtract_blank(string_):
    if type(string_) != str:
        string_ = str(string_)
    return re.sub(r'\s', '', string_)


# 去除所有不可打印字符[\t\r\n\f\v]
# example:
# subtract_unprintable('''ab \t\n gda\d''') = 'ab  gda\d'
def subtract_unprintable(string_):
    if type(string_) != str:
        string_ = str(string_)
    return re.sub(r'\t|\r|\n|\f', '', string_)


# 将一个字符串按给定的数组分割
# 支持分隔符是多个字符，如按['中国', '..']分割
# example:
# split_plus('abc,d e,f.g.h', [',', ' ', '.', 'bc']) = ['a', 'd', 'e', 'f', 'g', 'h']
def split_plus(string_, separator_array_):
    if string_ is None or string_ == '':
        return []

    if separator_array_ is None or len(separator_array_) <= 0:
        # 默认按逗号空格分割
        separator_array_ = [',', ' ']

    #过滤掉分隔符列表中的空元素,否则会出现死循环
    separator_array_ = filter(lambda x: x is not None and x != '', separator_array_)

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