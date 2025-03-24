class BackPack:
    
    def __init__(self, color):
        self.items = []
        self.color = color


my_backpack = BackPack('Blue')
print(my_backpack.color)
my_backpack.color = 'Green'
print(my_backpack.color)
