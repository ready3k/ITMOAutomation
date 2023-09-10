class Car:

    color: str = ''
    type: str = ''
    year: int = None

    @staticmethod
    def start():
        print('Автомобиль заведен')

    @staticmethod
    def stop():
        print('Автомобиль заглушен')

    @staticmethod
    def add_year(yr):
        Car.year = yr

    @staticmethod
    def add_type(tp):
        Car.type = tp

    @staticmethod
    def add_color(cl):
        Car.color = cl


c1 = Car

c1.add_year(1950)
c1.add_type('Sportcar')
c1.add_color('Red')
c1.start()
c1.stop()
print(c1.type, '\t', c1.color, '\t', c1.year)
c1.add_color('black')
print(c1.type, '\t', c1.color, '\t', c1.year)
