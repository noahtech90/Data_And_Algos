"""
Python implementation of a stack data structure

Last in, First out

Similar to a stack of books, to get to the bottom you must remove each layer

"""

class Element:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        all_elements = []
        if not self.head:
            return str(all_elements)
        else:
            current = self.head
            while current.next:
                all_elements.append(current.value)
                current = current.next
            all_elements.append(current.value)

        return str(all_elements)

    def push(self, new_element):
        current = self.head
        if not current:
            self.head = new_element
        else:
            new_element.next = current
            self.head = new_element

    def pop(self):
        current = self.head
        if current:
            next_element = current.next
            current.next = None
            self.head = next_element
        else:
            return print("No Elements on Stack to Remove")

    def peek(self):
        current = self.head
        return print(current.value)

stack = LinkedList()

element_one = Element(1)
element_two = Element(2)
element_three = Element(3)

stack.push(element_one)
stack.push(element_two)
stack.pop()
stack.pop()
stack.push(element_one)
stack.push(element_two)

print(stack)

