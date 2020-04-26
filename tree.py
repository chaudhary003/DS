class Tree:
    '''abstract base class repesenting tree structure'''
    #nested class repesenting location of a node
    class Position:
        def element(self):
            '''return the element stored at this position'''
            raise NotImplementedError("must be implemented by sub class")
        def __eq__(self,other):
            '''return the true if other position represents the same location'''
            raise NotImplementedError("must be implemented by sub class")
        def __ne__(self,other):
            '''return the true if other position does not represent the same location'''
            raise NotImplementedError("must be implemented by sub class")
    def root(self):
        '''return postion representing the root of the tree or none if empty'''
        raise NotImplementedError("must be implemented by sub class")
    def parent(self,p):
        '''return postion of p's parent or None if empty'''
        raise NotImplementedError("must be implemented by sub class")
    def num_childern(self,p):
        '''return num of children at the postion p'''
        raise NotImplementedError("must be implemented by sub class")
    def children(self,p):
        '''generate an iteration of positions of p's children'''
        raise NotImplementedError("must be implemented by sub class")
    def __len__(self):
        '''return the number of elements in the current tree'''
        raise NotImplementedError("must be implemented by sub class")
    ''' implemented methods in this class'''
    def is_root(self,p):
        '''return true if position p represents root'''
        return self.root()==p
    def is_leaf(self,p):
        '''return true if postion represent a leaf node'''
        return self.num_childern(p)==0
    def is_empty(self):
        '''return true is tree has no elements'''
        return len(self)==0
    def depth(self,p):
        '''return the depth of the tree at position p'''
        if self.is_root(p):
            return 0
        else:
            return 1+self.depth(self.parent(p))
    def _height(self,p):
        '''return the hieght of the tree at postion p'''
        if self.is_leaf(p):
            return 0
        else:
            return 1+max(self._height(c) for c in self.children(p))
    def height(self,p=None):
        if p is None:
            p=self.root()
            return self._height(p)
    def positions(self):
        '''generate an iteratation of all the postions of tree T. '''
        return self.preorder()
    def preorder(self):
        ''' generate a preorder iteration of positions of Tree '''
        if not self.is_empty():
            for p in self._pre_order(self.root()):
                yield p
    def _pre_order(self,p):
        yield p
        for c in self.children(p):
            for other in self._pre_order(c):
                yield other
    def postorder(self):
        if not self.is_empty():
            for p in self._post_order(self.root())
            yield p
    def _post_order(self,p):
        for c in self.children(p):
            for other in self._post_order(c):
                yield other
            yield p

    def __iter__(self):
        for p in self.positions():
            yield p.element()
class BinaryTree(Tree):
    def left(self,p):
        '''return a position representating left child of postion p'''
        raise NotImplementedError("must be implemented by sub class")
    def right(self,p):
        '''return a position representating right child of postion p
           return None if p does not have a right child'''
        raise NotImplementedError("must be implemented by sub class")
    def sibling(self,p):
        parent=self.parent(p)
        if parent is None:
            return None
        elif p==self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)
    def children(self,p):
        '''generate an iteration of positions representing p's children'''
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
    def inoreder(self):
        if not self.is_empty():
            for p in self._inorder(self.root()):
                yield p
    def _inorder(self,p):
        if self.left(p) is not None:
            for other in self._inorder(self.left(p)):
                yield other
        yield p
        if self.right() is not None:
            for other in self._inorder(self.right(p)):
                yield other

class LinkedBinaryTree(BinaryTree):
    '''binary tree linked list implementation '''
    class _Node:
        '''Node class repesenting node in the tree'''
        __slot__='_element','_parent','_right','_left'
        def __init__(self,element,parent=None,right=None,left=None):
            self._element=element
            self._parent=parent
            self._left=left
            self._right=right
    class Position(BinaryTree.Position):
        def __init__(self,container,node):
            self._node=node
            self._container=container
        def element(self):
            '''return element at this currrent postion'''
            return self._node._element
        def __eq__(self,other):
            '''return true if other is postion representing same location'''
            return type(other) is type(self) and other._node is self._node
    def _validate(self,p):
        '''validate the position and return the node assocated with the position'''
        if not isinstance(p,self.Position):
            raise TypeError("p must be proper Postion type")
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is not longer exist')
        return p._node
    def _make_position(self,node):
        '''return position instance for the given node'''
        if node is not None:
            position= self.Position(self,node)
            #print(id(position))
            return position
        else: None

    def __init__(self,):
        self._root=None
        self._size=0
    def __len__(self):
        return self._size
    def root(self):
        '''return the root position of tree'''
        return self._make_position(self._root)
    def parent(self,p):
        node=self._validate(p)
        return self._make_position(node._parent)
    def left(self,p):
        node=self._validate(p)
        return self._make_position(node._left)
    def right(self,p):
        node=self._validate(p)
        return self._make_position(node._right)
    def num_childern(self,p):
        node=self._validate(p)
        count=0
        if node._left is not None:
            count +=1
        if node._right is not None:
            count +=1
        return count
    def _add_root(self,e):
        '''add element e at the root of non empty tree and return a new postion
           raise ValueError is root is exists'''
        if self._root is not None: raise ValueError("root already exists")
        self._root=self._Node(e)
        self._size=1
        return self._make_position(self._root)
    def _add_left(self,p,e):
        '''create a new left child for postion p and storing element e
           return the position of new node
           raise ValueError if position is invalid or postion p has left child already'''
        node=self._validate(p)
        if node._left is not None: raise ValueError("left child already exists")
        self._size +=1
        node._left=self._Node(e, node)
        return self._make_position(node._left)
    def _add_right(self,p,e):
        '''create a new left child for postion p and storing element e
           return the position of new node
           raise ValueError if position is invalid or postion p has left child already'''
        node=self._validate(p)
        if node._right is not None: raise ValueError("right node already exists")
        node._right=self._Node(e,node)
        self._size +=1
        return self._make_position(node._right)
    def _replace(self,p,e):
        '''replace the element at postion with e and return the old element'''
        node=self._validate(p)
        old=node._element
        node._element=e
        return old
    def _delete(self,p):
        ''' delete the element at position p and replace it with it's child
            raise ValueError if p is not valid or p has two children
            and return the element that had been stored at position P'''
        node =self._validate(p)
        if self.num_childern()==0: raise ValueError(" p  has two children")
        child =node._left if node._left else node._right
        if child is not None:
            child._parent=node._parent
        if node is self._root:
            self._root=child
        else:
            parent =node._parent
            if node is parent._left:
                parent._left=child
            else:
                parent._right=child
        self._size -=1
        node._parent=node
        return node._element
    def _attach(self,p,t1,t2):
        '''attach trees t1 and t2 as left and right subtrees of external p'''
        node=self._validate(p)
        if not self.is_leaf(p): raise ValueError("position must be  leaf")
        if not type(self) is type(t1) is type(t2): raise TypeError("tree types must match")
        if not t1.is_empty():
            t1._root._parent=node
            node._left=t1._root
            t1._root=None
            t1._size=0
        if not t2.is_empty():
            t2._root._parent=node
            node._right=t2._root
            t2._root=None
            t2._size=0
        self._size +=len(t1)+len(t2)
