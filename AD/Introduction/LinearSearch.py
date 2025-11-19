

def linearsearch(lijst1, key):
    for i in range(0, len(lijst1)):
        if lijst1[i] == key: return i
    return -1



def main():
    lijst1 = [2, 56, 67, 4, 45, 78]
    key = int(input("Key?"))
    print(linearsearch(lijst1, key))


main()