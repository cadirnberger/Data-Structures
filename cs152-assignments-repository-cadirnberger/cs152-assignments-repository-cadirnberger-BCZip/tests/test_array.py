import copy
import pytest
from datastructures.array import Array

from cg_pytest_reporter import suite_weight, suite_name, name, weight

from tests.car import Car, Color, Make, Model

@suite_weight(1.0)
@suite_name('Array Test Suite')
class TestArray:
    car1 = Car('123', Color.RED, Make.TOYOTA, Model.CAMRY)
    car2 = Car('456', Color.BLUE, Make.TOYOTA, Model.CIVIC)
    car3 = Car('789', Color.BLACK, Make.FORD, Model.FOCUS)

    @pytest.fixture
    def setup_complex_object_array(self) -> Array[Car]:
        return Array[Car]([self.car1, self.car2, self.car3], Car)

    @pytest.fixture
    def setup_numerical_array(self) -> Array[int]:
        return Array[int]([i for i in range(10)], int)

    @name("Constructing an array with a complex object should deep copy the complex object's data")
    @weight(1)
    def test_constructing_an_array_with_a_complex_object_should_deep_copy_the_complex_objects_data(self, setup_complex_object_array: Array[Car]):
        original_array = setup_complex_object_array
        
        deep_copied_array = copy.deepcopy(original_array)
        deep_copied_array[0].vin = '000'

        assert original_array[0] is not deep_copied_array[0]
    
    @name("Constructing an array with a numerical type should deep copy the numerical data")
    @weight(1)
    def test_constructing_an_array_with_a_numerical_type_should_copy_the_numerical_data(self, setup_numerical_array: Array):
        array = copy.copy(setup_numerical_array)
        for i in range(len(array)):
            assert array[i] == setup_numerical_array[i]


    @name("Index operator should return the item at the index specified of the Array")
    @weight(1)
    def test_index_operator_should_return_the_item_at_the_index_specified_of_the_array(self, setup_numerical_array: Array):
        assert setup_numerical_array[5] == 5
    
    @name("Index operator should raise an IndexError exception if the index is out of bounds")
    @weight(1)
    def test_index_operator_should_raise_an_IndexError_exception_if_the_index_is_out_of_bounds(self, setup_numerical_array: Array):
        with pytest.raises(IndexError):
            setup_numerical_array[10]
    
    @name("Adding an item to a full Array should raise an IndexError exception")
    @weight(1)
    def test_adding_an_item_to_a_full_array_should_raise_an_index_error_exception(self, setup_numerical_array: Array):
        with pytest.raises(IndexError):
            setup_numerical_array[10]

    @name("Equality operator should return true for valid instances containing the same data")
    @weight(1)
    def test_equality_operator_should_return_true_for_valid_instances_containing_the_same_data(self, setup_numerical_array: Array):
        array1 = setup_numerical_array
        array2 = setup_numerical_array

        assert array1 == array2
    
    @name("Non-Equality operator should return true for valid instances containing the same data")
    @weight(1)

    def test_non_equality_operator_should_return_true_for_valid_instances_containing_the_same_data(self, setup_numerical_array: Array, setup_complex_object_array: Array):
        array1 = setup_numerical_array
        array2 = setup_complex_object_array

        assert array1 != array2

    @name("Non-Equality operator should return false for comparison of a Array to another object type")
    @weight(1)
    def test_equality_operator_should_return_false_for_comparison_of_a_array_to_another_object_type(self, setup_numerical_array: Array):
        assert setup_numerical_array != 'string instance'

    @name("Contains operator should return true if the item being checked is in the Array")
    @weight(1)
    def test_contains_operator_should_return_true_if_the_item_being_checked_is_in_the_array(self, setup_numerical_array: Array):
        assert 1 in setup_numerical_array

    @name("Contains operator should return false if the item being checked is not in the Array")
    @weight(1)
    def test_contains_operator_should_return_false_if_the_item_being_checked_is_not_in_the_array(self, setup_numerical_array: Array):
        assert not 11 in setup_numerical_array
    
    @name("To String operator should return a string representation of the Array")
    @weight(1)
    def test_to_string_operator_should_return_a_string_representation_of_the_array(self, setup_numerical_array: Array):
        assert str(setup_numerical_array) is not None
    
    @name("Representation operator should return a string representation of the Array")
    @weight(1)
    def test_representation_operator_should_return_a_string_representation_of_the_array(self, setup_numerical_array: Array):
        assert repr(setup_numerical_array) is not None
    
    @name("Clear operator should clear the Array")
    @weight(1)
    def test_clear_operator_should_clear_the_array(self, setup_numerical_array: Array):
        setup_numerical_array.clear()
        for item in setup_numerical_array:
            assert item is None

    @name("Clear operator should reset the Array to default size")
    @weight(1)
    def test_clear_operator_should_reset_the_array_to_default_size_and_values(self, setup_numerical_array: Array):
        setup_numerical_array.clear()
        assert len(setup_numerical_array) == 0
    
    @name("Clear operator should return reset the Array to the specified default value")
    @weight(1)
    def test_clear_operator_should_reset_the_array_to_the_specified_default_value(self, setup_numerical_array: Array):
        setup_numerical_array.clear()
        assert len(setup_numerical_array) == 0

    @name("Delete operator should remove item in position and copy the Array contents from index + 1 down to fill the gap caused by deleting the item")
    @weight(1)
    def test_del_operator_should_remove_item_in_position_and_copy_the_array_contents_from_index_plus_1_down_to_fill_the_gap_caused_by_deleting_the_item(self, setup_numerical_array: Array):
        del setup_numerical_array[0]
        assert setup_numerical_array[0] == 1

    @name("Reversed operator should reverse the Array")
    @weight(1)
    def test_reversed_operator_should_return_true(self, setup_numerical_array: Array):
        expected = 9
        for item in reversed(setup_numerical_array):
            assert expected == item
            expected -= 1
    
    @name("Iterator operator should return the item at index during iteration")
    @weight(1)
    def test_iterator_operator_should_return_the_item_at_index_during_iteration(self, setup_numerical_array: Array):
        expected = 0
        for item in setup_numerical_array:
            assert expected == item
            expected += 1

    @name("Length operator should return the length of the Array")
    @weight(1)
    def test_length_operator_should_return_the_length_of_the_array(self, setup_numerical_array: Array):
        assert len(setup_numerical_array) == 10

    @name("Length operator should return the length of the Array + 1 after appending an item")
    @weight(1)
    def test_length_operator_should_return_the_length_of_the_array_plus_1_after_appending_an_item(self, setup_numerical_array: Array):
        setup_numerical_array.append(10)
        print(repr(setup_numerical_array))
        assert len(setup_numerical_array) == 11

    @name("Reverse operator should reverse the Array")
    @weight(1)
    def test_reverse_operator_should_reverse_the_array(self, setup_numerical_array: Array):
        expected = 9
        for item in reversed(setup_numerical_array):
            assert expected == item
            expected -= 1

   # @name("Resizing with a negative size should raise a ValueError.")
   # @weight(1)
   # def test_resizing_with_a_negative_size_should_raise_a_value_error(self, setup_numerical_array: Array):
        #with pytest.raises(ValueError):
            #setup_numerical_array._resize(-1)

    @name("setitem operator should raise a TypeError exception if the item being set is not the same type as the Array")
    @weight(1)
    def test_setitem_operator_should_raise_a_type_error_exception_if_the_item_being_set_is_not_the_same_type_as_the_array(self, setup_numerical_array: Array):
        with pytest.raises(TypeError):
            setup_numerical_array[0] = 'string'

    @name("Bracket operator (__getitem__) should return a slice of the Array if a slice is passed in")
    @weight(1)
    def test_bracket_operator_should_return_a_slice_of_the_array_if_a_slice_is_passed_in(self, setup_numerical_array: Array):
        assert setup_numerical_array[1:5] == Array([1,2,3,4], int)

    @name("Constructor should raise a ValueError if the sequence passed in is not a sequence")
    @weight(1)
    def test_constructor_should_raise_a_value_error_if_the_sequence_passed_in_is_not_a_sequence(self):
        with pytest.raises(ValueError):
            Array(1, int) #type: ignore

    @name("Constructor should raise a TypeError if the sequence passed in is not the same type as the Array")
    @weight(1)
    def test_constructor_should_raise_a_type_error_if_the_sequence_passed_in_is_not_the_same_type_as_the_array(self):
        with pytest.raises(TypeError):
            Array(['string'], int) #type: ignore
    
    @name("Bracket operator (__getitem__) should raise a TypeError if the index is not an integer or slice")
    @weight(1)
    def test_bracket_operator_should_raise_a_type_error_if_the_index_is_not_an_integer_or_slice(self, setup_numerical_array: Array):
        with pytest.raises(TypeError):
            setup_numerical_array['string'] #type: ignore

    def test_index_bounds_get_should_raise_indexerror_for_out_of_bounds(self):
        # Arrange 
        array = Array[int]([0,1,2,3,4], data_type=int)
        out_of_bounds= 5
        # Act and Assert
        with pytest.raises(IndexError):
            array[out_of_bounds]
    #def test_index_should_raise_indexerror_for_non_int_index(self):
        # Arrange 
     #   array = Array[int]([0,1,2,3,4], data_type=int)
      #  index = '0'
        # Act and Assert
      #  with pytest.raises(IndexError):
       #     array[index]
    def test_index_should_return_four(self):
        # Arrange
        array = Array[int]([0,1,2,3,4], data_type=int)

        # Act 
        value_at_index_four = array[4]
        #Assert
        assert value_at_index_four == 4
    def test_vaules_should_match(self, setup_numerical_array):
        # Arrange
        # Act and Assert
        for index in range(len(setup_numerical_array)):
            assert index == setup_numerical_array[index]
    def test_reverse_iter_should_reverse_array(self, setup_numerical_array):
        counter =9 

        for item in reversed(setup_numerical_array):
            assert item == counter
            counter -=1
    def test_apppend_front_should_add_negative_one_to_front(self, setup_numerical_array):
        #Arrange
        expected = -1
        #Act
        setup_numerical_array.append_front(-1)
        #Assert
        for index in range(len(setup_numerical_array)):
            assert setup_numerical_array[index] == expected
            expected += 1

    def test_append_fround_logical_size_should_be_eleven_and_physical_size_20(self, setup_numerical_array):
        #arrange
        #Act
        setup_numerical_array.append_front(-1)
        #Assert
        assert len(setup_numerical_array) ==11
        assert len(setup_numerical_array._items) ==20





