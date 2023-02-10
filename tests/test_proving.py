from proving.proving import d, calculate_uncertanity
import pytest
import numpy as np


def test_n():
    assert d(20) == np.sqrt(20)


def test_calculate_uncertanity():
    """testing with  a x sett with 0.05% 'repetability'range of 5 measurment"""
    x = np.array([1000.00, 1000.00, 1000.00, 1000.25, 999.75])
    res = calculate_uncertanity(x)
    assert res["uncertanity_prcent"] == pytest.approx(0.0267, 0.001)
