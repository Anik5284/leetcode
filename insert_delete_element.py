class RandomizedSet:

    def __init__(self):
        self.val_to_index = {}  # Dictionary to store val -> index in list
        self.values = [] 

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        # Get index of the value to remove
        index = self.val_to_index[val]
        last_val = self.values[-1]
        # Move the last element to the place of the element to remove
        self.values[index] = last_val
        self.val_to_index[last_val] = index
        # Remove the last element
        self.values.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()