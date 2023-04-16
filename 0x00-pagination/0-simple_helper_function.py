#!/usr/bin/env python3

'''
A simple helper function
'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    '''Function that returns start and end index of a page'''
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
