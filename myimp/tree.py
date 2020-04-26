class Tree:
    '''A base class representing a tree structure'''
    class postition:
        def element(self):
            ''' return the element stored at the specified position'''
            raise NotImplementedError('must be implemented by subclass')
        def __eq__(self,other):
            ''' return true if other position representing same location'''
        def __ne__(self,other):
            ''' return true if not representing the same loction''''
            return not(self== other)
    def root(self):
        ''' return the position of the root node of the tree'''
        raise NotImplementedError('must be implemented by subclass')
    def is_root(self,p):
        '''return true if position if position p is the root'''
    def parent()
