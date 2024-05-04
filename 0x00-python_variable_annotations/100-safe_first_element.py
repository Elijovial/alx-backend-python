#!/usr/bin/env python3
"""a duck typed function"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """unknown type element"""
    if lst:
        return lst[0]
    else:
        return None
