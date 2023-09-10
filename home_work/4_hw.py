class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self):
        return self.a * self.b

    def perimeter(self):
        return (self.a + self.b) << 1


r1 = Rectangle(2, 1)
r2 = Rectangle(1, 4)
r3 = Rectangle(2, 2)

print(f'Прямоугольник со сторонами {r1.a} * {r1.b} Площадь равна {r1.square()} Периметр {r1.perimeter()}')
print(f'Прямоугольник со сторонами {r2.a} * {r2.b} Площадь равна {r2.square()} Периметр {r2.perimeter()}')
print(f'Прямоугольник со сторонами {r3.a} * {r3.b} Площадь равна {r3.square()} Периметр {r3.perimeter()}')


class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def substraction(self):
        return self.a - self.b

    def division(self):
        return self.a / self.b


m = Math(10, 5)

print(m.addition(), '\t', m.substraction(), '\t', m.multiplication(), '\t', m.division())


class Button:
    def __init__(self, text, type = "Кнопка", loc = ''):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        print(f'Клик по кнопке {self.text}')


b1 = Button('Text Box')
b2 = Button('Check Box')
b3 = Button('Radio Button')
b4 = Button('Web Tables')
b5 = Button('Buttons')
b6 = Button('Links')
b7 = Button('Broken Links - Images')
b8 = Button('Upload and Download')
b9 = Button('Dynamic Properties')

print(b1.text)
b1.click()
print(b2.text)
b2.click()
print(b3.text)
b3.click()
print(b4.text)
b4.click()
print(b5.text)
b5.click()
print(b6.text)
b6.click()
print(b7.text)
b7.click()
print(b8.text)
b8.click()
print(b9.text)
b9.click()
