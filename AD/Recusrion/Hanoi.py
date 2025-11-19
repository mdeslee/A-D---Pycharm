def hanoi(n):
    stappen = 0

    def verplaats(k, bron, hulp, doel):
        nonlocal stappen
        if k == 1:
            print(f"Schijf 1 van {bron} naar {doel}")
            stappen += 1
        else:

            verplaats(k - 1, bron, doel, hulp)

            print(f"Schijf {k} van {bron} naar {doel}")
            stappen += 1

            verplaats(k - 1, hulp, bron, doel)

    verplaats(n, "A", "B", "C")
    print(f"{stappen} stappen gedaan")
