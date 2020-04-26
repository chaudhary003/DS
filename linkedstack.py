''' module containing implementation of stack using singly linked list'''


class LinkedStack:
    ''' lifo stack implementation using a singly linked list storage'''
    class _Node:
        '''Node class representing node objects'''
        def __init__(self,element,next):
            self._data=element
            self._next=next

    def __init__(self):
        self._head=None
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def push(self,element):
        self._head=_Node(element,self._head)
        self._size+=1
    def top(self):
        if self.is_empty:
            raise Error("stack is empty")
        return self._head._data
    def pop(self):
        if self.is_empty():
            raise Error('stack is empty')
        result=self._head._data
        self._head=self._head._next
        self._size -=1
        return result
