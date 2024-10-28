#!/usr/bin/env python3
"""takes two integer arguments"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """return a tuple of size two"""
    start = (page - 1) * page_size
    end = page * page_size
    return start, end


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
        pass

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(
            page, int) and page > 0, \
            "AssertionError raised when page and/or page_size are not ints"
        assert isinstance(
            page_size, int) and page > 0, \
            "AssertionError raised when page and/or page_size are not ints"
        assert isinstance(page == 0), "AssertionError raised with 0"
        assert isinstance(page_size == 0), "AssertionError raised with 0"
        assert isinstance(
            page < 0), "AssertionError raised with negative values"
        assert isinstance(
            page_size < 0), "AssertionError raised with negative values"

        start, end = index_range(page, page_size)

        dataset = self.dataset()

        if start >= len(dataset):
            return []

        return dataset[start:end]
