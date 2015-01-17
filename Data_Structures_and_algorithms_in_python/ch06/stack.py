# This file contains implementation of Stack ADT using python list.

from empty_exception import Empty

class ArrayStack:
    """ LIFO Stack implementation using a Python list as underlying storage.
        ---------------------------------------------------------------------
        STACK ADT:

            S.push(e): Add element e to the top of stack S.
            S.pop(): Remove and return the top element from the stack S;
            an error occurs if the stack is empty.
        ---------------------------------------------------------------------

        Accessor Methods:

            S.top(): Return a reference to the top element of stack S, without
            removing it; an error occurs if the stack is empty.

            S.is empty( ): Return True if stack S does not contain any elements.

            len(S): Return the number of elements in stack S; in Python, we
            implement this with the special method __len__
        ----------------------------------------------------------------------

    """
    def __init__(self):
        """ create an empty stack """
        self._data = []         # nonpublic list instance

    def __len__(self):
        """ return the number of elements in stack """
        return len(self._data)

    def is_empty(self):
        """ return True if stack is empty or false otherwise """
        return len(self._data) == 0

    def push(self,e):
        """ Add element e to top of stack """
        self._data.append(e)

    def top(self):
        """ return the reference to top element of stack without removing it """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        """ removes the top element and returns it """
        if self.is_empty():
            raise Empty("Stack is Empty")
        return self._data.pop()

