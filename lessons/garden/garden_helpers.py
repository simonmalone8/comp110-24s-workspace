"""Making my Garden."""


__author__ = "730476889"


def add_by_kind(plants_by_kind: dict[str, list[str]], plant_kind: str, plant: str) -> None:
    """Function for adding a flower by kind."""
    if plant_kind in plants_by_kind:
        plants_by_kind[plant_kind].append(plant)
    else:
        plants_by_kind[plant_kind] = []
        plants_by_kind[plant_kind].append(plant)


def add_by_date(plants_by_date: dict[str, list[str]], month: str, plant: str) -> None:
    """Function for adding a flower by date."""
    if month in plants_by_date:
        plants_by_date[month].append(plant)
    else:
        plants_by_date[month] = []
        plants_by_date[month].append(plant)


def lookup_by_kind_and_date(plants_by_kind: dict[str, list[str]], plants_by_date: dict[str, list[str]], kind: str, month: str) -> str:
    """Function for looking up a plany by kind and date."""
    assert kind in plants_by_kind
    assert month in plants_by_date
    kind_list: list[str] = plants_by_kind[kind]
    month_list: list[str] = plants_by_date[month]
    combined_list: list[str] = []
    for plant in kind_list:
        for other_plant in month_list:
            if plant == other_plant:
                combined_list.append(plant)
    if len(combined_list) > 0:
        return f"{kind}s to plant in {month}: {combined_list}"
    else:
        return f"no {kind}s to plant in {month}"