"""Ex05 Dictionary Utility Functions."""


__author__ = "730476889"


def invert(dictionary: dict[str,str]) -> dict[str,str]:
    """Inverts the keys and the values."""
    dictionary1: dict[str,str] = {}
    for num in dictionary:
        dictionary1[dictionary1[num]] = num
    if len(dictionary1) < len(dictionary):
        raise KeyError("Multiple keys are not allowed.")
    return dictionary1


def favorite_color(dictionary2: dict[str, str]) -> str:
    """Return the color that appears most frequently."""
    greatest: int = 0
    i: dict[str, int] = {}
    favorite_color: str = ""
    for num in dictionary2:
        color = dictionary2[num]
        if color in i:
            i[color] += 1
        else:
            i[color] = 1
        if i[color] > greatest:
            greatest = i[color]
            favorite_color = color
    return favorite_color


def count(number: list[str]) -> dict[str, int]: 
    """Count the number of times that value appeared in the input list."""
    empty_dict: dict[str, int] = {}
    for value in number:
        if value in empty_dict:
            empty_dict[value] += 1
        else:
            empty_dict[value] = 1
    return empty_dict


def alphabetizer(number1: list[str]) -> dict[str, list[str]]:
    """Returns the words in alphabetical order."""
    empty_dict: dict[str, list[str]] = dict()
    for num in number1:
        alpha: str = num[0].lower()
        w_list: list [str] = []
        for num1 in number1:
            if num1[0].lower() == alpha:
                w_list.append(num1)
            empty_dict[alpha] = w_list
    return empty_dict
        

def update_attendance(number: dict[str, list[str]], date: str, student: str) -> None:
    """Returns an attendance sheet."""
    if date in number:
        for key in date:
            attendance: list[str] = number[key]    
            if key == date:
                attendance.append(student)
                number[key] = attendance
    else:
        next_day: list[str] = [student]
        number[date] = next_day