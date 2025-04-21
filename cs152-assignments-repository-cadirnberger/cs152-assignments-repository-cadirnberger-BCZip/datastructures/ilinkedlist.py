from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, Iterable, Iterator, List, Optional, TypeVar

T = TypeVar('T')

@dataclass
class ListNode(Generic[T]):
    item: T
    previous: Optional[ListNode[T]] = None
    next: Optional[ListNode[T]] = None
    def __str__(self) -> str: return str(self.item)
    def __repr__(self) -> str: return f'ListNode: {str(self)} Next: {str(self.next)} Previous: {str(self.previous)}'

class ILinkedList(Generic[T], Iterable[T], ABC):
    """
    Interface for a generic doubly linked list.

    This interface defines the methods required for a doubly linked list implementation.
    """

    @abstractmethod
    def append(self, item: T) -> None:
        """
        Appends an item to the end of the list.

        Args:
            item (T): The item to append.

        Returns:
            None

        Examples:
            >>> linked_list = LinkedList()
            >>> linked_list.append(1)
            >>> repr(linked_list)
            'LinkedList([1])'
            >>> linked_list.append(2)
            >>> repr(linked_list)
            'LinkedList([1, 2])'
        """
        pass

    @abstractmethod
    def prepend(self, item: T) -> None:
        """
        Prepends an item to the beginning of the list.

        Args:
            item (T): The item to prepend.

        Returns:
            None

        Examples:
            >>> linked_list = LinkedList()
            >>> linked_list.prepend(1)
            >>> repr(linked_list)
            'LinkedList([1])'
            >>> linked_list.prepend(0)
            >>> repr(linked_list)
            'LinkedList([0, 1])'
        """
        pass

    @abstractmethod
    def insert_at(self, item: T, index: int) -> None:
        """
        Inserts an item at a specific index.

        Args:
            item (T): The item to insert.
            index (int): The index at which to insert the item.

        Returns:
            None

        Raises:
            IndexError: If the index is out of bounds.

        Examples:
            >>> linked_list = LinkedList([1, 2, 4])
            >>> linked_list.insert_at(3, 2)
            >>> repr(linked_list)
            'LinkedList([1, 2, 3, 4])'
            >>> linked_list.insert_at(0, 0)
            >>> repr(linked_list)
            'LinkedList([0, 1, 2, 3, 4])'
            >>> linked_list.insert_at(5, 10)
            Traceback (most recent call last):
                ...
            IndexError: Index out of bounds
        """
        pass

    @abstractmethod
    def pop_back(self) -> T:
        """
        Removes and returns the last item from the list.

        Returns:
            T: The item removed.

        Raises:
            IndexError: If the list is empty.

        Examples:
            >>> linked_list = LinkedList([1, 2, 3])
            >>> item = linked_list.pop_back()
            >>> item
            3
            >>> repr(linked_list)
            'LinkedList([1, 2])'
            >>> linked_list.clear()
            >>> linked_list.pop_back()
            Traceback (most recent call last):
                ...
            IndexError: Pop from empty list
        """
        pass

    @abstractmethod
    def pop_front(self) -> T:
        """
        Removes and returns the first item from the list.

        Returns:
            T: The item removed.

        Raises:
            IndexError: If the list is empty.

        Examples:
            >>> linked_list = LinkedList([1, 2, 3])
            >>> item = linked_list.pop_front()
            >>> item
            1
            >>> repr(linked_list)
            'LinkedList([2, 3])'
            >>> linked_list.clear()
            >>> linked_list.pop_front()
            Traceback (most recent call last):
                ...
            IndexError: Pop from empty list
        """
        pass

    @abstractmethod
    def pop_at(self, index: int) -> T:
        """
        Removes and returns the item at a specific index.

        Args:
            index (int): The index of the item to remove.

        Returns:
            T: The item removed.

        Raises:
            IndexError: If the index is out of bounds.

        Examples:
            >>> linked_list = LinkedList([1, 2, 3, 4])
            >>> item = linked_list.pop_at(2)
            >>> item
            3
            >>> repr(linked_list)
            'LinkedList([1, 2, 4])'
            >>> linked_list.pop_at(10)
            Traceback (most recent call last):
                ...
            IndexError: Index out of bounds
        """
        pass

    @abstractmethod
    def clear(self) -> None:
        """
        Clears the list.

        Returns:
            None

        Examples:
            >>> linked_list = LinkedList([1, 2, 3])
            >>> linked_list.clear()
            >>> repr(linked_list)
            'LinkedList([])'
        """
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """
        Checks if the list is empty.

        Returns:
            bool: True if the list is empty, False otherwise.

        Examples:
            >>> linked_list = LinkedList()
            >>> linked_list.is_empty()
            True
            >>> linked_list.append(1)
            >>> linked_list.is_empty()
            False
        """
        pass

    @abstractmethod
    def front(self) -> T:
        """
        Retrieves the first item of the list.

        Returns:
            T: The first item.

        Raises:
            IndexError: If the list is empty.

        Examples:
            >>> linked_list = LinkedList([1, 2, 3])
            >>> linked_list.front()
            1
            >>> linked_list.clear()
            >>> linked_list.front()
            Traceback (most recent call last):
                ...
            IndexError: List is empty
        """
        pass

    @abstractmethod
    def back(self) -> T:
        """
        Retrieves the last item of the list.

        Returns:
            T: The last item.

        Raises:
            IndexError: If the list is empty.

        Examples:
            >>> linked_list = LinkedList([1, 2, 3])
            >>> linked_list.back()
            3
            >>> linked_list.clear()
            >>> linked_list.back()
            Traceback (most recent call last):
                ...
            IndexError: List is empty
        """
        pass

    @abstractmethod
    def to_list(self) -> List[T]:
        """
        Converts the linked list to a Python list.

        Returns:
            list[T]: The list of items.

        Examples:
            >>> linked_list = LinkedList([1, 2, 3])
            >>> linked_list.to_list()
            [1, 2, 3]
            >>> linked_list.clear()
            >>> linked_list.to_list()
            []
        """
        pass

    @abstractmethod
    def __getitem__(self, index: int) -> T:
        """
        Retrieves the item at a specific index.

        Args:
            index (int): The index of the item to retrieve.

        Returns:
            T: The item at the specified index.

        Raises:
            IndexError: If the index is out of bounds.

        Examples:
            >>> linked_list = LinkedList([1, 2, 3])
            >>> linked_list[0]
            1
            >>> linked_list[2]
            3
            >>> linked_list[10]
            Traceback (most recent call last):
                ...
            IndexError: Index out of bounds
        """
        pass

    @abstractmethod
    def __setitem__(self, index: int, item: T) -> None:
        """
        Sets the item at a specific index.

        Args:
            index (int): The index of the item to set.
            item (T): The new item.

        Returns:
            None

        Raises:
            IndexError: If the index is out of bounds.

        Examples:
            >>> linked_list = LinkedList([1, 2, 3])
            >>> linked_list[1] = 99
            >>> repr(linked_list)
            'LinkedList([1, 99, 3])'
            >>> linked_list[10] = 5
            Traceback (most recent call last):
                ...
            IndexError: Index out of bounds
        """
        pass

    @abstractmethod
    def __delitem__(self, index: int) -> None:
        """
        Deletes the item at a specific index.

        Args:
            index (int): The index of the item to delete.

        Returns:
            None

        Raises:
            IndexError: If the index is out of bounds.

        Examples:
            >>> linked_list = LinkedList([1, 2, 3])
            >>> del linked_list[1]
            >>> repr(linked_list)
            'LinkedList([1, 3])'
            >>> del linked_list[10]
            Traceback (most recent call last):
                ...
            IndexError: Index out of bounds
        """
        pass

    @abstractmethod
    def __contains__(self, item: T) -> bool:
        """
        Checks if the list contains a specific item.

        Args:
            item (T): The item to check for.

        Returns:
            bool: True if the item is in the list, False otherwise.

        Examples:
            >>> linked_list = LinkedList([1, 2, 3])
            >>> 2 in linked_list
            True
            >>> 99 in linked_list
            False
        """
        pass

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        """
        Compares the list with another list for equality.

        Args:
            other (object): The other list to compare with.

        Returns:
            bool: True if the lists are equal, False otherwise.

        Examples:
            >>> list1 = LinkedList([1, 2, 3])
            >>> list2 = LinkedList([1, 2, 3])
            >>> list1 == list2
            True
            >>> list3 = LinkedList([4, 5, 6])
            >>> list1 == list3
            False
        """
        pass

    @abstractmethod
    def __iter__(self) -> Iterator[T]:
        """
        Returns an iterator over the items of the list.

        Returns:
            Iterator[T]: The iterator.

        Examples:
            >>> linked_list = LinkedList([1, 2, 3])
            >>> for item in linked_list:
            ...     print(item)
            1
            2
            3
        """
        pass

    @abstractmethod
    def __len__(self) -> int:
        """
        Returns the number of items in the list.

        Returns:
            int: The length of the list.

        Examples:
            >>> linked_list = LinkedList()
            >>> len(linked_list)
            0
            >>> linked_list.append(1)
            >>> len(linked_list)
            1
            >>> linked_list.append(2)
            >>> len(linked_list)
            2
        """
        pass