#!/usr/bin/env python2
# coding=utf-8

import ArrayUtils

__author__ = 'zero.liu'
__date__ = 14 - 10 - 27


def contain_counts_test():
    print ArrayUtils.contain_counts([1, 2, 3, 4, 5, 4, 2, 2, 1], 1)
    print ArrayUtils.contain_counts([1, 2, 3, 4, 5, 4, 2, 2, '1'], '1')
    print ArrayUtils.contain_counts([1, 2, 3, 4, 5, 4, 2, 2, None], None)
    print ArrayUtils.contain_counts(None, 1)
    print ArrayUtils.contain_counts([], None)
    print ArrayUtils.contain_counts([], 1)


def find_max_times_element_test():
    print ArrayUtils.find_max_times_element([1, 3, 3, 4, 5, 4, 2, 2, 1])
    print ArrayUtils.find_max_times_element(None)
    print ArrayUtils.find_max_times_element([None, None])


if __name__ == '__main__':

    contain_counts_test()

    find_max_times_element_test()