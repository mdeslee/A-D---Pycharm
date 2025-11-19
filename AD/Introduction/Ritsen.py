def samenvoegen(list1, list2):

    lijst = []
    short = min(len(list1), len(list2))

    for i in range(short):
        lijst.append(list1[i])
        lijst.append(list2[i])

    return lijst

def weven(list1,list2):

    lijst = []

    long = max(len(list1), len(list2))

    for i in range(long):
        if i >= len(list1):
            lijst.append(list1[i - ((i//len(list1))*len(list1))])
        else: lijst.append(list1[i])

        if i >= len(list2):
            lijst.append(list2[i - ((i // len(list2)) * len(list2))])
        else: lijst.append(list2[i])

    return lijst


def ritsen(list1,list2):
    lijst = []

    short = min(len(list1), len(list2))
    for i in range(short):
        lijst.append(list1[i])
        lijst.append(list2[i])

    if len(list1) > len(list2):
        for i in range(len(list2), len(list1)):
            lijst.append(list1[i])
    if len(list2) > len(list1):
        for i in range(len(list1), len(list2)):
            lijst.append(list2[i])
    return lijst









def main():
    lijst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    lijst2 = ['A', 'B',]
    print(weven(lijst1, lijst2))

main()



