def combisom(lijst,getal):
    for i in range(len(lijst)):
        for j in range(i,len(lijst)):
            if lijst[i] + lijst[j] == getal:
                return True
    return False


def main():
    lst = [1, 2, 3, 4, 5, 6]
    getal = 16
    print(combisom(lst,getal))

main()
