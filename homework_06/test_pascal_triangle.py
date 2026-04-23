from homework_06.solutions import pascal_triangle


def test_pascal_triangle_zero_rows():
    assert pascal_triangle(0) == []


def test_pascal_triangle_one_row():
    assert pascal_triangle(1) == [[1]]


def test_pascal_triangle_three_rows():
    assert pascal_triangle(3) == [[1], [1, 1], [1, 2, 1]]


def test_pascal_triangle_five_rows_last_row():
    result = pascal_triangle(5)
    assert result[-1] == [1, 4, 6, 4, 1]


def test_pascal_triangle_rows_start_and_end_with_one():
    result = pascal_triangle(6)
    assert all(row[0] == 1 and row[-1] == 1 for row in result)
