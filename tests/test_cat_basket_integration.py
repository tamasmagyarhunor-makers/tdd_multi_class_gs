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
