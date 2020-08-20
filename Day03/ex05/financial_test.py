import re
import pytest
from financial import get_row


@pytest.fixture
def total_revenue():
    return get_row('MSFT', 'Total Revenue')


def test_invalid_ticker():
    with pytest.raises(ValueError, match='ticker does not exist'):
        get_row('AAAA', 'Total Revenue')


def test_invalid_row():
    with pytest.raises(ValueError, match='row does not exist'):
        get_row('MSFT', 'abcdef')


def test_return_type(total_revenue):
    assert isinstance(total_revenue, tuple)


def test_return_len(total_revenue):
    assert len(total_revenue) == 6


def test_return_elems_type(total_revenue):
    for elem in total_revenue:
        assert isinstance(elem, str)


def test_returns_row_name(total_revenue):
    assert total_revenue[0] == 'Total Revenue'


def test_returns_correct_values(total_revenue):
    for elem in total_revenue[1:]:
        assert re.match(r'\d{2,3},\d{3},000', elem)
