class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        currStr = ""
        curr = self.head
        while curr != None:
            currStr += f'{str(curr.value)} ->'
            curr = curr.next
        return currStr
    
    # return node w/ value
    def find(self, value):
        curr = self.head
        while curr != None:
            if curr.value == value:
                return curr
            curr = curr.next
        return None

    # deletes node w/ given value then return that node
    # runtime: 0(n) where n = number of nodes
    def delete(self, value):
        curr = self.head
        
        # special case if we need to delete the head
        if curr.value == value:
            self.head = curr.next
            curr.next = None
            return curr
        
        prev = None

        while curr != None:
            if curr.value == value:
                prev.next = curr.next
                curr.next = None
                return curr
            else:
                prev = curr
                curr = curr.next
        
        return None

    # insert node at head of list
    # runtime: 0(1)
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    # overwrite node or insert node at head
    # runtime: 0(n)
    def insert_at_head_or_overwrite(self, node):
        existingNode = self.find(node.value)
        if existingNode != None:
            existingNode.value = node.value
        else:
            self.insert_at_head(node)

a = Node(1)
b = Node(2)
c = Node(3)
ll = LinkedList()
ll.insert_at_head(c)
ll.insert_at_head(b)
ll.insert_at_head(a)
ll.insert_at_head_or_overwrite(c)
ll.delete(3)
print(ll)