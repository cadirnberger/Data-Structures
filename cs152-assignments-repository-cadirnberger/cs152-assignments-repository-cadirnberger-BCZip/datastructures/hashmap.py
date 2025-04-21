from __future__ import annotations
from typing import Any, Dict, Iterable, Iterator, List, Set, Tuple
import copy
#import sympy
from datastructures.array import Array
from datastructures.linkedlist import LinkedList
from datastructures.ihashmap import IHashMap, KeyValuePair, _K, _V

def hash_function(key: _K) -> int :
    if isinstance(key, Iterable):
        sum = 0
        for item in key:
            sum += hash(item)
        return sum
    return hash(key)
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):  
        if n % i == 0:
            return False
    return True
def next_prime(n: int) -> int:
    n += 1
    while not is_prime(n):
        n += 1
    return n
class HashMap(IHashMap[_K, _V]):
    def __init__(self, starting_map: Dict = {}) -> None:
        self._buckets: Array[LinkedList[KeyValuePair]]= Array(starting_sequence=[LinkedList[KeyValuePair]()for _  in range(7)], data_type=object)
        self._item_count = 0
        for key, value in starting_map:
            buckets_index = hash_function(key) % len(self._buckets)
            self._buckets[buckets_index].append(KeyValuePair(_key=key, value=value))
            self._item_count += 1
        self.resize_rehash()
        
    def resize_rehash(self)-> None:
        buckets_in_use = 0 
        total = len(self._buckets)
        for buckets_index in range(len(self._buckets)):
            if len(self._buckets[buckets_index]) > 0:
                buckets_in_use += 1
        ratio : float = buckets_in_use / total
        if ratio > 0.6:
            new_bucket_size = next_prime(len(self._buckets))

            tem_buckets = Array(starting_sequence=[LinkedList[KeyValuePair]()for _ in range(new_bucket_size)], data_type=object)

            for key,value in self.items():
                bucket = hash_function(key) % len(tem_buckets)
                tem_buckets[bucket].append(KeyValuePair(_key=key, value=value))
        
            self._buckets = tem_buckets

    def __getitem__(self, key: _K) -> _V:
        buckets_index = hash_function(key) % len(self._buckets)

        for item in self._buckets[buckets_index]:
            if item.key == key:
                return item.value
        raise KeyError(f"{key} not found")

    def __setitem__(self, key: _K, value: _V) -> None:
        buckets_index = hash_function(key) % len(self._buckets)
        bucket = self._buckets[buckets_index]
        for item in bucket:
            if item.key == key:
                item.value = value
                return
        self._buckets[buckets_index].append(KeyValuePair(_key=key, value=value))
        self._item_count += 1
        self.resize_rehash()
        
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HashMap):
            return False
        if len(self) != len(other):
            return False
        for key, value in self.items():
            if key not in other or other[key] != value:
                return False
        return True

    def __delitem__(self, key: _K) -> None:
        bucket_index = hash_function(key) % len(self._buckets)
        bucket = self._buckets[bucket_index]
        for idx, pair in enumerate(bucket):
            if pair.key == key:
                bucket.pop_at(idx)
                self._item_count -= 1
                return
        raise KeyError(f"{key} not found")

    def clear(self) -> None:
        self._buckets = Array(starting_sequence=[LinkedList[KeyValuePair]() for _ in range(7)], data_type=object )
        self._item_count = 0

    def keys(self) -> List[_K]: 
        return {pair.key for bucket in self._buckets for pair in bucket}

    def values(self) -> List[_V]: 
        value: list[_K] = []
        for bucket in self._buckets:
            for pair in bucket:
                value.append(pair.value)
        return copy.deepcopy(value)

    def items(self) -> List[Tuple[_K, _V]]: 
        return {(pair.key, pair.value) for bucket in self._buckets for pair in bucket}
        
    
    def __len__(self) -> int: 
        return self._item_count 

    def __iter__(self) -> Iterator[_K]: 
        return iter(self.keys())

    def __contains__(self, key: Any) -> bool: 
        bucket_index = hash_function(key) % len(self._buckets)

        for pair in self._buckets[bucket_index]:
            if pair.key == key:
                return True
        return False

    def __str__(self) -> str: 
        return "{" + ", ".join([f"{key}: {value}" for key, value in self.items()]) + "}"
    
    def __repr__(self) -> str: 
        return f"HashMap({str(self)})"