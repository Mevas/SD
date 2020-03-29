import random
from unittest import TestCase

from sorts import Sorter

tests = [
    [123, 321, 222, 782, 100, 7214],
    [1, 2, 3, 4],
    [4, 3, 2, 1],
    [1],
    [],
    [3, 3, 3, 1, 1, 3, 3, 3],
    [1000000000, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    random.sample(range(101), 100),
]

with open('tests.txt', 'r') as f:
    for test in f.readlines():
        n, limit = [int(x) for x in test.strip().split()]
        tests.append([random.randint(0, limit) for _ in range(n)])


class TestSorts(TestCase):
    def setUp(self):
        self.sorter = Sorter()
        self.test_cases = tests

        self.sorter.start_timer()

    def tearDown(self):
        print()

    @staticmethod
    def is_sorted(result, test_array):
        return result == sorted(test_array)

    def test_bubble(self):
        for index, test in enumerate(self.test_cases):
            bubble = self.sorter.bubble_sort(test)
            print(f'Bubble sort takes {self.sorter.end_timer()}s for test case {index}  ({len(test)} elements in the range {min(test, default=None), max(test, default=None)})')

            self.assertTrue(self.is_sorted(bubble, test), f'Bubble sort does not work on test case {test} - output is {bubble}')

    def test_count(self):
        for index, test in enumerate(self.test_cases):
            count = self.sorter.count_sort(test)
            print(f'Count sort takes {self.sorter.end_timer()}s for test case {index}  ({len(test)} elements in the range {min(test, default=None), max(test, default=None)})')

            self.assertTrue(self.is_sorted(count, test), f'Count sort does not work on test case {test} - output is {count}')

    def test_radix(self):
        for index, test in enumerate(self.test_cases):
            # Base 10
            radix = self.sorter.radix_sort(test)
            print(f'Radix sort (base 10) takes {self.sorter.end_timer()}s for test case {index}  ({len(test)} elements in the range {min(test, default=None), max(test, default=None)})')

            self.assertTrue(self.is_sorted(radix, test), f'Radix sort does not work on test case {test} - output is {radix}')

            # Base 256
            self.sorter.start_timer()
            radix = self.sorter.radix_sort(test, base=256)
            print(f'Radix sort (base 256) takes {self.sorter.end_timer()}s for test case {index}  ({len(test)} elements in the range {min(test, default=None), max(test, default=None)})')

            self.assertTrue(self.is_sorted(radix, test), f'Radix in base 256 sort does not work on test case {test} - output is {radix}')

    def test_merge(self):
        for index, test in enumerate(self.test_cases):
            merge = self.sorter.merge_sort(test)
            print(f'Merge sort takes {self.sorter.end_timer()}s for test case {index}  ({len(test)} elements in the range {min(test, default=None), max(test, default=None)})')

            self.assertTrue(self.is_sorted(merge, test), f'merge sort does not work on test case {test} - output is {merge}')

    def test_quick(self):
        for index, test in enumerate(self.test_cases):
            quick = self.sorter.quick_sort(test)
            print(f'Quick sort takes {self.sorter.end_timer()}s for test case {index}  ({len(test)} elements in the range {min(test, default=None), max(test, default=None)})')

            self.assertTrue(self.is_sorted(quick, test), f'quick sort does not work on test case {test} - output is {quick}')

    # Test creat doar pentru a compara vitezele
    def test_native(self):
        for index, test in enumerate(self.test_cases):
            self.sorter.native_sort(test)
            print(f'Native sort takes {self.sorter.end_timer()}s for test case {index}  ({len(test)} elements in the range {min(test, default=None), max(test, default=None)})')
