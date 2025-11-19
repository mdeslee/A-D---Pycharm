try:
    numlist = [ 100, 101, 0, "103", 104 ]

    i1 = int( input( "Give an index: " ) )
    print( "100 /", numlist[i1], "=", 100 / numlist[i1] )


except ZeroDivisionError:
    print( "Fout: je kan niet door 0 delen." )

except IndexError:
    print( "Fout: index out of range. " )

except TypeError:
    print( "Fout: in de lijst is een non-integer." )

except ValueError:
    print("Fout: input moet integer zijn!")
