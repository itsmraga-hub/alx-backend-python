#!/usr/bin/env python3
"""
    Write a type-annotated function make_multiplier that takes a float
    multiplier as argument and returns a function that multiplies
    a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Takes in a float and returns a function
    """

    def func(n: float) -> float:
        """
            Multiplies a float n, by multiplier
        """
        return float(n * multiplier)

    return func
