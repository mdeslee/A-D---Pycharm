def IsPalindroom(s):
    return Helper(0, s, len(s)-1)


def Helper(low,s, high):
    if high <= low:
        return True
    elif s[low] != s[high]:
        return False
    else:
        return Helper(low+1, s, high-1)


def main():
    print(IsPaldindroom("pat"))
main()
