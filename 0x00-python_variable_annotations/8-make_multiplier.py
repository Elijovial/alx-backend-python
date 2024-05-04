#!/usr/bin/env python3
"""a type-annotated make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Accepts a float and return a function that multiplies it"""
    return lambda x: x * multiplier
