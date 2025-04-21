""" This module defines an Array2D interface that represents a two-dimensional array. 
    This file lists the stipulations and more information on the methods and their expected behavior.
    YOU SHOULD NOT MODIFY THIS FILE.
    Implement the Array2D class in the array2d.py file.
"""

from __future__ import annotations
from collections.abc import Sequence

from abc import ABC, abstractmethod
from typing import Any, Generic, Iterator, TypeVar, overload

from datastructures.iarray import IArray

T = TypeVar('T', bound=Any)


class IArray2D(IArray[T], Generic[T], ABC):
    """ An interface that represents the minimal functions needed to make an Array object
        into a two-dimensional array. Other typical functions like str, len, repr, etc. are not
        included in this interface because they are provided by the IArray
    """
    @abstractmethod
    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]]) -> None: 
        """ Initializes the Array2D object with a starting sequence of sequences.

        Examples:
            >>> array2d = Array2D([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            >>> repr(array2d)
            Array2D [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            >>> 
        
        Args:
            starting_sequence (Sequence[Sequence[T]]): The starting sequence of sequences.
            
        Raises:
            ValueError: If the starting sequence is not a valid sequence.
            ValueError: If the starting sequence is not a list of lists.
            ValueError: If all items are not of the same type.

        Returns:
            None            
            """
        pass

    @staticmethod
    @abstractmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> IArray[IArray[T]]:  
        """ Creates an empty two-dimensional array with the specified number of rows and columns.
        
        Args:
            rows (int): The number of rows in the two-dimensional array.
            cols (int): The number of columns in the two-dimensional array.
            data_type (type): The type of data that the array will hold.
        
        Returns:
            IArray2D[T]: An empty two-dimensional array of the specified size and data type.
        """
        pass


    @overload
    def __getitem__(self, index: int) -> IArray[T]: ...
    @overload
    def __getitem__(self, index: slice) -> IArray2D[T]: ...
    @abstractmethod
    def __getitem__(self, index: int | slice) -> IArray[T] | IArray2D[T]: 
        """ Gets the item at the specified index or a slice of the two-dimensional array. If the index is a slice,
            the method should return a two-dimensional array with the specified slice of the two-dimensional array. 
            Otherwise, it should return an array at the specified index since the elements of the two-dimensional array
            are arrays.
        Args:
            index (int | slice): The index or slice of the two-dimensional array.
            
        Returns:
            IArray[T] | IArray2D[T]: The item at the specified index or a slice of the two-dimensional array.
            
        Raises:
            IndexError: If the index is out of bounds.
            
        """
        pass

    @abstractmethod
    def __iter__(self) -> Iterator[IArray[T]]:
        """ Returns an iterator of the two-dimensional array. Because the two-dimensional array is
            made up of arrays, the iterator should return an iterator to an array.
        
        Returns:
            Iterator[IArray[T]]: An iterator of the two-dimensional array.
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """ Returns a string representation of the two-dimensional array. The string representation
            should include the string representation of each array in the two-dimensional array.
        
        Returns:
            str: A string representation of the two-dimensional array.
        """
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """ Returns a string representation of the two-dimensional array. The string representation
            should include the string representation of each array in the two-dimensional array.
        
        Returns:
            str: A string representation of the two-dimensional array.
        """
        pass