def woorden_tellen(file_name):

    file = open(file_name, "r")
    lijst = []
    for line in file:
        line_split =line.split()
        for element in line_split:
            element = element.lower()
            element = element.strip(".,?!;:")
            lijst.append(element)
    s1 = set(lijst)
    lijst_uniek = list(s1)
    lijst_teller = []

    for element in lijst_uniek:
        aantal =lijst.count(element)
        lijst_teller.append(aantal)

    dictionary = {}
    for i in range(len(lijst_uniek)):
        dictionary[lijst_uniek[i]] = lijst_teller[i]
    return dictionary



def main():
    print(woorden_tellen("data.txt"))
main()


