import pytest
from fizbuzz import fizbuzz2 as fizbuzz


@pytest.mark.parametrize("num", (1, 2))
def test_should_return_n_if_number_is_not_divisible_by_3_and_5(num):
    assert str(num) == fizbuzz(num)


@pytest.mark.parametrize("num", (3, 6))
def test_should_return_Fizz_if_number_is_divisible_by_3(num):
    assert "Fizz" == fizbuzz(num)

@pytest.mark.parametrize("num", (5, 10))
def test_should_return_Buzz_if_number_is_divisible_by_5(num):
    assert "Buzz" == fizbuzz(num)

@pytest.mark.parametrize("num", (15, 30))
def test_should_return_FizzBuzz_if_number_is_divisible_by_3_and_by_5(num):
    assert "FizzBuzz" == fizbuzz(num)
