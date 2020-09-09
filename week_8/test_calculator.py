"""This is our calculator test file"""
import pytest
from . import calculator

def test_one_plus_one_equals_two():
    assert 1 + 1 == 2

def test_zero_income_equals_zero_tax():
    tc = calculator.TaxCalculator(0)
    tax = tc.calculate_tax()
    assert tax == 0

def test_500_dollars_income_equals_52point5():
    tc = calculator.TaxCalculator(500)
    tax = tc.calculate_tax()
    assert tax == 52.7

@pytest.mark.skip('Temporarily skipped')
def test_assert_false():
    assert False
