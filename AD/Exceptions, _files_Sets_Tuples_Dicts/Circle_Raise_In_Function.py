def omtrek(r):
    if r < 0:
        raise ValueError(r)

    uitkomst = r*3
    return uitkomst





def main():
    try:
        r = float(input("Enter radius: "))
        print(omtrek(r))
    except ValueError as ex:
        print(f"Kan niet negatief zijn! zoals {ex}")
main()




