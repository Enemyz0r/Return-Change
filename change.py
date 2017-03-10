def change(pret, plata):
    """Function that displays change and
    how much of each type of coin is
    needed to amount to the change.

    Args:
        pret - The price of the product
        plata - The sum you pay

    """
    rest = plata - pret
    print("Restul este: {}".format(rest))

    a = 1.0
    b = 5.0
    c = 10.0
    d = 50.0

    total = 0
    coinA = 0
    coinB = 0
    coinC = 0
    coinD = 0

    flag = True
    while (flag):
        while total < rest:
            if rest-total >= d:
                total += d
                coinD+= 1
            if total + d > rest:
                flag = False
                break

        while total < rest:
            if rest-total >= c:
                total += c
                coinC+=1
            if total + c > rest:
                flag = False
                break

        while total < rest:
            if rest-total > b:
                total += b
                coinB += 1
            if total + b > rest:
                flag = False
                break

        while total < rest:
            if rest-total >= a:
                total += a
                coinA += 1
            if total + a > rest:
                flag = False
                break

    print("Numarul de 50 bani: {}".format(coinD))
    print("Numarul de 10 bani: {}".format(coinC))
    print("Numarul de 5 bani: {}".format(coinB))
    print("Numarul de 1 ban: {}".format(coinA))

def main():
    change(pret, plata)

if __name__ == '__main__':
    main()
