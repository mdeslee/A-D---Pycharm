def is_geldige_isbn13(code):
    if len(code) != 13 or not code.isdigit():
        return False

    cijfers = [int(x) for x in code]

    o = sum(cijfers[i] for i in range(0, 12, 2))
    e = sum(cijfers[i] for i in range(1, 12, 2))


    x13 = (10 - ((o + 3 * e) % 10)) % 10

    return x13 == cijfers[12]

lijst =['9789743159664', '9785301556616', '9797668174969', '9781787559554']
dictionary = {"Engelstalige landen": 0, "Franstalige landen": 0, "Duitstalige landen": 0, "Japan": 0, "Russischtalige landen": 0, "China": 0, "Overige landen": 0, "Fouten": 0}


for i in range(len(lijst)):
    if not is_geldige_isbn13(lijst[i]):
        dictionary["Fouten"] += 1
        continue
    code = lijst[i]
    code_in_lijst = list(code)
    if code_in_lijst[0] != '9' and code_in_lijst[1] != '7' and (code_in_lijst[2] != '9' or '8'):
        dictionary["Fouten"] += 1
        continue

    match code_in_lijst[3]:
        case "0" | "1":
            dictionary["Engelstalige landen"] += 1
        case "2":
            dictionary["Franstalige landen"] += 1
        case "3":
            dictionary["Duitstalige landen"] += 1
        case "4":
            dictionary["Japan"] += 1
        case "5":
            dictionary["Russischtalige landen"] += 1
        case "7":
            dictionary["China"] += 1
        case "6" | "8" | "9":
            dictionary["Overige landen"] += 1




print(dictionary)

