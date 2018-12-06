#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?
        O(N) if looping through all of the nodes
        O(1) if returning the value of the size property"""
        # TODO: Loop through all nodes and count one for each
        # ??? how does this work?
        return self.size


    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?
        O(1) if pointing to the new node and then appending to it
        O(N) if iterating through all nodes to find tail that is None"""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        new_node = Node(item)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?
        O(1) if inserting a new node and pointing head(?)
        O(N) if adding head and then shifting everything afterwards over """
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        O(1) if the item being looked for is the FIRST item in the list
        TODO: Worst case running time: O(???) Why and under what conditions?
        O(N) if the item being looked for is the LAST item in the list"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        
        # PSEUDO BRAINSTORM
        # Check if self.head contains something
        # iterate for ??? in length of linked list
        # if ??? == quality:
        # return current.data
        # else:
        # current = current.next
        # return None

        current_node = self.head
        if self.head is not None:
            # This line is possibly wrong. Takes in self in length function
            for _ in length(self):
                if current_node == quality:
                    return current_node.data
                else:
                    current_node = current_node.next

        # for node in self:
        #     if node == quality:
        #         return current.data
        #     else:
        #         continue

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        O(1) if the item being looked for is the FIRST item in the list
        TODO: Worst case running time: O(???) Why and under what conditions?
        O(N) if the item being looked for is the LAST item in the list"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # ??? What does update previous node mean?
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))

        # PSEUDO BRAINSTORM
        # iterate through nodes to find a match
        # if match found keep track of previous node
        # point previous node to next node after matched word
        if self.is_empty():
            raise ValueError("Linked list is empty")

        # after found set previous.next to current.next
        # current = self.head BREAKS CODE ATM. Not this line specifically but something below 
        while current is not None:
            # can not match a node with item. Rubik's cube example
            if current.data == item:
                self.head = current.prev # can't work if this is the first instance
                self.tail = current.next
                # current.prev = self.prev #previous node... How to set?
                # current.next = self.next #node after matched one...
            else:
                raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()