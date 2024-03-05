# Tests will be written once the application is somewhat working.
from main import cli
from pytest import raises


def test_main():
    with raises((TypeError, AttributeError)):
        cli(test=NotImplemented)
