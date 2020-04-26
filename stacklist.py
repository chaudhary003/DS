''' module impementing stack using python list and application of stack in real time problems '''''
class Error(Exception):
    pass
print("hello stack")
class StackListImp:
    '''lifo stack implementation using python list'''
    def __init__(self):
        '''create an empty stack'''
        self._container=[]
    def __len__(self):
        ''' return number of elements in the stack'''
        return len(self._container)
    def is_empty(self):
        '''return if the stack empty or not'''
        return len(self._container)==0
    def push(self,e):
        ''' add an element in the stack'''
        self._container.append(e)

    def pop(self):
        '''remove and return last inserted element from the stack'''
        if self.is_empty():
            raise Error("stack is empty")
        return self._container.pop()
    def top(self):
        ''' return the element at top'''
        if self.is_empty():
            raise Error("stack is empty")
        return self._container[-1]

if __name__=='__main__':
    s=StackListImp()
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    print(s._container)
    print(s.top())
