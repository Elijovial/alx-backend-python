#!/usr/bin/env python3
"""type-annotated sum mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Accepts list of integers and floats and returns
        their sum as float"""
    a: float = 0.0
    for x in mxd_lst:
        a += x
    return a
