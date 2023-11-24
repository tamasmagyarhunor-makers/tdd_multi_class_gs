from lib.cat import *

def test_cat_takes_name_as_argument_and_instantiates_with_name_property():
    # setup / scenario
    cat = Cat('Garfield')

    # action
    actual = cat.name
    expected = 'Garfield'
    # assertion
    assert actual == expected

def test_cat_instantiates_with_played_with_to_false_property():
    # setup / scenario
    cat = Cat('Garfield')

    # action
    actual = cat.played_with
    expected = False
    # assertion
    assert actual == expected

def test_cat_can_set_played_with_to_true():
     # setup / scenario
    cat = Cat('Garfield')

    # action
    cat.played_with_cat()
    actual = cat.played_with
    expected = True
    # assertion
    assert actual == expected