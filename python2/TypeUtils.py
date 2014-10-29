#!/usr/bin/env python2
# coding=utf-8

__author__ = 'zero.liu'
__date__ = '14 - 10 - 27'


from common import Charset


# 把元素中的字符串转换成指定编码，只转换字符串或list、set、tuple中的字符串
# charset_只能取 unicode, str, int, float
# example:
# convert_to_type(['杭州西湖', ['北京']], unicode) = [u'\u676d\u5dde\u897f\u6e56', [u'\u5317\u4eac']]
# convert_to_type(['杭州西湖', '123', 123], int) = ['\xe6\x9d\xad\xe5\xb7\x9e\xe8\xa5\xbf\xe6\xb9\x96', 123, 123]
# convert_to_type([['123', '中文'], 123], float) = [[123.0, '\xe4\xb8\xad\xe6\x96\x87'], 123.0]
def convert_to_type(element_, charset_):
    if element_ is None or charset_ is None:
        return element_

    convert_ = None
    if charset_ == unicode:
        convert_ = lambda _ele_: _ele_.decode(Charset.DEFAULT) if isinstance(_ele_, str) else None
    elif charset_ == str:
        convert_ = lambda _ele_: _ele_.encode(Charset.DEFAULT) if isinstance(_ele_, unicode) else None
    elif charset_ == int:
        convert_ = lambda _ele_: int(_ele_) if (isinstance(_ele_, (unicode, str)) and _ele_.isdigit()) or (
            isinstance(_ele_, (float, long, int))) else None
    elif charset_ == float:
        convert_ = lambda _ele_: float(_ele_) if (isinstance(_ele_, (unicode, str)) and _ele_.isdigit()) or (
            isinstance(_ele_, (float, long, int))) else None
    else:
        return element_

    # 内部私有函数，递归转换集合中的字符串
    def __convert_to_charset(_collection_):
        _array_temp_ = []
        for _ele_ in _collection_:
            _tmp_ = convert_(_ele_)
            if _tmp_ is not None:
                _array_temp_.append(_tmp_)
            elif isinstance(_ele_, (list, set, tuple)):
                _array_temp_.append(__convert_to_charset(_ele_))
            else:
                _array_temp_.append(_ele_)
        if isinstance(_collection_, set):
            _array_temp_ = set(_array_temp_)
        if isinstance(_collection_, tuple):
            _array_temp_ = tuple(_array_temp_)
        return _array_temp_

    temp_ = convert_(element_)
    if temp_ is not None:
        return temp_

    if isinstance(element_, (list, set, tuple)):
        return __convert_to_charset(element_)

    return element_