from pytest import raises


def test_main():
    with raises(TypeError):
        raise TypeError
