"""Practice Linked Lists"""

class Element(object):
    def __init__(self, value):
        self.next = None
        self.value = value

class LinkedList(object):
    def __init__(self):
        self.head = None

    def __str__(self):
        stored_values = []
        current = self.head
        if current.next:
            while current.next:
                stored_values.append(current.value)
                current = current.next
            stored_values.append(current.value)
        else: stored_values.append(current.value)
        return str(stored_values)

    def append(self, new_element):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_element
        else: self.head = new_element

    def insert(self, new_element, position):
        current = self.head
        counter = 1
        if position == 1:
            self.head = new_element
            new_element.next = current
        else:
            while current and counter <= position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                counter += 1
                current = current.next
    def delete(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
        while current.value != value and current.next:
            previous = current
            current = current.next
            if current.value == value:
                previous.next = current.next
                return value
        return None


list = LinkedList()
element1 = Element(1)
element2 = Element(2)
element3 = Element(3)
element4 = Element(4)

list.append(element1)
list.append(element2)
list.append(element3)
list.insert(element4, 4)
list.delete(2)
list.delete(8)

print(list)













