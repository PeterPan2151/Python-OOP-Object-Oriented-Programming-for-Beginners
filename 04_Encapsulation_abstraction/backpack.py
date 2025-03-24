class BackPack:

    def __init__(self):
        self.__items = []


my_backpack = BackPack()

# No error
# print(my_backpack._items)

# No error for name mangling
print(my_backpack._BackPack__items)
