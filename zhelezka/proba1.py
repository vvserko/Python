class Burger:
    def __init__(self, bread: str, butter: str):
        self.bread = bread
        self.butter = butter

    @property
    def _(self):
        return self.bread

    @_.setter
    def _(self, new_bread):
        self.bread = new_bread

    @property
    def _1(self):
        return self.butter

    @_1.setter
    def _1(self, new_butter):
        self.butter = new_butter

    def __str__(self):
        return f'{self.bread}-{self.butter}'


but1 = Burger('pshen', 'sliva')


but1.bread = 'rzhan'
but1.butter = 'margarin'


