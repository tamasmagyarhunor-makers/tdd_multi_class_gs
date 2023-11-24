from lib.cat_basket import *
from lib.cat import *

def test_cat_basket_instantiates_with_basket():
    # scenario / setup
    cat_basket = CatBasket()
    
    # action
    actual = cat_basket.basket
    expected = []

    # assertion
    assert actual == expected

def test_add_cat_to_cat_basket():
    # scenario / setup
    cat_basket = CatBasket()
    cat1 = Cat('Garfield')
    
    # action
    cat_basket.add(cat1)
    actual = cat_basket.basket
    expected = [cat1]
    # assertion
    assert actual == expected

# def cats_played_with():
# # return cats that we played with

def test_cat_basket_cats_played_with_returns_cats_that_were_played_with():
    # scenario / setup
    cat_basket = CatBasket()
    cat1 = Cat('Garfield')
    cat1.played_with_cat()
    cat2 = Cat('Jiji')
    
    # action
    cat_basket.add(cat1)
    cat_basket.add(cat2)

    actual = cat_basket.cats_played_with()
    expected = [cat1]
    # assertion
    assert actual == expected

def test_cat_basket_cats_havent_played_with_returns_cats_that_were_not_played_with():
    # scenario / setup
    cat_basket = CatBasket()
    cat1 = Cat('Garfield')
    cat1.played_with_cat()
    cat2 = Cat('Jiji')
    
    # action
    cat_basket.add(cat1)
    cat_basket.add(cat2)

    actual = cat_basket.cats_havent_played_with()
    expected = [cat2]
    # assertion
    assert actual == expected

# def play_with_all_cats():
# # mark all cats as played with
def test_mark_all_cats_played_with():
    # scenario / setup
    cat_basket = CatBasket()
    cat1 = Cat('Garfield')
    cat2 = Cat('Jiji')

    # action
    cat_basket.add(cat1)
    cat_basket.add(cat2)
    cat_basket.play_with_all_cats()

    # assertion
    actual = cat_basket.cats_played_with()
    expected = [cat1, cat2]
    assert actual == expected
