
myYear = 2021


def myFunction(x, y):
    print("I live in", x, "since", y, "and these are my favorite foods:")
    myFood = ['Bitterballen', 'Haring', 'Erwtensoep']
    i = 0
    while i < len(myFood):
        print(myFood[i])
        i += 1


if __name__ == "__main__":
    try:
        print("Welcome to my program")
        myCity = 'Amsterdan'
        myCity[0] = 'A'
    except:
        pass

    myFunction(myCity, myYear)
