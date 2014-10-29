#!/usr/bin/env python2
# coding=utf-8

import TypeUtils

__author__ = 'zero.liu'
__date__ = '14 - 10 - 27'


def convert_to_type_test():

    print TypeUtils.convert_to_type(['杭州西湖', ['北京']], unicode)

    print TypeUtils.convert_to_type(TypeUtils.convert_to_type(['杭州西湖', '123', 123], int), unicode)

    print TypeUtils.convert_to_type([['123', '中文'], 123], float)


if __name__ == '__main__':

    convert_to_type_test()
