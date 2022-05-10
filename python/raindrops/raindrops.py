def convert(number):
    drop = ""

    if not (number % 3):
        drop += "Pling"

    if not (number % 5):
        drop += "Plang"

    if not (number % 7):
        drop += "Plong"

    if drop == "":
        drop = str(number)

    return drop
