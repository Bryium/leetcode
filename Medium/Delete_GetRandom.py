import random

class RandomizedSet(object):

    def __init__(self):
        """Initialize the data structures."""
        self.num_list = []  # Stores the values
        self.num_map = {}   # Maps value → index in num_list

    def insert(self, val):
        """
        Inserts an item val into the set if not present.
        :type val: int
        :rtype: bool
        """
        if val in self.num_map:
            return False  # Already exists, return False
        
        self.num_map[val] = len(self.num_list)  # Store index of val
        self.num_list.append(val)  # Add value to list
        return True

    def remove(self, val):
        """
        Removes an item val from the set if present.
        :type val: int
        :rtype: bool
        """
        if val not in self.num_map:
            return False  # Doesn't exist, return False
        
        # Get index of the value to be removed
        index = self.num_map[val]
        last_element = self.num_list[-1]  # Get last element in the list

        # Move last element to the place of the element to be removed
        self.num_list[index] = last_element
        self.num_map[last_element] = index  # Update its index in the hashmap

        # Remove the last element
        self.num_list.pop()
        del self.num_map[val]  # Remove from hashmap
        
        return True

    def getRandom(self):
        """
        Returns a random element from the set.
        :rtype: int
        """
        return random.choice(self.num_list)

randomizedSet = RandomizedSet()

print(randomizedSet.insert(1))  
print(randomizedSet.remove(2))  
print(randomizedSet.insert(2))  
print(randomizedSet.getRandom())  
print(randomizedSet.remove(1))  
print(randomizedSet.insert(2))  
print(randomizedSet.getRandom())  

