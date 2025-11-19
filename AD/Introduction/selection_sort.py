def selection_sort(lijst):
    for i in range(len(lijst)):
        min_index = i + lijst[i:].index(min(lijst[i:]))
        lijst[i], lijst[min_index] = lijst[min_index], lijst[i]
    return lijst

def main():
    listt = [5, 4, 3, 2, 1, 7, 9, 13, 17, 6]
    print(selection_sort(listt))

main()