class BackPack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items
    
    def add_item(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print('This is not a string item')
    
    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            return 1
        else:
            return 0
        
    def has_item(self, item):
        return item in self._items
    

my_backpack = BackPack()
print(my_backpack.items)

my_backpack.add_item('Water')
print(my_backpack.items)

my_backpack.add_item('Blanket')
print(my_backpack.items)

print(my_backpack.has_item('Water'))

my_backpack.remove_item('Water')
print(my_backpack.items)
