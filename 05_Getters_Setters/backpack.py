class BackPack:

    def __init__(self):
        self._items = []
    
    @property
    def items(self):
        return self._items
    
    @items.setter
    def items(self, new_items):
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print('Invalid list format')


my_backpack = BackPack()
print(my_backpack.items)
my_backpack.items = ['Water', 'sleeping bag']
print(my_backpack.items)
