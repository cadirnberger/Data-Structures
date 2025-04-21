from abc import abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class IStack(Generic[T]):
    '''Interface for a stack data structure'''

    @abstractmethod
    def push(self, item: T) -> None:
        '''Pushes an item onto the stack
        
        Examples: 
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.push(3)
            >>> print(stack.size())
            3
        
        Args:
            item: The item to push onto the stack'''
        ...

    @abstractmethod
    def pop(self) -> T:
        '''Pops an item from the stack
        
        Examples:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.push(3)
            >>> print(stack.pop())
            3
            >>> print(stack.pop())
            2
            >>> print(stack.pop())
            1
            >>> print(stack.size())
            0
            
            Returns:
                The item at the top of the stack
                
            Raises:
                IndexError: If the stack is empty'''
        ...

    @abstractmethod
    def peek(self) -> T:
        '''Returns the item at the top of the stack
        
        Examples:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.push(3)
            >>> print(stack.peek())
            3
            >>> print(stack.size())
            3
            
            Returns:
                The item at the top of the stack
            
            Raises:
                IndexError: If the stack is empty'''
        ...

    @abstractmethod
    def is_empty(self) -> bool:
        '''Returns True if the stack is empty, False otherwise
        
        Examples:
            >>> stack = Stack()
            >>> print(stack.is_empty())
            True
            >>> stack.push(1)
            >>> print(stack.is_empty())
            False
            
            Returns:
                True if the stack is empty, False otherwise'''
        ...

    @abstractmethod
    def size(self) -> int:
        '''Returns the number of items in the stack
        
        Examples:
            >>> stack = Stack()
            >>> print(stack.size())
            0
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.push(3)
            >>> print(stack.size())
            3
            
            Returns:
                The number of items in the stack'''
        ...

    @abstractmethod
    def clear(self) -> None:
        '''Removes all items from the stack
        
        Examples:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.push(3)
            >>> stack.clear()
            >>> print(stack.size())
            0
            
            Returns:
                None'''
        ...
    
    @abstractmethod
    def __contains__(self, item: T) -> bool:
        '''Returns True if the item is in the stack, False otherwise
        
        Examples:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.push(3)
            >>> print(1 in stack)
            True
            >>> print(4 in stack)
            False
            
            Returns:
                True if the item is in the stack, False otherwise'''
        ...
    
    @abstractmethod
    def __eq__(self, other: object) -> bool:
        '''Returns True if the stack is equal to another stack, False otherwise
        
        Examples:
            >>> stack1 = Stack()
            >>> stack1.push(1)
            >>> stack1.push(2)
            >>> stack1.push(3)
            >>> stack2 = Stack()
            >>> stack2.push(1)
            >>> stack2.push(2)
            >>> stack2.push(3)
            >>> print(stack1 == stack2)
            True
            
            Returns:
                True if the stack is equal to the other stack, False otherwise'''
        ...

    @abstractmethod
    def __str__(self) -> str:
        '''Returns a string representation of the stack
        
        Examples:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.push(3)
            >>> print(stack)
            Stack: [3, 2, 1]
            
            Returns:
                A string representation of the stack'''
        ...

    @abstractmethod
    def __repr__(self) -> str:
        """Returns a string representation of the stack
        
        Examples:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.push(3)
            >>> print(stack)
            Stack: [3, 2, 1]
            
            Returns:
                A string representation of the stack"""
        ...