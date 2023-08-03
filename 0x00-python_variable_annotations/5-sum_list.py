#!/usr/bin/env python3
"""
    Write a type-annotated function sum_list which takes a list
    input_list of floats as argument and returns their sum as a float.
"""
import functools


def sum_list(input_list: list[float]) -> float:
    """
        Find sum of input list of float numbers
    """
    return functools.reduce(lambda a, b: a + b, input_list)
