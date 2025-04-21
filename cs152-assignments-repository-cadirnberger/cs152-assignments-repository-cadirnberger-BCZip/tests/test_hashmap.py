import pytest
from dataclasses import dataclass
from typing import Final
from datastructures.hashmap import HashMap

@dataclass
class Person:
    ssn: str
    name: str
    age: int

    def __hash__(self) -> int:
        return hash(self.ssn)

    def __eq__(self, other) -> bool:
        return self.ssn == other.ssn

    def __str__(self) -> str:
        return f"{self.ssn} {self.name} {self.age}"

PERSON1: Final[Person] = Person(ssn="123", name="John", age=30)
PERSON2: Final[Person] = Person(ssn="456", name="Jane", age=40)
PERSON3: Final[Person] = Person(ssn="789", name="Jack", age=50)

class TestHashMap:
    @pytest.fixture
    def simple_hashmap(self) -> HashMap[int, str]:
        hashmap = HashMap[int, str]()
        for key in range(10):
            hashmap[key] = str(key)
        return hashmap

    @pytest.fixture
    def complex_hashmap(self) -> HashMap[str, Person]:
        hashmap = HashMap[str, Person]()
        hashmap[PERSON1.ssn] = PERSON1
        hashmap[PERSON2.ssn] = PERSON2
        hashmap[PERSON3.ssn] = PERSON3
        return hashmap

    def test_insert_and_retrieve(self, simple_hashmap: HashMap[int, str]):
        assert simple_hashmap[1] == "1"
        assert simple_hashmap[5] == "5"
        
    def test_key_error(self, simple_hashmap: HashMap[int, str]):
        with pytest.raises(KeyError):
            _ = simple_hashmap[100]

    def test_overwrite_key(self, simple_hashmap: HashMap[int, str]):
        simple_hashmap[1] = "100"
        assert simple_hashmap[1] == "100"

    def test_delete_key(self, simple_hashmap: HashMap[int, str]):
        del simple_hashmap[2]
        assert 2 not in simple_hashmap
        with pytest.raises(KeyError):
            _ = simple_hashmap[2]

    def test_length(self, simple_hashmap: HashMap[int, str]):
        assert len(simple_hashmap) == 10

    def test_equality(self, simple_hashmap: HashMap[int, str]):
        other_hashmap = HashMap[int, str]()
        for key in range(10):
            other_hashmap[key] = str(key)
        assert simple_hashmap == other_hashmap

    def test_clear(self, simple_hashmap: HashMap[int, str]):
        simple_hashmap.clear()
        assert len(simple_hashmap) == 0
        assert not any(simple_hashmap.keys())

    def test_iteration(self, simple_hashmap: HashMap[int, str]):
        keys = list(simple_hashmap.keys())
        values = list(simple_hashmap.values())
        assert keys == list(range(10))
        assert values == [str(x) for x in range(10)]

    def test_contains(self, simple_hashmap: HashMap[int, str]):
        assert 3 in simple_hashmap
        assert 100 not in simple_hashmap

    def test_keys_values_items(self, simple_hashmap: HashMap[int, str]):
        keys = simple_hashmap.keys()
        values = simple_hashmap.values()
        items = simple_hashmap.items()
        assert keys == set(range(10))
        assert set(values) == {str(x) for x in range(10)}
        assert items == {(x, str(x)) for x in range(10)}

    def test_complex_object(self, complex_hashmap: HashMap[str, Person]):
        assert complex_hashmap[PERSON1.ssn] == PERSON1
        assert complex_hashmap[PERSON2.ssn] == PERSON2
        assert complex_hashmap[PERSON3.ssn] == PERSON3