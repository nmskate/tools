#!/usr/bin/env python2
# coding=utf-8

__author__ = 'zero.liu'
__date__ = '14 - 10 - 27'


# 统计一个元素在一个列表中出现的次数
def contain_counts(element_array_, element_):
    if element_array_ is None or len(element_array_) <= 0:
        return 0

    count_ = 0
    for array_item in element_array_:
        if array_item == element_:
            count_ += 1
    return count_


# 获取一个数组中出现次数最多的元素及出现次数
# 如果有多个返回一个列表
# 返回结果形如：(['aaa'], 3) 或 (['a', 'b'], 3)
def find_max_times_element(array_):
    if array_ is None or len(array_) <= 0:
        return [], 0

    # 把元素和出现的次数放到字典中
    tmp_dict_ = {}
    for item_ in array_:
        if tmp_dict_.get(item_) is None:
            tmp_dict_[item_] = 0
        tmp_dict_[item_] += 1

    # 先找出最大次数
    max_times_ = 0
    for _key_, _value_ in tmp_dict_.items():
        if _value_ > max_times_:
            max_times_ = _value_

    # 再找出最大元素
    result_item_ = []
    for _key_, _value_ in tmp_dict_.items():
        if _value_ == max_times_:
            result_item_.append(_key_)
    return result_item_, max_times_
