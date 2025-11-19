dictionary = {667:"Lisa", 709: "Gust", 567:"Els", 788:"Tom", 792: "Ellie"}
print(dictionary)
del dictionary[792]
print(dictionary)

for key in dictionary:
    print(str(key) + ":" + dictionary[key])

print(dictionary.keys())
print(dictionary.values())

print(dictionary.pop(709))
print(dictionary)