from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict, Generic, Iterator, List, Set, Tuple, TypeVar

_K = TypeVar('_K')
_V = TypeVar('_V')

@dataclass
class KeyValuePair(Generic[_K, _V]):
    """ Class KeyValuePair - representing a key-value pair in the HashMap.
    
        Attributes:
            key (K): The key of the pair. Initialized as a field to prevent modification.
            value (V): The value of the pair.
    """
    _key: _K = field(init=True, repr=True)
    value: _V

    @property
    def key(self) -> _K:
        return self._key

class IHashMap(ABC, Generic[_K, _V]):
    """ Class HashMap - A generic HashMap data structure class. The HashMap class is a data structure that stores key-value pairs.
        
        HashMap Properties:
            1. The underlying data structure of the HashMap is a combination of an Array (buckets) and a LinkedList (chains). The 
                LinkedList is used to handle collisions for each bucket. Key/Value pairs are stored in the LinkedList using the provided 
                KeyValuePair class definition.
            2. The HashMap always uses a prime number for the number of buckets (Array length) to improve the hashing algorithm. The 
                HashMap is initialized at construction time to 7 (buckets).
            3. Values are retrieved from the HashMap via the bracket operator using the Key (see __set__ method). 
                If the key is not present, the HashMap raises a KeyError.
            4. Key/Values are inserted into the HashMap via the bracket operator (see __get__ method). If the key is already present, 
                the value is replaced. Otherwise, the key/value pair is appended to the end of the LinkedList in the bucket.
            5. The index used in the bracket operators is determined by hashing the key using a hash function. 
                The following properties are true of a hash function:
                a. A hash function may be supplied by the user during construction of the HashMap. If a hash function is not supplied,
                    the HashMap will use a default generic hash function that supports any key type and whether the key is iterable or not.
                b. The signature of a hash function: def hash_function(key: Any) -> int:. Note, the hash function must return an integer. 
                c. The hash function must be deterministic. This means that the hash function must return the same integer for the same key.
                d. A hash function itself does not take into account the number of buckets or whether the integer returned by the hash
                    function would result in a bucket that is out of bounds. The HashMap will handle this.
                e. If a key is an iterable (e.g., a string), the default hash function will hash the sum of the hashes of the elements. 
                    If the key is not an iterable, then it hashes the key itself: hash(key).
            6. Collisions will occur when two keys hash into the same bucket index. If a key hashes to a bucket that already contains a
                key-value pair in the chain, the new key-value pair is appended to the end of the LinkedList.
            7. If a hash function is not provided by the user, the HashMap must have a default hash function that hashes the key.
            8. If the percentage of buckets in use surpasses 60%, resize the hash map to the next highest prime. This
                means that if the hash map has 7 buckets and 5 are in use, the load factor is 5/7 = 0.714, which is
                greater than 0.6. The buckets size should be resized to the next highest prime, which in this example is 11. 
                Note: a `bucket in use` is defined as a bucket that has one or more items in the bucket's chain.
                When resizing, rehash all the keys in the hash map.
            9. The items, keys, and values methods return a deep copy of the items, keys, and values (using copy.deepcopy).
    """

    @abstractmethod
    def __init__(self, starting_map: Dict = {}) -> None:
        """ Constructor for the HashMap class.
            
            Examples: 
                >>> hashmap = HashMap()
                >>> hashmap['x'] = 3
                >>> print(hashmap['x'])
                3
                >>> hashmap = HashMap()
                >>> hashmap['x'] = 3
                >>> print(hashmap['x'])
                3
                >>> hashmap = HashMap(starting_map={'x': 3, 'y': 4})
                >>> print(repr(hashmap))
                HashMap({x: 3, y: 4})
                >>> hashmap = HashMap(starting_map="Not a dictionary")
                TypeError: starting_map must be a Python dictionary
            
            Args:
                starting_map (dict): The starting map to initialize the hashmap with (optional).   
                
            Raises:
                TypeError: If the starting map is not a Python dictionary.
        """
        ...

    @abstractmethod
    def __getitem__(self, key: _K) -> _V:
        """ Bracket operator for getting a Value from the hash map. If the key is not present, raise a KeyError.

            Examples:
                >>> hashmap = HashMap()
                >>> hashmap['x'] = 3
                >>> hashmap['x']
                3
                >>> hashmap['y']
                KeyError: 'key y not found'

            Args:
                key (K): The key to get the value of.

            Returns:
                V: The value of the key.

            Raises:
                KeyError: If the key is not present in the hashmap.
        """
        ...


    @abstractmethod
    def __setitem__(self, key: _K, value: _V) -> None:
        """ Bracket operator for setting a value in the hash map. If the key is already present, replace the value.
            If the load factor is greater than the threshold, resize the hash map.
            
            Examples:
                >>> hashmap = HashMap()
                >>> hashmap['x'] = 3
                >>> hashmap['x']
                3
                
            Args:
                key (K): The key to set the value of. 
                value (V): The value to set.

            Returns:
                None
            """
        ...

    @abstractmethod
    def __len__(self) -> int:
        """ Length operator for the hash map. Returns the count of items in the hash map.
        
            Examples:
                >>> hashmap = HashMap()
                >>> len(hashmap)
                0
                >>> hashmap['x'] = 3
                >>> len(hashmap)
                1
                
            Returns:
                int: The count of the hash map.
        """
        ...
        
    @abstractmethod
    def __eq__(self, other: object) -> bool:
        """ Equality operator for the hash map. Returns true if the hash maps are equal.
        
            Examples:
                >>> hashmap1 = HashMap()
                >>> hashmap2 = HashMap()
                >>> for i in range(5): 
                ...     hashmap1[i] = hashmap2[i] = i
                >>> print(repr(hashmap1))
                HashMap({0: 0, 1: 1, 2: 2, 3: 3, 4: 4})
                >>> print(repr(hashmap2))
                HashMap({0: 0, 1: 1, 2: 2, 3: 3, 4: 4})
                >>> print(hashmap1 == hashmap2)
                True
                >>> hashmap1[0] = 100
                >>> print(repr(hashmap1))
                HashMap({0: 100, 1: 1, 2: 2, 3: 3, 4: 4})
                >>> print(hashmap1 == hashmap2)
                False

            Args:
                other (object): The other hash map to compare to.
                
            Returns:
                bool: True if the hash maps are equal.
            """
        ...

    @abstractmethod
    def __iter__(self) -> Iterator[_K]:
        """ Iterator for the hash map. Returns an iterator of the keys.

            Examples:
                >>> hashmap = HashMap(starting_map={'x': 3, 'y': 4})
                >>> for key, value in hashmap:
                ...     print(key, value)
                x 3
                y 4

            Returns:    
                Any: An iterator of the keys.
        """
        ...

    @abstractmethod
    def __delitem__(self, key: _K) -> None:
        """ Delete an item in the hash map. Does not resize the buckets, but does remove the associated chain link.
        
        Examples:
            >>> hashmap = HashMap(starting_map={'x': 3, 'y': 4})
            >>> print(repr(hashmap))
            HashMap({x: 3, y: 4})
            >>> del hashmap['x']
            >>> print(repr(hashmap))
            HashMap({y: 4})

            Args:
                key (Any): The key to delete.
                
            Returns:
                None
        """
        ...

    @abstractmethod
    def __contains__(self, key: object) -> bool:
        """ Contains operator for the hash map. Returns true if the key is in the hash map. 
        
            Examples:
                >>> hashmap = HashMap(starting_map={'x': 3})
                >>> print(repr(hashmap))
                HashMap({x: 3})
                >>> print('x' in hashmap)
                True
                >>> print('y' in hashmap)
                False
                
            Args:
                key (Any): The key to check for.
            
            Returns:
                bool: True if the key is in the hash map.
        """
        ...

    @abstractmethod
    def clear(self) -> None:
        """ Clear the hash map. Removes all items from the hash map.
        
            Examples:
                >>> hashmap = HashMap(starting_map={'x': 3})
                >>> print(repr(hashmap))
                HashMap({x: 3})
                >>> hashmap.clear()
                >>> print(repr(hashmap))
                HashMap({})
                
            Returns:
                None
        """
        ...

    @abstractmethod
    def keys(self) -> List[_K]:
        """ Returns a view object (deep copy of the keys). The view object contains the keys of the 
            dictionary, as a set.
        
            Examples:
                >>> hashmap = HashMap[str, int](starting_map={'x': 3, 'y': 4, 'z': 5})
                >>> keys: List[str] = hashmap.keys()
                >>> print(keys)
                ['x', 'y', 'z']
                
            Returns:
                list: The keys of the hash map.
        """
        ...

    @abstractmethod
    def values(self) -> List[_V]:
        """ Returns a view object (deep copy of the values). The view object contains the values of the dictionary, 
            as a list.
        
            Examples:
                >>> hashmap = HashMap[str, int](starting_map={'x': 3, 'y': 4, 'z': 5})
                >>> values: List[int] = hashmap.values()
                >>> print(values)
                [3, 4, 5]
            
            Returns:
                list: The values of the hash map.
        """
        ...

    @abstractmethod
    def items(self) -> List[Tuple[_K, _V]]:
        """ Returns a view object (deep copy). The view object contains the key-value pairs of the dictionary, as a list of tuples.
        
            Examples:
                >>> hashmap = HashMap[str, int](starting_map={'x': 3, 'y': 4, 'z': 5})
                >>> items: List[Tuple[str, int]] = hashmap.items()
                >>> print(items)
                [('x', 3), ('y', 4), ('z', 5)]
            
            Returns:
                list: The items of the hash map as tuples.
        """
        ...

    @abstractmethod
    def __str__(self) -> str:
        """ String representation of the hash map.
        
            Examples:
                >>> hashmap = HashMap[str, int](starting_map={'x': 3, 'y': 4, 'z': 5})
                >>> print(hashmap)
                {x: 3, y: 4, z: 5}
        """
        ...
    
    @abstractmethod
    def __repr__(self) -> str:
        """ Representation of the hash map.
        
            Examples:
                >>> hashmap = HashMap[str, int](starting_map={'x': 3, 'y': 4, 'z': 5})
                >>> print(repr(hashmap))
                HashMap({x: 3, y: 4, z: 5})
        """
        ...