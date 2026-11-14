
import pytest
from main import decide_action


def test_move():
    assert decide_action(3.0) == "MOVE"


def test_stop():
    assert decide_action(1.2) == "STOP"


def test_boundary():
    assert decide_action(1.5) == "STOP"


def test_zero_distance():
    assert decide_action(0.0) == "STOP"


def test_invalid_distance():
    with pytest.raises(ValueError):
        decide_action(-1.0)
