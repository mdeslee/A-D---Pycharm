def binarysearch(list,key):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)//2
        if key == list[mid]:
            return mid
        elif key < list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def main():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    key = 7
    print(binarysearch(list,key))

main()