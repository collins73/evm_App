import EVM
import pytest

import EVM


def test_costVariance():
    assert EVM.costVariance(6000) == 3000


def test_costPerformanceIndex():
    assert EVM.costPerformanceIndex(200000) == .7


def test_scheduleVariance():
    assert EVM.scheduleVariance(16000, 8000) == 8000


def test_schedulePerformanceIndex():
    assert EVM.schedulePerformanceIndex(16000, 8000) == 2


