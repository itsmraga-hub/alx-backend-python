#!/usr/bin/env python3
"""
    Write a type-annotated function sum_mixed_list which takes a list
    mxd_lst of integers and floats and returns their sum as a float.
"""
import functools


def sum_mixed_list(mxd_lst: list(int|float)): -> float:
    """
        A function that adds both ints and floats
        and returns a float
    """
    return functools.reduce(lambda a, b: a + b, mxd_lst)
