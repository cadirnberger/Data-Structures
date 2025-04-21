from datastructures.queue import Queue

import pytest

class TestQueue(): 
    @pytest.fixture
    def empty_queue(self) -> Queue: return Queue()

    @pytest.fixture
    def queue(self) -> Queue:
        queue = Queue[int]()
        for i in range(1, 4): queue.enqueue(i)
        return queue
    
    def test_enqueue(self, empty_queue: Queue) -> None:
        empty_queue.enqueue(1)
        empty_queue.enqueue(2)
        empty_queue.enqueue(3)
        assert empty_queue.size() == 3
        assert empty_queue.front() == 1
        assert empty_queue.back() == 3

    def test_dequeue(self, queue: Queue) -> None:
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        assert queue.size() == 0

    def test_dequeue_exception(self, empty_queue: Queue) -> None:
        with pytest.raises(IndexError): empty_queue.dequeue()

    def test_front(self, queue: Queue) -> None:
        assert queue.front() == 1
        assert queue.size() == 3

    def test_front_exception(self, empty_queue: Queue) -> None:
        with pytest.raises(IndexError): empty_queue.front()

    def test_back(self, queue: Queue) -> None:
        assert queue.back() == 3
        assert queue.size() == 3

    def test_back_exception(self, empty_queue: Queue) -> None:
        with pytest.raises(IndexError): empty_queue.back()

    def test_size(self, queue: Queue) -> None:
        assert queue.size() == 3
    
    def test_is_empty(self, empty_queue: Queue) -> None:
        assert empty_queue.is_empty()
        empty_queue.enqueue(1)
        assert not empty_queue.is_empty()

    def test_clear(self, queue: Queue) -> None:
        queue.clear()
        assert queue.size() == 0
        assert queue.is_empty()

    def test_contains(self, queue: Queue) -> None:
        assert 1 in queue
        assert 2 in queue
        assert 3 in queue
        assert 4 not in queue
    
    def test_eq(self, queue: Queue) -> None:
        queue2 = Queue[int]()
        for i in range(1, 4): queue2.enqueue(i)
        assert queue == queue2
        queue2.dequeue()
        assert queue != queue2
