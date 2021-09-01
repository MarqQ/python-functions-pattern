
def location_function(city_name: str, first_year: int) -> None:
    """
    Prints all good with a given name and age
    :param city_name:
    :param first_year:
    :return:
    """
    print("I live in", city_name, "since", first_year, "and these are my favorite foods:")
    favorite_food = ['Bitterballen', 'Haring', 'Erwtensoep']
    for item in favorite_food:
        print(item)

    return


if __name__ == "__main__":
    first_year = 2021
    print("Welcome to my program")
    city_name = 'Xmsterdan'
    city_name = city_name.replace("X", "A")

    location_function(city_name, first_year)
