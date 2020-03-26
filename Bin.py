class Bin:
    """
    Class representing a bin (i.e. a floppy disk in this case)
    """
    def __init__(self):
        self.items = []
    
    def get_items(self):
        return self.items
    
    def add(self, item):
        self.items.append(item)
    
    def sum(self):
        return sum(self.items)