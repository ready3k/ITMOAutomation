def test_hw_function_one():
    assert ('home', 'work') == ('home', 'work')


def test_hw_function_two():
    assert 'QA' != 'QC'


def test_hw_function_three():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)
