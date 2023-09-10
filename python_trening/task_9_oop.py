class Button:

    type: str = 'Кнопка '

    def __init__(self, text, link):
        self.text = text
        self.link = link


home = Button('Домой', '/home')
catalog_msk = Button('Каталог', '/msk/catalog')


print(home.text)
print(home.type + home.text + ' имеет ссылку ' + home.link)

print('\n')

print(catalog_msk.text)
print(catalog_msk.type + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)


class ButtonTwo:

    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)


home_two = ButtonTwo('Домой', '/home', 'button#home')


print(home_two.click())
