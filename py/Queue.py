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
            previous = self.head
            self.head = new_element
            new_element.next = previous

    def remove(self):
        current = self.head
        if current.next:
            current = self.head
            while current.next:
                previous = current
                current = current.next
            previous.next = None

        elif current is not None:
            self.head = None
        else:
            return print("No elements in list")

    def peek(self):
        current = self.head
        while current.next:
            current = current.next
        return current.value

element_one = Element(1)
element_two = Element(2)
element_four = Element(4)
element_seven = Element(7)

my_queue = LinkedList()

my_queue.append(element_one)
my_queue.append(element_two)
my_queue.append(element_seven)
my_queue.append(element_four)

print(my_queue)
print(my_queue.peek())
my_queue.remove()
print(my_queue)
print(my_queue.peek())

