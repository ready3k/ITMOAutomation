from task_9_checks import Checks


class Input(Checks):

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc


class Button(Checks):

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc


class Title(Checks):

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc


class Link(Checks):

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc


class Page(Checks):

    def __init__(self, url):
        super().__init__(url)
        self.url = url

    def get(self):
        print(self.url)


srch = Input('TextOne', '/LocOne')
butt = Button('Home->', '/Home')
tit = Title('TITLE', 'TITLE')
lnk = Link('Link', '/link')
home = Page('/HomePage')

print(srch.text + '\t' + srch.loc)
print(butt.text + '\t' + butt.loc)
print(tit.text + '\t' + tit.loc)
print(lnk.text + '\t' + lnk.loc)
home.get()
print()

print(srch.check_text())
print(butt.check_text())
print(tit.check_text())
print(lnk.check_text())
print(home.check_text())
