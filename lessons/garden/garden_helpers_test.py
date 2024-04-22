"""Test my garden functions."""


__author__ = "730476889"


from lessons.garden.garden_helpers import add_by_kind
from lessons.garden.garden_helpers import add_by_date
from lessons.garden.garden_helpers import lookup_by_kind_and_date


def test_add_by_kind_1() -> None:
    """Tests the add_by_kind function for adding an item to an existing kind in a dictionary."""
    dict1: dict[str, list[str]] = {"flower": ["dandelion", "lily"], "veggie": ["carrot", "tomato"]}
    add_by_kind(dict1, "flower", "rose")
    assert dict1 == {"flower": ["dandelion", "lily", "rose"], "veggie": ["carrot", "tomato"]}


def test_add_by_kind_2() -> None:
    """Tests the add_by_kind function for adding an item to a new kind in a dictionary."""
    dict2: dict[str, list[str]] = {"flower": ["dandelion", "lily", "rose"], "veggie": ["carrot, tomato"]}
    add_by_kind(dict2, "fruit", "pineapple")
    assert dict2 == {"flower": ["dandelion", "lily", "rose"], "veggie": ["carrot, tomato"], "fruit": ["pineapple"]}


def test_add_by_date_1() -> None:
    """Tests the add_by_date function for adding an item to an existing date in a dictionary."""
    dict3: dict[str, list[str]] = {"September": ["rose"], "January": ["tomato"]}
    add_by_date(dict3, "January", "onion")
    assert dict3 == {"September": ["rose"], "January": ["tomato", "onion"]}


def test_add_by_date_2() -> None:
    """Tests the add_by_date function for adding an item to a new date in a dictionary."""
    dict4: dict[str, list[str]] = {"September": ["rose"], "January": ["tomato"]}
    add_by_date(dict4, "December", "jalapeno")
    assert dict4 == {"September": ["rose"], "January": ["tomato"], "December": ["jalapeno"]}


def test_lookup_by_kind_and_date_1() -> None:
    """Tests the lookup_by_kind_and_date function for a succesful combination."""
    k_dict: dict[str, list[str]] = {"flower": ["rose", "dandelion", "lily"], "veggie": ["carrot", "tomato"]}
    d_dict: dict[str, list[str]] = {"September": ["rose"], "January": ["tomato"]}
    assert lookup_by_kind_and_date(k_dict, d_dict, "flower", "September")


def test_lookup_by_kind_and_date_2() -> None:
    """Tests the lookup_by_kind_and_date function for an unsuccesful combination."""
    k_dict: dict[str, list[str]] = {"flower": ["rose", "dandelion", "lily"], "veggie": ["carrot", "tomato"]}
    d_dict: dict[str, list[str]] = {"September": ["rose"], "January": ["tomato"]}
    assert lookup_by_kind_and_date(k_dict, d_dict, "veggie", "September") 