import pytest


from datastructures.linkedlist import LinkedList
from tests.car import Car, Make, Model, Color


@pytest.fixture
def empty_list(): return LinkedList()

@pytest.fixture
def numerical_list(): return LinkedList([1, 2, 3, 4, 5])

@pytest.fixture
def car_list():
    car1 = Car('123', Color.RED, Make.TOYOTA, Model.CAMRY)
    car2 = Car('456', Color.BLUE, Make.TOYOTA, Model.CIVIC)
    car3 = Car('789', Color.BLACK, Make.FORD, Model.FUSION)
    return LinkedList([car1, car2, car3])

class TestLinkedList:
    
    def test_append(self, empty_list):
        empty_list.append(1)
        assert len(empty_list) == 1
        assert empty_list.back() == 1
        empty_list.append(2)
        assert len(empty_list) == 2
        assert empty_list.back() == 2
        assert empty_list.to_list() == [1, 2]

    def test_prepend(self, empty_list):
        empty_list.prepend(1)
        assert len(empty_list) == 1
        assert empty_list.front() == 1
        empty_list.prepend(0)
        assert len(empty_list) == 2
        assert empty_list.front() == 0
        assert empty_list.to_list() == [0, 1]

    def test_insert_at(self, empty_list):
        empty_list.insert_at(1, 0)
        assert empty_list.to_list() == [1]
        empty_list.append(3)
        empty_list.insert_at(2, 1)
        assert empty_list.to_list() == [1, 2, 3]
        with pytest.raises(IndexError):
            empty_list.insert_at(4, 5)

    def test_pop_back(self, numerical_list):
        assert len(numerical_list) == 5
        numerical_list.pop_back()
        assert len(numerical_list) == 4
        assert numerical_list.to_list() == [1, 2, 3, 4]
        numerical_list.pop_back()
        numerical_list.pop_back()
        numerical_list.pop_back()
        numerical_list.pop_back()
        assert len(numerical_list) == 0
        assert numerical_list.to_list() == []
        with pytest.raises(IndexError):
            numerical_list.pop_back()

    def test_pop_front(self, numerical_list):
        assert len(numerical_list) == 5
        numerical_list.pop_front()
        assert len(numerical_list) == 4
        assert numerical_list.to_list() == [2, 3, 4, 5]
        for _ in range(4):
            numerical_list.pop_front()
        assert len(numerical_list) == 0
        assert numerical_list.to_list() == []
        with pytest.raises(IndexError):
            numerical_list.pop_front()

    def test_pop_at(self, numerical_list):
        numerical_list.pop_at(2)
        assert numerical_list.to_list() == [1, 2, 4, 5]
        numerical_list.pop_at(0)
        assert numerical_list.to_list() == [2, 4, 5]
        numerical_list.pop_at(len(numerical_list) - 1)
        assert numerical_list.to_list() == [2, 4]
        with pytest.raises(IndexError):
            numerical_list.pop_at(5)

    def test_clear(self, numerical_list):
        numerical_list.clear()
        assert len(numerical_list) == 0
        assert numerical_list.to_list() == []
        assert numerical_list.is_empty()

    def test_is_empty(self, empty_list, numerical_list):
        assert empty_list.is_empty()
        assert not numerical_list.is_empty()

    def test_front(self, numerical_list):
        assert numerical_list.front() == 1
        with pytest.raises(IndexError):
            empty_list = LinkedList()
            empty_list.front()

    def test_back(self, numerical_list):
        assert numerical_list.back() == 5
        with pytest.raises(IndexError):
            empty_list = LinkedList()
            empty_list.back()

    def test_to_list(self, numerical_list):
        assert numerical_list.to_list() == [1, 2, 3, 4, 5]

    def test_getitem(self, numerical_list):
        assert numerical_list[0] == 1
        assert numerical_list[4] == 5
        with pytest.raises(IndexError):
            _ = numerical_list[5]

    def test_setitem(self, numerical_list):
        numerical_list[0] = 10
        assert numerical_list[0] == 10
        numerical_list[4] = 50
        assert numerical_list[4] == 50
        with pytest.raises(IndexError):
            numerical_list[5] = 60

    def test_contains(self, numerical_list):
        assert 3 in numerical_list
        assert 6 not in numerical_list

    def test_eq(self):
        list1 = LinkedList([1, 2, 3])
        list2 = LinkedList([1, 2, 3])
        list3 = LinkedList([4, 5, 6])
        assert list1 == list2
        assert list1 != list3

    def test_iterator(self, numerical_list):
        items = [item for item in numerical_list]
        assert items == [1, 2, 3, 4, 5]

    def test_next(self, numerical_list):
        iterator = iter(numerical_list)
        assert next(iterator) == 1
        assert next(iterator) == 2
        assert next(iterator) == 3
        assert next(iterator) == 4
        assert next(iterator) == 5
        with pytest.raises(StopIteration):
            next(iterator)

    def test_len(self, empty_list, numerical_list):
        assert len(empty_list) == 0
        assert len(numerical_list) == 5

    def test_append_complex_objects(self, car_list):
        car4 = Car('012', Color.RED, Make.FORD, Model.FUSION)
        initial_length = len(car_list)
        car_list.append(car4)
        assert len(car_list) == initial_length + 1
        assert car_list.back() == car4
        expected_list = [Car('123', Color.RED, Make.TOYOTA, Model.CAMRY),
                         Car('456', Color.BLUE, Make.TOYOTA, Model.CIVIC),
                         Car('789', Color.BLACK, Make.FORD, Model.FUSION),
                         car4]
        assert car_list.to_list() == expected_list

    def test_prepend_complex_objects(self, car_list):
        car0 = Car('000', Color.BLACK, Make.TOYOTA, Model.CAMRY)
        initial_length = len(car_list)
        car_list.prepend(car0)
        assert len(car_list) == initial_length + 1
        assert car_list.front() == car0
        expected_list = [car0,
                         Car('123', Color.RED, Make.TOYOTA, Model.CAMRY),
                         Car('456', Color.BLUE, Make.TOYOTA, Model.CIVIC),
                         Car('789', Color.BLACK, Make.FORD, Model.FUSION)]
        assert car_list.to_list() == expected_list

    def test_insert_at_complex_objects(self, car_list):
        car_mid = Car('555', Color.BLUE, Make.FORD, Model.CAMRY)
        initial_length = len(car_list)
        car_list.insert_at(car_mid, 2)
        assert len(car_list) == initial_length + 1
        expected_list = [Car('123', Color.RED, Make.TOYOTA, Model.CAMRY),
                         Car('456', Color.BLUE, Make.TOYOTA, Model.CIVIC),
                         car_mid,
                         Car('789', Color.BLACK, Make.FORD, Model.FUSION)]
        assert car_list.to_list() == expected_list
        assert car_list[2] == car_mid

    def test_pop_back_complex_objects(self, car_list):
        initial_length = len(car_list)
        last_car = car_list.back()
        car_list.pop_back()
        assert len(car_list) == initial_length - 1
        assert car_list.back() != last_car
        expected_list = [Car('123', Color.RED, Make.TOYOTA, Model.CAMRY),
                         Car('456', Color.BLUE, Make.TOYOTA, Model.CIVIC)]
        assert car_list.to_list() == expected_list
        with pytest.raises(IndexError):
            empty_list = LinkedList()
            empty_list.pop_back()

    def test_pop_front_complex_objects(self, car_list):
        initial_length = len(car_list)
        first_car = car_list.front()
        car_list.pop_front()
        assert len(car_list) == initial_length - 1
        assert car_list.front() != first_car
        expected_list = [Car('456', Color.BLUE, Make.TOYOTA, Model.CIVIC),
                         Car('789', Color.BLACK, Make.FORD, Model.FUSION)]
        assert car_list.to_list() == expected_list
        with pytest.raises(IndexError):
            empty_list = LinkedList()
            empty_list.pop_front()

    def test_pop_at_complex_objects(self, car_list):
        initial_length = len(car_list)
        car_to_remove = car_list[1]
        car_list.pop_at(1)
        assert len(car_list) == initial_length - 1
        assert car_to_remove not in car_list
        expected_list = [Car('123', Color.RED, Make.TOYOTA, Model.CAMRY),
                         Car('789', Color.BLACK, Make.FORD, Model.FUSION)]
        assert car_list.to_list() == expected_list
        with pytest.raises(IndexError):
            car_list.pop_at(10)

    def test_contains_complex_objects(self, car_list):
        car_exists = car_list[0]
        car_not_in_list = Car('999', Color.RED, Make.TOYOTA, Model.CAMRY)
        assert car_exists in car_list
        assert car_not_in_list not in car_list

    def test_eq_complex_objects(self, car_list):
        other_car_list = LinkedList(car_list.to_list())
        assert car_list == other_car_list
        car_list.pop_back()
        assert car_list != other_car_list

    def test_iteration_complex_objects(self, car_list):
        cars = [car for car in car_list]
        assert cars == car_list.to_list()

    def test_getitem_complex_objects(self, car_list):
        car = car_list[1]
        assert car == car_list.to_list()[1]
        with pytest.raises(IndexError):
            _ = car_list[10]

    def test_setitem_complex_objects(self, car_list):
        new_car = Car('999', Color.RED, Make.TOYOTA, Model.CAMRY)
        car_list[0] = new_car
        assert car_list[0] == new_car
        expected_list = [new_car,
                         Car('456', Color.BLUE, Make.TOYOTA, Model.CIVIC),
                         Car('789', Color.BLACK, Make.FORD, Model.FUSION)]
        assert car_list.to_list() == expected_list
        with pytest.raises(IndexError):
            car_list[10] = new_car

    def test_is_empty_complex_objects(self):
        empty_car_list = LinkedList()
        assert empty_car_list.is_empty()
        car = Car('123', Color.RED, Make.TOYOTA, Model.CAMRY)
        empty_car_list.append(car)
        assert not empty_car_list.is_empty()

    def test_clear_complex_objects(self, car_list):
        car_list.clear()
        assert len(car_list) == 0
        assert car_list.is_empty()
        assert car_list.to_list() == []

    def test_len_complex_objects(self, car_list):
        assert len(car_list) == 3
        car_list.append(Car('999', Color.RED, Make.FORD, Model.FUSION))
        assert len(car_list) == 4
        car_list.pop_front()
        assert len(car_list) == 3
