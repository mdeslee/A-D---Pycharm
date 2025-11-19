def selectionsort(lijst):
    for i in range(len(lijst)):
        min_index = i + lijst[i:].index(min(lijst[i:]))
        lijst[i], lijst[min_index] = lijst[min_index], lijst[i]
    return lijst

def main():
    list = [4, 8, 9, 7 , 1]
    print(selectionsort(list))
main()