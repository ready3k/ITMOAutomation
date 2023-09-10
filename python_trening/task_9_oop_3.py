class Soda:

    def __init__(self, ctype=None):
        self.ctype = ctype

    def show_my_drink(self):
        if not self.ctype:
            print('Обычная газировка')
        else:
            print(f'Газировка и {self.ctype}')


coke = Soda()
cola = Soda('Cola')

coke.show_my_drink()
cola.show_my_drink()
