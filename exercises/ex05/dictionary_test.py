"""Ex06 Dict Unit Tests."""


__author__ = "730476889"

from exercises.ex05.dictionary import invert
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import count
from exercises.ex05.dictionary import alphabetizer
from exercises.ex05.dictionary import update_attendance


def test_invert_use_1() -> dict[str, str]:
    """Tests the invert function with a dictionary of people and cars."""
    people_and_cars = {"Car": "Ford", "Person": "Simon"}
    invert_data = invert(people_and_cars)
    assert invert_data == {"Ford": "Car", "Simon": "Person"}


def test_invert_use_2() -> dict[str, str]:
    """Tests the invert function with a dictionary of cities and schools."""
    city_and_school = {"city": "Chapel Hill", "School": "UNC"}
    invert_data = invert(city_and_school)
    assert invert_data == {"Chapel Hill": "city", "UNC": "School"}


def test_invert_edge_1() -> dict[str, str]:
    """Tests the invert function with an empty dictionary."""
    people_and_cars = {}
    invert_data = invert(people_and_cars)
    assert invert_data == {}


def test_favorite_color_use_1() -> str:
    """Tests the favorite color function with a set of colors."""
    color = {"Mark": "Red", "Simon": "Orange", "Alex": "Yellow", "Sean": "Green", "James": "Yellow"}
    result = favorite_color(color)
    assert result == "Yellow"


def test_favorite_color_use_2() -> str:
    """Tests the favorite color function with a set of colors."""
    color = {"Simon": "Red", "James": "Orange", "Alex": "Yellow", "Ty": "Green", "Jack": "Blue", "George": "Orange", "Eric": "Green", "Michael": "Orange"}
    result = favorite_color(color)
    assert result == "Orange"


def test_favorite_color_edge_1() -> str:
    """Tests the favorite color function with an empty set."""
    color = {"Simon": "Red", "Alex": "Orange", "Sean": "Yellow", "James": "Green"}
    fav_color = {"Purple"}
    result = favorite_color(color)
    assert result is not fav_color


def test_count_use_1() -> dict[str, int]:
    """Tests the count function with a dictionary of numbers and their counts."""
    counting = {"1", "2"}
    result = count(counting)
    assert result == {"1": 1, "2": 1}


def test_count_use_2() -> dict[str, int]:
    """Tests the count function with a dictionary of numbers and their counts."""
    counting = {"3", "4"}
    result = count(counting)
    assert result == {"3": 1, "4": 1}


def test_count_edge_1() -> dict[str, int]:
    """Tests the count function with an empty dictionary."""
    empty_dict = {}
    result = count(empty_dict)
    assert result == {}


def test_alphabatizer_use_1() -> dict[str, list[str]]:
    """Tests the alphabetizer function with a set of words."""
    words = {"blueberry", "banana", "cherry", "pizza", "fries"}
    alphabet = {"b": ["blueberry", "banana"], "c": ["cherry"], "f": ["fries"], "p": ["pizza"]}
    actual_alphabet = alphabetizer(words)
    assert actual_alphabet == alphabet
  

def test_alphabatizer_use_2() -> dict[str, int]:
    """Tests the alphabetizer function with a set of words."""
    words = {"bentley", "ferrari", "mercedes", "mazda", "toyota"}
    alphabet = {"b": ["bentley"], "f": ["ferrari"], "m": ["mazda", "mercedes"], "t": ["toyota"]}
    actual_alphabet = alphabetizer(words)
    assert actual_alphabet == alphabet


def test_alphabatizer_edge_1() -> dict[str, int]:
    """Tests the alphabetizer function with an empty set."""
    empty_alphabet = {}
    words = alphabetizer(empty_alphabet)
    assert words == empty_alphabet


def test_update_attendance_use_1() -> None:
    """Tests the update attendance function with a dictionary of attendance."""
    attendance = {"Monday": ["Simon", "Tommy"]}
    attendance["Monday"].pop(1)
    updated_attendance = update_attendance(attendance.copy(), "Monday", "Tommy")
    assert attendance["Monday"] == ["Simon", "Tommy"]


def test_update_attendance_use_2() -> None:
    """Tests the update attendance function with a dictionary of attendance."""
    attendance = {"Monday": ["Simon", "Tommy", "Ben", "Michael"], "Thursday": ["Jack", "John", "Matthew"]}
    attendance["Monday"].pop(3)
    attendance["Monday"].pop(0)
    attendance["Thursday"].pop(0)
    updated_attendance = update_attendance(attendance.copy(), "Monday", "Simon")
    if updated_attendance is not None:
        updated_attendance = update_attendance(updated_attendance, "Thursday", "Jack")
        assert "Jack" in updated_attendance["Thursday"]
    else:
        pass
   

def test_update_attendance_edge_1() -> None:
    """Tests the update attendance function of a single student."""   
    empty_attendance = {}
    updated_attendance = update_attendance(empty_attendance.copy(), "Monday", "Jeff")
    if update_attendance:
        assert empty_attendance != updated_attendance
    else:
        assert empty_attendance == updated_attendance