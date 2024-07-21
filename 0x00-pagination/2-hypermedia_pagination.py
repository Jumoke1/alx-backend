#!/usr/bin/env python3
"""pagination"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for a given page and page size.

    Args:
    page (int): The current page number (1-indexed).
    page_size (int): The number of items per page.

    Returns:
    tuple: A tuple containing the start index and the end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


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
        """ get a page from the data set
            Args:
            page (int): The page number to retrieve (1-indexed).
            page_size (int): The number of items per page.

            Returns:
            List[List]: The list of rows for the specified page.
        """
        assert isinstance(page, int)and page > 0
        assert isinstance(page_size, int)and page_size > 0

        start_index, end_index = index_range(page, page_size)
        data = self.dataset()

        if start_index >= len(data):
            return []
        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """get information about a page """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        next_page = page + 1 if end_index < total_pages else None,
        prev_page = page - 1 if start_index > 1 else None,
        page_info = {
           "page_size": len(data),
           "page": page,
           "data": data,
           "next_page": next_page,
           "prev_page": prev_page,
           "total_pages": total_pages
        }
        return page_info
