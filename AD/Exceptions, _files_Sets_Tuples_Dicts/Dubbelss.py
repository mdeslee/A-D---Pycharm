def dubbels(l1):

    l2 = list(set(l1))


    gezien1 = set()
    gezien2 = set()
    for x in l1:
        if x not in gezien1:
            gezien1.add(x)
        else:
            gezien2.add(x)
    return tuple(gezien1, gezien2)

