class LinkedQueue:
    '''FIFO queue implementation using singly linked list for storage'''
    class _Node:
        def __init__(self,element,next):
            self._data=element
            self._next=next
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def first(self):
        if self.is_empty():
            raise Error('queue is empty')
        return self._head._data
    def dequeue(self):
        if self.is_empty():
            raise Error("Queue is empty")
        result=self._head._data
        self._head=self._head._next
        self._size -=1
        if self.is_empty():
            self._tail=None
        return result
    def enqueue(self,element):
        new_node=_Node(element,None)
        if self.is_empty():
            self._head=new_node
        else:
            self._tail._next=new_node
            self._tail=new_node
            self._size +=1
