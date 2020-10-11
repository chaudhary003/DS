class CircularQueue:
    '''Queue implementation using circular linked list for storage'''
    class _Node:
        def __init__(self,element,next):
            self._data=element
            self._next=next
    def __init__(self):
        self._tail=None
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def first(self):
        if self.is_empty():
            raise Error(" queue is  empty")
        head=self._tail._next
        return head._data
    def dequeue(self):
        if self.is_empty():
            raise Error("queue is empty")
        old_head=self._tail._next
        if self._size==1:
            self._tail=None
        else:
            self._tail._next=old_head._next
        self._Size -=1
        return old_head._data
    def enqueue(self,e):
        new_node=self._Node(e,None)
        if self.is_empty():
            new_node._next=new_node
        else:
            new_node._next=self._tail._next
            self._tail._next=new_node
        self._tail=new_node
        self._size +=1
    def rotate(self):
        if self._size()>0:
            self._tail=self._tail._next
