import pytest
from . import client


def test_client_for_income_of_10000_dollars():
    tax = client.calculate_tax_for_user(10000)
    assert tax == 1345