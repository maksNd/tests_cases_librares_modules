import conftest
from utils import sum_func


def test_sum_func(two_numbers_sum):
    result = sum_func(two_numbers_sum[0], two_numbers_sum[1])
    assert result == 2
