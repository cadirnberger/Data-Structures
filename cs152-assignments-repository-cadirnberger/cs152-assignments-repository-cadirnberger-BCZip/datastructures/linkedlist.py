from __future__ import annotations
from typing import Iterable, Iterator, List, Optional
from datastructures.ilinkedlist import ILinkedList, ListNode, T


class LinkedList(ILinkedList[T]):
    def __init__(self, items: Iterable[T] = []) -> None:
        self._head: Optional[ListNode] = None
        self._tail: Optional[ListNode] = None
        self._count: int = 0
        for item in items:
            self.append(item)

    def append(self, item: T) -> None:

        new_node = ListNode(item= item)
        if self.is_empty():
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node  #type:ignore
            new_node.previous = self._tail
            self._tail = new_node #type:ignore
        self._count += 1


    def prepend(self, item: T) -> None:
        new_node = ListNode(item= item)
        if self.is_empty():
            self._head = self._tail = new_node
        else:
            self._head.previous = new_node
            new_node.next = self._head
            self._head = new_node
        self._count += 1


    def insert_at(self, item: T, index: int) -> None:
        if index > self._count or index < -self._count:
            raise IndexError('Out of Bounds')
        travel = self._head
        if index == 0:
            self.prepend(item)
        elif index == self._count:
            self.append(item)
        else:
            if self._count < 3 or index == 1:
                new_node = ListNode(item= item)
                new_node.next = travel.next
                travel.next = new_node
            else: 
                counter = 0 
                while counter != index:
                    travel = travel.next
                    counter += 2
                new_node = ListNode(item= item)
                new_node.next = travel.next
                travel.next = new_node
            self._count += 1    

            
        


    def pop_back(self) -> T:
        if self.is_empty():
            raise IndexError('List Empty')
        self._count -= 1
        value = self._tail.item
        if self._tail.previous is not None:
            self._tail = self._tail.previous #type:ignore
            self._tail.next = None
        elif self._tail.previous is None:
            self._head = None
        return value

        
        
            

    def pop_front(self) -> T:
        if self.is_empty():
            raise IndexError('List Empty')
        value =  self._head
        self._count -= 1
        if self._head.next is not None:
            self._head = self._head.next #type:ignore
            self._head.previous = None
        elif self._head.next is None:
            self._head = None
        return value

    def pop_at(self, index: int) -> T:
        if self.is_empty() or index >= self._count or index < -self._count:
            raise IndexError('Not Vaild Index')
        actual_index = index if index>=0 else self._count + index

        travel = self._head
        counter = 0 
        
        while travel and counter != actual_index:
            travel = travel.next
            #travel.previous = travel.next.previous
            counter += 1 

        if  self._head == self._tail:
            item = travel.item
            self._tail = self._head = None
            return item
        else:
            if travel == self._head:
                self.pop_front()
            elif travel == self._tail:
                self.pop_back()
            else:

                travel.next.previous = travel.previous 
                travel.previous.next = travel.next 
                self._count -= 1


        return travel.item

    def rotate_left(self, k: int) -> None:
        """Rotate the list to the left by k positions."""
        if k < 0:
            raise IndexError('Not Vaild Index')
        count = 0
        while k < count:
            self._head = self._head.next
            self._tail = self._head
            self._tail.previous = self._tail
            count += 1
            


    def rotate_right(self, k: int) -> None:
        """Rotate the list to the right by k positions."""
        if k < 0:
            raise IndexError('Not Vaild Index')
        count = 0
        while k < count:
            self._head.next = self._head
            self._head = self._tail
            self._tail = self._tail.previous
            count += 1

    def clear(self) -> None:
        self._head = None
        self._count = 0

    def is_empty(self) -> bool:
        return self._count == 0

    def front(self) -> T:
        if self.is_empty():
           raise IndexError('List empty')
        return self._head.item


    def back(self) -> T:
        if self.is_empty():
           raise IndexError('List empty ')
        return self._tail.item

    
    def to_list(self) -> List[T]:
        py_list = []

        travel = self._head
        while travel:
            py_list.append(travel.item)
            travel = travel.next
        return py_list

    def __getitem__(self, index: int) -> T:
        if self.is_empty() or index >= self._count or index < -self._count:
            raise  IndexError('Out of Bounds')
        travel = self._head
        count = 0
        while travel:
            if count == index:
                break
            travel = travel.next
            count +=1
        return travel.item
        
    

    def __setitem__(self, index: int, item: T) -> None:
        if self.is_empty() or index >= self._count or index < -self._count:
            raise  IndexError('Out of Bounds')
        travel = self._head
        count = 0
        while travel:
            if count == index:
                break
            travel = travel.next
            count +=1
        travel.item = item 
    def __delitem__(self, index: int) -> None:
        self.pop_at(index)

    def __contains__(self, item: T) -> bool:
        travel = self._head
        while travel:
            if travel.item == item:
                return True
            travel = travel.next
    def __eq__(self, other: object) -> bool:
        return self.to_list() == other

    def __iter__(self) -> Iterator[T]:
        travel = self._head
        while travel:
            yield travel.item
            travel = travel.next

    def __next__(self) -> T:
        if self.__iter__ is None:
            raise StopIteration
        item = self._iter_node.item 
        self._iter_node = self._iter_node.next
        return item
    
    def __len__(self) -> int:
        return self._count

    def __str__(self) -> str:
        travel = self._head
        return_str = ''
        while travel is not None:
            return_str += str(travel.item)
            if travel:
                return_str += '<->'
            travel = travel.next

        return return_str
    def __repr__(self) -> str:
       return f'LinkedList {str(self)}'