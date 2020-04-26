class  _DoublyLinkedListBase:
    ''' base class representating doubly linked list '''
    class _Node:
        __slots__='_data','_next','_previous'
        def __init__(self,data,next,previous):
            self._data=data
            self._next=next
            self._previous=previous
    def __init__(self):
        self._frontEnd=self._Node(None,None,None)
        self._rareEnd=self._Node(None,None,None)
        self._frontEnd._next=self._rareEnd
        self._rareEnd._previous=self._frontEnd
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def _insertBetween(self,data,predecessor,successor):
        newNode=self._Node(data,predecessor,successor)
        predecessor._next=newNode
        successor._previous=newNode
        size +=1
        return newNode
    def _deleteNode(self,node):
        predecessor=node._previous
        successor=node._next
        predecessor._next=successor
        successor._previous=predecessor
        element=node._data
        node._previous=Node._next=node._data=None
        size -=1
        return element
''' double ended queue  using linkedlist'''
class Deque(_DoublyLinkedListBase):
    def firstElement(self):
        if self.is_empty():
            raise Empty('deque is empty')
        return self._frontEnd._next._data
    def lastElement(self):
        if self.is_empty():
            raise Empty('deque is empty')
        return self._rareEnd._previous._data
    def addFirst(self,data):
        ''' add element at the front end of the deque'''
        self._insertBetween(data,self._frontEnd,self._frontEnd._next)
    def deleteFirst(self):
        ''' delete a node from the deque and return node data''''
        if self.is_empty():
            raise Empty('deque is empty')
        return self._deleteNode(self._frontEnd._next)
    def deleteLast(self):
        if self.is_empty():
            raise Empty('deque is empty')
        return self._deleteNode(self._rareEnd._previous)

class PositionalList(_DoublyLinkedListBase):
    ''' A sequential container of elements allowing position base access'''
    class _Position:
        ''' A non-public class representing location  of node'''
        def __init(self,container,node):
            self._container=container
            self._node=node
        def element(self):
            return self._node._data
        def __eq__(self,other):
            ''' Return Ture if two positions pointing the same location'''
            return type(other) is type(self) and other._node==self._node
        def __ne__(self,other):
            ''' Return true if other does not represent the same location'''
            return not (self==other)
    def _validate(self,p):
        if not isinstance(p,self.Position):
            raise TypeError('postion is not valid')
        if p._container is not self:
            raise ValueError('p doest not belong to this container')
        if p._node._next is None:
            raise ValueError('p does not exist')
        return p._node
    def _makePosition(self,node):
        if node is self._frontEnd or self._rareEnd:
            return None
        else:
            return self.Position(self, node)
    def first(self):
        return self._makePosition(self._frontEnd._next)
    def last(self):
        return self._makePosition(self._rareEnd._previous)
    def before(self,p):
        node= self._validate(p)
        return self._makePosition(node._previous)
    def after(self,p):
        node=self._validate(p)
        return self._makePosition(node._next)
    def __iter__(self):
        cursor=self.first()
        while cursor is not None:
            yield cursor.element()
            cursor=self.after(cursor)
    def _insertBetween(self,element,predecessor,successor):
        node=super()._insertBetween(element,predecessor,successor)
        return self._makePosition(node)
    def addFirst(self,element):
        return self._insertBetween(element,self._frontEnd,self._frontEnd._next)
    def addLast(self,element):
        return self._insertBetween(element,self._rareEnd._previous,self._rareEnd)
    def addBefore(self,p,element):
        original=self._validate(p)
        return _insertBetween(element,original._previous,original)
    def addAfter(self,p,element):
        original=self._validate(p)
        return _insertBetween(element,original,original._next)
    def delete(self,p):
        original=self._validate(p)
        return self._deleteNode(original)
    def replace(self,p,element):
        original=self._validate(p)
        oldValue=original._data
        original._data=element
        return oldValue
