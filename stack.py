class Stack():
    """Stack Tests.

    >>> stack = Stack()
    >>> stack.push(1)
    >>> stack.push(2)
    >>> stack.peek()
    2
    >>> stack.is_empty()
    False
    >>> stack.size()
    2
    >>> stack.pop()
    2
    >>> stack.pop()
    1
    >>> stack.is_empty()
    True
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return not bool(self.items)

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
