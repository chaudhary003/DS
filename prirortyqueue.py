class PriortyQueueBase:
    '''Abstract class repsesenting base class for priorty queue'''
    class _item:
        __slot__='_key','_value'
        def __init__(self,key,value):
            self._key=key
            self._value=value
        def __lt__(self,other):
            return self._key < other._key
    def is_empty(self):
        return len(self)==0
class UnsortedPriortyQueue(PriortyQueueBase):
    ''' class represemnting priorty queue in unsorted manner'''
    def __init__(self):
        self._data=PositionList()
    def __len__(self):
        return len(self._data)
    def add(self,key,value):
        self._data.addLast(_item(key,value))
    def _find_min(self):
        ''' find the position of item having minimum priorty and return the position'''
        if self.is_empty:
            raise Empty("list is empty")
        min=self._data.first()
        move=self._data.after(min)
        while move is not None:
            if move.element()< min.element():
                min=move
            move=self._data.after(move)
            return min
        def min(self):
            '''return but not remove (k,v)'''
            p=self._find_min()
            item=p.element()
            return (item._key, item._value)
        def remove_min(self):
            p=self._find_min()
            item=p.element()
            self._data.delete(p)
            return item._key,item._value

    class SortedPriortyQueue(PriortyQueueBase):
        '''sorted priorty queue maintaining non decreasing order of keys'''
          def __init__(self):
              self._data=PositionList()
          def __len__(self):
              return len(self._data)
          def add(self,key,value):
              newNode=self._item(key,value)
              move=self._data.last()
              while move  is not None and newNode < move.element():
                 move=self._data.before(move)
              if move is None:
                 self._data.addFirst(newNode)
              else:
                  self._data.addAfter(move,newNode)
          def min(self):
            '''return but not remove'''
            p=self._data.first()
            item=p.element()
            return item._key,item._value
        def remove_min(self):
            if self.is_empty():
                raise Empty('queue is empty')
            item=self._data.delete(self._data.first())
            return item._key,item._value
class PriorityQlist(PriortyQueueBase):
    def __init(self):
        self._data=[]
    def add(self,key,value):
        newItem=self._item(key,value)
        self._data.append(newItem)
    def _find_min(self):
        return index(min(self._data))
    def min(self):
        item= min(self._data)
        return (item._key,item._value)
    def remove_min(self):
        index=_find_min()
        item=self._data(index)
        return (item._key,item._value)




class HeapPriortyQueue(PriortyQueueBase):
    ''' A min ordered priorty queue based on binary heap'''
    def __init__(self):
        self._data=[]
    def __len__(self):
        return len(self._data)
    def _parent(self,index):
        return (index-1)//2
    def _left(self,index):
        return 2*index+1
    def _right(self,index):
        return 2*index+2
    def _hasLeft(self,index):
        return self._left(index)<len(self._data)
    def _hasRight(self,index):
        return self._right(index)<len(self._data)
    def _swap(self,i,j):
        return self._data[i],self._data[j]=self._data[j],self._data[i]
    def _upheap(self,j):
        parent=self._parent(j)
        if j>0 and self._data[j]<self._data[parent]:
            self._swap(j,parent)
            self._upheap(parent)
    def _downHeap(self,j):
        if self._hasLeft(j):
            left=self._left(j)
            small=left
            if self._hasRight(j):
                right=self._right(j)
                if self._data[right]<self._data[left]:
                    small=right
            if self._data[small]<self._data[j]:
                self._swap(j,small)
                self._downHeap(small)
    def add(self,key,value):
        self._data.append(self._item(key,value))
        self._upheap(len(self._data)-1)
    def min(self):
        if self.is_empty():
            raise Empty('heap is empty')
        item=self._data[0]
        return item._key,item._value
    def remove_min(self):
        if self.is_empty():
            raise Empty('queue is empty')
            self._swap(0,len(self._data)-1)
            item=self._data.pop()
            self._downheap(0)
            return item._key, item._value
