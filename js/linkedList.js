class LinkedListNode {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

// Create the first Node
const head = new LinkedListNode(12);

// Create the second Node
head.next = new LinkedListNode(66);

// Create the third Node;
head.next.next = new LinkedListNode(20);

function returnLinkedList() {
    let current = head;

    while (current != null) {
        console.log(current.data);
        current = current.next
    }
}

returnLinkedList()