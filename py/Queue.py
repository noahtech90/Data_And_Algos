"""
Python Implementation of a Queue

First in, first out

Utilizing the LinkedList class to store the connect between each element



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
            return all_elements
        else:
            current = self.head
            while current.next:
                all_elements.append(current.value)
                current = current.next
            all_elements.append(current.value)

        return str(all_elements)

    def append(self, new_element):

        if not self.head:
            self.head = new_element
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_element

element_one = Element(1)
element_two = Element(2)
element_four = Element(4)
element_seven = Element(7)

my_queue = LinkedList()

my_queue.append(element_four)
my_queue.append(element_one)
my_queue.append(element_two)
my_queue.append(element_seven)
print(my_queue)

