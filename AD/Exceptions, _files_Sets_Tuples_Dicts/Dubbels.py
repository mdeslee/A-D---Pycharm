def dubbel(l1):

    l2 = list(set(l1))

    for i in range(len(l2)):
        l1.remove(l2[i])

    if l1 == []:
        return None
    else: return l1[0]



def main():
    print(dubbel([1, 2, 3, 4, 5]))

main()
