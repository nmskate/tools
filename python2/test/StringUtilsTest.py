#!/usr/bin/env python2
# coding=utf-8

import TypeUtils
import StringUtils

__author__ = 'zero.liu'
__date__ = 14 - 10 - 27


def subtract_blank_test():
    print StringUtils.subtract_blank('''ab \t\n gda\\d''')
    print StringUtils.subtract_blank(None)
    print StringUtils.subtract_blank('')
    print StringUtils.subtract_blank(' a ')


def subtract_unprintable_test():
    str_test = '''ab \t\n gda\\d'''
    print StringUtils.subtract_unprintable(str_test)


def split_plus_test():
    separator_array_ = ['ab', ', ', ' ', 'e', '中文', ':', '|']
    str_ = 'abc,de fgh, ijk,lmn:op|qr中文st'

    separator_array_ = TypeUtils.convert_to_type(separator_array_, unicode)
    str_ = TypeUtils.convert_to_type(str_, unicode)

    print StringUtils.split_plus(str_, separator_array_)


if __name__ == '__main__':

    subtract_blank_test()

    split_plus_test()