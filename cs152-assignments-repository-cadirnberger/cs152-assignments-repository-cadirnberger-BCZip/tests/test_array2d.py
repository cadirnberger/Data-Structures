import pytest

from datastructures.array import Array
from datastructures.array2d import Array2D
from tests.car import Car, Make, Model, Color

ROWS = 3
COLS = 2

class TestArray2D:

    @pytest.fixture
    def array2d_numerical_uniform(self):
        array2d = Array2D.empty(ROWS, COLS, int)
        num = 0

        for row in range(len(array2d)):
            for col in range(len(array2d[row])):
                array2d[row][col] = num
                num += 1

        return array2d
    
    @pytest.fixture
    def array2d_cars_uniform(self):
        array2d_cars = Array2D.empty(ROWS, COLS, Car)
        
        vin_num = 0

        for row in range(len(array2d_cars)):
            for col in range(len(array2d_cars[row])):
                array2d_cars[row][col] = Car(vin=str(vin_num), make=Make.FORD, model=Model.FOCUS, color=Color.BLUE)
                vin_num += 1

        return array2d_cars

    def test_array2d_dimensions_should_3_by_2(self, array2d_numerical_uniform):
        assert len(array2d_numerical_uniform) == ROWS
        for row in array2d_numerical_uniform:
            assert len(row) == COLS

    def test_array2d_should_return_correct_values(self, array2d_numerical_uniform):
        expected = 0
        for row in range(len(array2d_numerical_uniform)):
            for col in range(len(array2d_numerical_uniform[row])):
                assert expected == array2d_numerical_uniform[row][col]
                expected += 1

    def test_array2d_should_return_correct_values_cars(self, array2d_cars_uniform):
        expected = 0
        for row in range(len(array2d_cars_uniform)):
            for col in range(len(array2d_cars_uniform[row])):
                assert array2d_cars_uniform[row][col].vin == str(expected)
                expected += 1

    def test_from_pylist2d_should_raise_value_error(self):
        with pytest.raises(ValueError):
            Array2D([1, 2, 3])  # type: ignore


    def test_from_pylist2d_should_return_correct_values_using_range(self):
        array2d = Array2D([[0, 1], [2, 3], [4, 5]])
        expected = 0
        for row in range(len(array2d)):
            for col in range(len(array2d[row])):
                assert expected == array2d[row][col]
                expected += 1
    
    def test_from_pylist2d_should_return_correct_values_using_iter(self):
        array2d = Array2D([[0, 1], [2, 3], [4, 5]])
        expected = 0
        for row in array2d:
            for item in row:
                assert expected == item
                expected += 1
    
    def test_from_pylist2d_should_return_correct_values_cars_using_range(self):
        array2d = Array2D([[Car(vin=str(i), make=Make.FORD, model=Model.FOCUS, color=Color.BLUE) for i in range(COLS)] for _ in range(ROWS)])
        
        for row in array2d:
            expected = 0
            for item in row:
                assert str(expected) == item.vin
                expected += 1

    def test_from_pylist2d_should_return_correct_values_cars_using_iter(self):
        array2d = Array2D([[Car(vin=str(i), make=Make.FORD, model=Model.FOCUS, color=Color.BLUE) for i in range(COLS)] for _ in range(ROWS)])
        
        for row in array2d:
            expected = 0
            for item in row:
                assert str(expected) == item.vin
                expected += 1
    
    def test_contains_should_return_true_for_existing_item(self, array2d_numerical_uniform):
        assert Array([2, 3], int) in array2d_numerical_uniform

    def test_contains_should_return_false_for_non_existing_item(self, array2d_numerical_uniform):
        assert Array([2, 4], int) not in array2d_numerical_uniform

    def test_length_should_return_correct_length(self, array2d_numerical_uniform):
        assert len(array2d_numerical_uniform) == ROWS

    def test_lengths_of_columns_should_return_correct_lengths(self, array2d_numerical_uniform):
        for row in array2d_numerical_uniform:
            assert len(row) == COLS
    
    def test_jagged_array_lengths_of_columns_should_return_correct_lengths(self):
        array2d = Array2D([[0, 1], [2, 3], [4]])
        assert len(array2d) == 3
        assert len(array2d[0]) == 2
        assert len(array2d[1]) == 2
        assert len(array2d[2]) == 1

    def test_modified_jagged_array_lengths_of_columns_should_return_correct_lengths(self):
        array2d = Array2D([[0, 1], [2, 3], [4]])
        array2d[2].append(5)
        assert len(array2d) == 3
        assert len(array2d[0]) == 2
        assert len(array2d[1]) == 2
        assert len(array2d[2]) == 2

    def test_slice_on_array2d_should_return_correct_values(self):
        array2d = Array2D([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        assert array2d[0:2] == Array2D([[0, 1, 2], [3, 4, 5]])
        assert array2d[1:3] == Array2D([[3, 4, 5], [6, 7, 8]])
        assert array2d[0:2][0:2] == Array2D([[0, 1, 2], [3, 4, 5]])
        assert array2d[1:3][1:3] == Array2D([[6, 7, 8]])
        assert array2d[0:2][0:2][0:2] == Array2D([[0, 1, 2], [3, 4, 5]])
        assert array2d[1:3][1:3][1:3] == Array2D([])

    def test_equal_should_be_true_for_same_array(self):
        array2d = Array2D([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        assert array2d == array2d

    def test_equal_should_be_true_for_equal_arrays(self):
        array2d1 = Array2D([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        array2d2 = Array2D([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        assert array2d1 == array2d2

    def test_equal_should_be_false_for_different_arrays(self):
        array2d1 = Array2D([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        array2d2 = Array2D([[0, 1, 2], [3, 4, 5], [6, 7, 9]])
        assert array2d1 != array2d2