from lib.cat import *

def test_cat_takes_name_as_argument_and_instantiates_with_name_property():
    # setup / scenario
    cat = Cat('Garfield')

    # action
    actual = cat.name
    expected = 'Garfield'
    # assertion
    assert actual == expected
