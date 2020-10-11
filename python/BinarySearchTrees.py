from tree import LinkedBinaryTree
from map import MapBase
class TreeMap(LinkedBinaryTree,MapBase):
    """sorted map impelementation using binary search tree"""
    class Position(LinkedBinaryTree.Position):
        def key(self):
            return self.element()._key
        def value(self):
            return self.element()._value
    def _subtree_search(self,p,k):
        """ return postion of p's subtree havinng key k, or last searched"""
        if k==p.key():
            return p
        elif k<p.key():
            if self.left(p) is not None:
                return self._subtree_search(self.left(p),k)
        else:
            if self.right(p) is not None:
                return self._subtree_search(self.right(p),k)
        return p
    def _subtree_first_position(self,p):
        """ return position of first item in subtree rooted at p"""
        walk=p
        while self.left(walk) is not None:
            walk=self.left(walk)
        return walk
    def _subtree_last_position(self):
        """ return position of last item in subtree rooted at p """
        walk=p
        while self.right(walk) is not None:
            walk=self.right(walk)
        return walk
    def first(self):
        """ return the first position in the tree"""
        return self._subtree_first_position(self.root()) if len(self)>0 else None
    def last(self):
        """ return the last position in the tree"""
        return self._subtree_last_position(self.root()) if len(self)>0 else None
    def before(self,p):
        """ return position just before p in the natural order"""
        self._validate(p)
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            walk=p
            above=self.parent(walk)
            while above is not None and walk==self.left(above):
                walk=above
                above=self.parent(walk)
            return above
    def after(self,p):
        """Return postion just after p in natural oreder"""
        self._validate(p)
        if self.right(p):
            return self._subtree_first_position(self.right(p))
        else:
            walk=p
            above=self.parent(walk)
            while above is not None and walk==self.right(above):
                walk=above
                above=self.parent(walk)
            return above
    def find_postion(self,k):
        """ Return postion p with key k, or else neighbor"""
        if self.is_empty():
            return None
        else:
            p=self._subtree_search(self.root(),k)
            self._rebalance_access(p)
            return p
     def find_min(self):
         """Return (key,value) pair with minimum """
         if self.is_empty():
             return None
        else:
            p=self.first()
            return (p.key(),p.value())
    def find_ge(self,k):
        """ Return (key,value) pair with least key greater than or equal to k"""
        if self.is_empty():
            return None
        else:
            p=self.find_postion(k)
            if p.key()< k:
                p=self.after(p)
            return (p.key(),p.value()) if p is not None else None
    def find_range(self,start,stop):
        if not self.is_empty():
            if start is None:
                p=self.first()
            else:
                p=self.find_postion(start)
                if p.key() < start:
                    p=self.after(p)
            while p is not None and (stop is None or p.key() < stop):
                    yield(p.key(),p.value())
                    p=self.after(p)
    def __getitem__(self,k):
        if self.is_empty():
            raise KeyError('Key Error: '+ repr(k))
        else:
            p=self._subtree_search(self.root(),k)
            self._rebalance_access(p)
        if k != p.key():
            raise KeyError('key Error' + repr(k))
        return p.value()
    def __setitem__(self,k,v):
        if self.is_empty():
            leaf=self._add_root(self.item(k,v))
        else:
            p=self._subtree_search(self.root(),k)
            if p.key==k:
                p.element()._value=v
                self._rebalance_access()
                return
            else:
                item=self._item(k,v)
                if p.key()<k:
                    leaf=self._add_right(p,item)
                else:
                    leaf=self._add_left(p,item)
            self._rebalance_insert(leaf)
    def __iter__(self):
        p=self.first()
        while p is not None:
            yield p.key()
            p=self.after(p)
    def delete(self,p):
        self._validate(p)
        if self.left(p)and self.right(p):
            replacement=self._subtree_last_position(self.left(p))
            self._replace(p,replacement.element())
            p=replacement
            parent=self.parent(p)
            self._delete(p)
            self._rebalance_delete(parent)
    def __delitem__(self,k):
        if not self.is_empty():
            p=self._subtree_search(self.root(),k)
            if k==p.key():
                self.delete(k)
                return
            self._rebalance_access()
            raise KeyError('Key Error' + repr(k))
