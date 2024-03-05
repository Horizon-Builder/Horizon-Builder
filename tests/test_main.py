# Tests will be written once the application is somewhat working.
from pytest import raises


def test_main():
    with raises(TypeError):
        raise TypeError
