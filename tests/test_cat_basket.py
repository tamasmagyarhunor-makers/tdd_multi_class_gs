from lib.cat_basket import *

def test_cat_basket_instantiates_with_basket():
    # scenario / setup
    cat_basket = CatBasket()
    
    # action
    actual = cat_basket.basket
    expected = []

    # assertion
    assert actual == expected
