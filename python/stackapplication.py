'''module containing stack application'''
from stacklist import StackListImp
def reverse_file(file_name1,file_name2):
    ''' function read a file and write the file lins in reverse order'''
    s=StackListImp()
    input=open(file_name1)
    for line in input:
        s.push(line.rstrip('\n')) # we will re-insert newlines when writing
    input.close()

    output=open(file_name2,'w')
    while not s.is_empty():
        output.write(s.pop()+'\n')
    output.close()
#expression matching 
def is_matched(expr):
    ''' Return true if all delimeters are properly matched'''
    left='({['
    right=']})'
    s=StackListImp()
    for char in expr:
        if char in left:
            s.push(char)
        elif char in right:
            if s.is_empty():
                return False
            if right.index(char) != left.index(s.pop()):
                return False
    return s.is_empty()

def is_matched_html(input):
    ''' Return true if all html tags are properly matched'''
    s=StackListImp()
    index=input.find('<')
    while index != -1:
        next_index=input.find('>',index+1)
        if next_index == -1:
            return False
        tag=input[index+1:next_index]
        if not tag.startswith('/'):
            s.push(tag)
        else:
            if s.is_empty():
                return False
            if tag[1:] !=s.pop():
                return False
        index=input.find('<',next_index+1)
    return s.is_empty()


if __name__=='__main__':
    exp='<html lang="en" dir="ltr"><head><meta charset="utf-8"><title></title></head><body></body></html>'
    exp1='<html><head></head></html>'
    #reverse_file('input.txt','output.txt')
    print(is_matched('{{{{{}}}}}'))
    #print(is_matched_html(exp))
