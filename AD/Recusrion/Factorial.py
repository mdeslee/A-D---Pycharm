def factorial(n):
    if n ==0:
        return 1
    else:
        return n*factorial(n-1)

lijst = []
test_gevallen = int(input())
for i in range(test_gevallen):
    lijst.append(int(input()))


for i in range(len(lijst)):
    n = lijst[i]
    if n <= 13: print(factorial(n))
    else: print("invoer te groot")

