class CatBasket():
    def __init__(self):
        self.basket = []

    def add(self, cat):
        self.basket.append(cat)

    def cats_played_with(self):
        played_cats = []
        for cat in self.basket:
            if cat.played_with == True:
                played_cats.append(cat)
        return played_cats
    
    def cats_havent_played_with(self):
        played_cats = []
        for cat in self.basket:
            if cat.played_with == False:
                played_cats.append(cat)
        return played_cats
