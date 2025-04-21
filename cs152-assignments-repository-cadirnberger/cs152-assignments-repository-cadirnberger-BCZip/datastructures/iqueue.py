from abc import abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class IQueue(Generic[T]):
    '''Interface for a queue data structure'''

    @abstractmethod
    def enqueue(self, item: T) -> None:
        '''Enqueues an item onto the queue
        
        Examples:
            >>> queue = Queue()
            >>> queue.enqueue(1)
            >>> queue.enqueue(2)
            >>> queue.enqueue(3)
            >>> print(queue.size())
            3
            
        Args:
            item: The item to enqueue onto the queue'''
        ...

    @abstractmethod
    def dequeue(self) -> T:
        '''Dequeues an item from the queue
        
        Examples:
            >>> queue = Queue()
            >>> queue.enqueue(1)
            >>> queue.enqueue(2)
            >>> queue.enqueue(3)
            >>> print(queue.dequeue())
            1
            >>> print(queue.dequeue())
            2
            >>> print(queue.dequeue())
            3
            >>> print(queue.size())
            0
            
            Returns:
                The item at the front of the queue
                
            Raises:
                IndexError: If the queue is empty'''
        ...

    @abstractmethod
    def front(self) -> T:
        '''Returns the item at the front of the queue
        
        Examples:
            >>> queue = Queue()
            >>> queue.enqueue(1)
            >>> queue.enqueue(2)
            >>> queue.enqueue(3)
            >>> print(queue.front())
            1
            
            Returns:
                The item at the front of the queue
                
            Raises:
                IndexError: If the queue is empty'''
        ...

    @abstractmethod
    def back(self) -> T:
        '''Returns the item at the back of the queue
        
        Examples:
            >>> queue = Queue()
            >>> queue.enqueue(1)
            >>> queue.enqueue(2)
            >>> queue.enqueue(3)
            >>> print(queue.back())
            3
            
            Returns:
                The item at the back of the queue
                
            Raises:
                IndexError: If the queue is empty'''
        ...

    @abstractmethod
    def size(self) -> int:
        '''Returns the number of items in the queue
        
        Examples:
            >>> queue = Queue()
            >>> queue.enqueue(1)
            >>> queue.enqueue(2)
            >>> queue.enqueue(3)
            >>> print(queue.size())
            3
            
            Returns:
                The number of items in the queue'''
        ...

    @abstractmethod
    def is_empty(self) -> bool:
        '''Returns True if the queue is empty, False otherwise
        
        Examples:
            >>> queue = Queue()
            >>> print(queue.is_empty())
            True
            >>> queue.enqueue(1)
            >>> print(queue.is_empty())
            False
            
            Returns:
                True if the queue is empty, False otherwise'''
        ...

    @abstractmethod
    def clear(self) -> None:
        '''Clears all items from the queue
        
        Examples:
            >>> queue = Queue()
            >>> queue.enqueue(1)
            >>> queue.enqueue(2)
            >>> queue.enqueue(3)
            >>> queue.clear()
            >>> print(queue.size())
            0
            
            Returns:
                None'''
        ...

    @abstractmethod
    def __contains__(self, item: T) -> bool:
        '''Returns True if the item is in the queue, False otherwise
        
        Args:
            item: The item to search for in the queue
            
        Returns:
            True if the item is in the queue, False otherwise'''
        ...

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        '''Returns True if the queue is equal to another queue, False otherwise
        
        Args:
            other: The other queue to compare against
            
        Returns:
            True if the queue is equal to the other queue, False otherwise'''
        ...

    @abstractmethod
    def __str__(self) -> str:
        '''Returns the string representation of the queue
        
        Returns:
            The string representation of the queue'''
        ...

    @abstractmethod
    def __repr__(self) -> str:
        '''Returns the string representation of the queue
        
        Returns:
            The string representation of the queue'''
        ...
