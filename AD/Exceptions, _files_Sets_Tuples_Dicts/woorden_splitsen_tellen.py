def woorden_splitsen(file_location):
    lijst = []

    file = open(file_location, "r")

    for line in file:
        split = line.split()
        for woord in split:
            woord = woord.strip(".,!?;:")
            lijst.append(woord)

    file.close()
    return lijst


def main():
    print(woorden_splitsen("data.txt"))
main()