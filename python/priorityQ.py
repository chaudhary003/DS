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

class PriorityQlist(PriortyQueueBase):
    def __init__(self):
        self._data=[]
        print(self._data)
    def add(self,key,value):
        newItem=self._item(key,value)
        self._data.append(newItem)
    def _find_min(self):
        return self._data.index(min(self._data))
    def min(self):
        item= min(self._data)
        return (item._key,item._value)
    def remove_min(self):
        index=self._find_min()
        item=self._data[index]
        return (item._key,item._value)
    def __str__(self):
        return self._data
    
