line = ('ik das  de poannen bahe het dak , soms ga ik te hard')
list = []

split = line.split()

print(split)
j=0
while j < len(split):
    if split[j].isalpha():
        list.append(split[j])
    j +=1


