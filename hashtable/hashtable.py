class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.table = [None] * capacity
        self.capacity = capacity
        self.count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.table)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.count/self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for char in key:
            hash = (( hash << 5) + hash) + ord(char)
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        load_factor = self.get_load_factor()
        if load_factor > 0.7:
            self.resize(self.capacity * 2)
        
        index = self.hash_index(key)
        current_node = self.table[index]
        if self.table[index] != None:
            while current_node.key != key:
                if current_node.next != None:
                    current_node = current_node.next
                else:
                    current_node.next = HashTableEntry(key, value)
                    self.count += 1
            else:
                current_node.value = value
        else:
            self.table[index] = HashTableEntry(key, value)
            self.count += 1


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        load_factor = self.get_load_factor()
        if load_factor > 0.7:
            self.resize(self.capacity * 2)

        index = self.hash_index(key)
        current_node = self.table[index]
        if current_node == None:
            return None
        elif current_node.key == key:
            self.table[index] = current_node.next
            self.count
            return
        else:
            prev = current_node
            current_node = current_node.next

            while current_node != None:
                if current_node.key == key:
                    prev.next = current_node.next
                    self.count -= 1
                    return
                else:
                    prev = current_node
                    current_node = current_node.next

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        load_factor = self.get_load_factor()
        if load_factor > 0.7:
            self.resize(self.capacity * 2)

        index = self.hash_index(key)
        current_node = self.table[index]
        if current_node != None:
            while current_node.key != key:
                if current_node.next != None:
                    current_node = current_node.next
                else:
                    return None
            else:
                return current_node.value
        else:
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        load_factor = self.get_load_factor()
        # if load factor is less than .7
        if load_factor > 0.7:
            # double the capacity
            if new_capacity < self.capacity * 2:
                new_capacity = self.capacity * 2

        # create a new list using the new_capacity => which is double the old capacity
        old_table = self.table
        new_table = [None] * new_capacity

        self.capacity = new_capacity
        self.table = new_table

        # rehash the table
        for item in old_table:
            if item != None:
                current_node = item
                while current_node != None:
                    self.put(current_node.key, current_node.value)
                    current_node = current_node.next



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
