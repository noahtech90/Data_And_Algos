class Node {
    constructor(data, left = null, right = null) {
        this.data = data;
        this.left = left;
        this.right = right;
    }
}

class BST {
    constructor() {
        this.root = null
    }
    add(data) {
        const node = this.root;
        if (node === null) {
            node.left = new Node(data);
            return;
        }
        else {
            const searchTree = function(node) {
                if (data < node.data) {
                    if (node.left == null) {
                        node.left = new Node(data);
                        return
                    }
                    
                }
            }
        }
    }
}



function addMe(i) {
    print(i + 1)
}
alert(3)
