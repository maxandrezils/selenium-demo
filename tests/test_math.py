def add_two_numbers(a, b):
    return a + b


def test_add_two_numbers():
    assert add_two_numbers(1, 2) == 3, "Should be 3"


def test_add_large_numbers():
    assert add_two_numbers(100, 200) == 300, "Should be 300"
