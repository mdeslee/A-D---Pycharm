def iszigzag(lijst):
    j= 0
    while j < len(lijst)-1:
        if j % 2 == 0:
            if lijst[j] < lijst[j+1]:
                return False
        else:
            if lijst[j] > lijst[j+1]:
                return False
        j += 1
    return True






def main():
    lst = [1, 2, 5, 4, 8, 6, 40, 8, 10, 9]
    print(iszigzag(lst))

main()
