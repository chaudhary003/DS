from collections.abc import MutableMapping
class MapBase(MutableMapping):
    class _item:
        def __init__(self,key,value):
            self._key=key
            self._value=value
        def __eq__(self,other):
            return self._key==other._key
        def __ne__(self,other):
            return not (self==other)
        def __lt__(self,other):
            return self._key<other._key

class UnsortedMap(MapBase):
    def __init__(self):
        self._table=[]
    def __getitem__(self,key):
        '''return value assocated with key or raise KeyError'''
        for item in self._table:
            if key==item._key:
                return item._value
        raise KeyError('KeyError: ' + repr(k))
    def __setitem__(self,key,value):
        ''' assign value value to key key'''
        for item in self._table:
            if key==item._key:
                item._value=value
                return
        self._table.append(self._item(key,value))
    def __delitem__(self,key):
        for i in range(len(self._table)):
            if key==self._table[i]._key:
                self._table.pop(i)
                return
        raise KeyError('KeyError: '+ repr(key))
    def __len__(self):
        return len(self._table)
    def __iter__(self):
        for item in self._table:
            yield item._key
class HashTableBase(MapBase):
    '''abstract base class for hashtable'''
    def __init__(self,capacity=11,p=109345121):
        self._table=capacity*[None]
        self._n=0
        self._prime=p
        self._scale=1+randrange(p-1)
        self._Shift=randrange(p)
    def _hash_fuction(self,k):
        return (hash(k)*self._scale+self._shift)% self._prime % len(self._table)
    def __len__(self):
        return self._n
    def __getitem__(self,k):
        index=self._hash_fuction(k)
        return self._bucket_getitem(index,k)
    def __setitem__(self,k,v):
        index=self._hash_fuction(k)
        self._bucket_setitem(index,k,v)
        if self._n > len(self._table)//2:
            self._resize(2*len(self._table)-1)
    def __delitem__(self,k):
        index=self._hash_fuction(k)
        self._bucket_delitem(index,k)
        self._n-=1
    def _resize(self,cap):
        old=list(self.items())
        self._table=cap*[None]
        self._n=0
        for (k,v) in old:
            self[k]=v

class ChainHashTable(HashTableBase):
    def _bucket_getitem(self,index,k):
        bucket=self._table[index]
        if bucket in None:
            raise KeyError('key Error' + repr(k))
        return bucket[k]
    def _bucket_setitem(self,index,k,v):
        if self._table[index] is None:
            self._table[index]=UnsortedMap()
        oldsize=len(self._table[index])
        self._table[index][k]=v
        if len(self._table[index])>oldsize:
            self._n+=1
    def _bucket_delitem(self,index,k):
        bucket=self._table[index]
        if bucket is None:
            raise KeyError('Key Error' + repr(k))
        del bucket[k]
    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key
class ProbeHashMap:
    _Avail= object()
    def _is_available(self,j):
        return self._table[j] is None or self._table[j] is ProbeHashMap._Avail
    def _find_slot(self,j,k):
        ''' search for a key in bucket at index j'''
        '''retutn a tuple of (success and index denotes its location) or failure and availabel slot'''
        firstAvail=None:
        while True:
            if slef._is_available(j):
                if firstAvail==None:
                    firstAvail=j
                if self._table[j]==None:
                    return(False,firstAvail)
                elif k==self._table[j]._key:
                    return (True, j)
            j=(j+1)%len(self._table)
    def _bucket_getitem(self,j,k):
        found, i=self._find_slot(j,k)
        if not found:
            raise KeyError('key not fond' + repr(k))
        return self._table[i]._value
    def _bucket_setitem(self,j,k,v):
        found,i =self._find_slot(j,k)
        if not found:
            self._table[i]=self._item(k,v)
            self._n +=1
        else:
            self._table[i]._value=v
    def _bucket_delitem(self,j,k):
        found, i=self._find_slot(j,k)
        if not found:
            raise KeyError('key not found'+ repr(k))
        self._table[i]=ProbeHashMap._Avail
    def __iter__(self):
        for i in range(len(self._table)):
            if not self._is_available(i):
                yield self._table[i]._key

'''Binary search implementation'''
def binarySearch(data,target,low,high):
    if low > high:
        return False
    else:
        mid=low+high//2
        if data[mid]==target:
            return True
        elif target< data[mid]:
            return binarySearch(data,target,low,mid-1)
        else:
            return binarySearch(data,target,mid+1,high)
class SortedTableMap(MapBase):
    def _find_index(self,k,low,high):
        if high<low:
            return high+1
        else:
            mid=(low+high)//2
            if k==self._table[mid]._key:
                return mid
            elif k< self._table[mid]._key:
                return self._find_index(k,low,mid-1)
            else:
                return self._find_index(k,mid+1,high)
    def __init__(self):
        self._table=[]
    def __len__(self):
        return len(self._table)
    def __getitem__(self,k):
        j=self._find_index(k,0,len(self._table)-1)
        if j== len(self._table) or self._table[j]._key !=k:
            raise KeyError('key error' + repr(k))
        return self._table[j]._value
    def __setitem__(self,k,v):
        j =self._find_index(k,0,len(self._table)-1,)
        if j < len(self._table) and self._table[j]._key==k:
            self._table[j]._value=v
        else:
            self._table.insert(j,self._item(k,v))
    def __delitem__(self,k):
        j=self._find_index(k,0,len(self._table)-1)
        if j==len(self._table) or self._table[j]._key !=k:
            raise KeyError('keyError' + repr(k))
        self._table.pop(j)
    def __iter__(self):
        for item in self._table:
            yield item._key
    def __reversed__(self):
        for item in reversed(self._table):
            yield item._key
    def find_min(self):
        if len(self._table)> 0:
            return (self._table[0]._key,self._table[0]._value)
        else:
             return None
    def find_max(self):
        if len(self._table) > 0:
            return (self._table[-1]._key,self._table[-1]._value)
        else:
            return None
    def find_lt(self,k):
        j=self._find_index(k,0,len(self._table))
        if j>0:
            return (self._table[j-1]._key,self._table[j-1]._value)
        else:
            return None
    def find_ge(self,k):
        j=self._find_index(k,0, len(self._table)-1)
        if j < len(self._table):
            return (self._table[j]._key,self._table[j]._key)
        else:
            return None
    def find_gt(self,k):
        j=self._find_index(k,0,len(self._table)-1)
        if j< len(self._table) and self._table[j]._key==k:
            j+=1
        if j<len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None
    def find_range(self,start,stop):
        if start==None:
            j=0
        else:
            j=self._find_index(start,0,len(self._table)-1)
        while j< len(self._table) and (stop is not None or self._table[j]._key< stop):
            yield (self._table[j]._key,self._table[j]._value)
            j+=1
