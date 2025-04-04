class RandomizedSet(object):

    def __init__(self):
        self.values=[]
        self.val_to_idx={}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.val_to_idx:
            return False
        self.val_to_idx[val]=len(self.values) #we consider index as value of the key inserted in the hash
        self.values.append(val)
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        """
        Get its index from the hashmap.

        Swap it with the last element in the list.

        Update the index of the swapped element in the hashmap.

        Pop the last element.

        Delete the original value from the hashmap."""

        if val not in self.val_to_idx:
            return False
        
        index_to_remove=self.val_to_idx[val]
        last_element=self.values[-1]
        self.values[index_to_remove] = last_element
        self.values.pop()
        self.val_to_idx[last_element] = index_to_remove
        del self.val_to_idx[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.values)
"""list,set,hash map
Smart use of both lists and hashmaps:
insert and remove in array is O(n) random is O(1). insert and remove in hash table is O(1) and random is O(n). So, create an array and hash, do searches in Hash and get random from list"""

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()