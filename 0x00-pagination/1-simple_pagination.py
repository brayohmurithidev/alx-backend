#!/usr/bin/env python3

'''
A simple helper function
'''
from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple:
    '''Function that returns start and end index of a page'''
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0, "a must be an integer"
        assert isinstance(page_size, int) and page_size > 0,\
            "b must be an integer"
        result = index_range(page, page_size)
        if result[0] >= len(self.dataset()) or result[1] <= result[0]:
            return []
        else:
            a, b = result[0], result[1]
            data = self.dataset()
            return data[a:b]
