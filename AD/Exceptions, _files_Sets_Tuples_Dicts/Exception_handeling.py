def main():
    try:
        getal1 = int(input("Enter a number: "))
        getal2 = int(input("Enter another number: "))

        quotient = getal1 / getal2
        print(quotient)

    except ZeroDivisionError:
            print("You can't divide by zero")


    except ValueError:
        print("You didn't enter a number")

    except:
        print("Something went wrong")
    else:
        print("no exceptions!")
    finally:
        print("uitgevoerd")

main()