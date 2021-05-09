from django.test import TestCase

from houses.utils import format_price, transform_params, transform_price


def test_price_format():
    assert format_price(1000000) == '$1.0M'
    assert format_price(1000) == '$1.0K'
    assert format_price(999999) == '$999.999K'


def test_transform_price():
    assert transform_price('$1.0M') == 1000000
    assert transform_price('$1.0K') == 1000
    assert transform_price('$999.999K') == 999999
