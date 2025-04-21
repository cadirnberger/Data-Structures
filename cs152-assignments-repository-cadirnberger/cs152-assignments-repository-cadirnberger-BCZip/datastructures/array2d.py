from __future__ import annotations
import os
from typing import Iterator, Sequence, overload

from datastructures.iarray import IArray
from datastructures.iarray2d import IArray2D
from datastructures.array import Array, T

class Array2D(IArray2D[T], Array[T]):
    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]]) -> None:
        if not isinstance(starting_sequence, Sequence):
            raise ValueError(f'A seqance is required, but received {starting_sequence}')
     #   for sequance in starting_sequence:
     #      if not isinstance(sequance, Sequence):
     #           raise ValueError('All sequance must be sequance')
        if not all(isinstance(sequance, Sequence) for sequance in starting_sequence):
            raise ValueError(f'All sequance must be sequance themselves, received {starting_sequence}')
        
        self._data_type = type(starting_sequence[0][0]) if len(starting_sequence)>0 and len(starting_sequence[0])>0 else object
        
        for sequance in starting_sequence:
            if not all(isinstance(item, self._data_type)for item in sequance):
                raise ValueError(f' All item must be of type{self._data_type}. Received {starting_sequence}')
        array: list[Array] = [Array(sequance, self._data_type) for sequance in starting_sequence]
        Array.__init__(self, Array(array, Array), Array) 

    @staticmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> IArray[IArray[T]]: 
        return Array([Array([data_type()]*cols, data_type)for _ in range(rows)], Array)
    
    @overload
    def __getitem__(self, index: int) -> IArray[T]: ...
    @overload
    def __getitem__(self, index: slice) -> IArray[T]: ...
    def __getitem__(self, index: int | slice) -> IArray[T] | IArray[T]: 
        if isinstance(index, slice):
            return Array(Array(self._items[index].tolist()), Array)
        return Array.__getitem__(self, index)
    
    def __iter__(self) -> Iterator[IArray[T]]:
        return Array.__iter__(self)
    
    def __str__(self) -> str: 
        return Array.__str__(self)
    
    def __repr__(self) -> str: 
        return f'Array2D{str(self)}'
    
#class Array2D():
 #   def __init__(self, rows: int, columns: int, data_type: type):

#        self._items2d = Array([Array([data_type()]* columns, data_type)]* rows, Array)
#    def __len__(self)-> int:
#        return len(self._items2d)
#    def __getitem__(self, row_number: int,) -> Array[T]:
        
#        return self._items2d[row_number]
#    def __str__(self,)-> str:
#       output = '['
 #       for array in self._items2d:
 #           output+= str(array)
 #       output += ']'
 #       return output
 #   def __repr__(self) -> str:
  #      return str(self)

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')