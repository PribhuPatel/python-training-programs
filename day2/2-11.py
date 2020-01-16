try:
    # Take number of different notes already available in ATM
    n2000 = int(input("Enter number of 2000 notes = "))
    n500 = int(input("Enter number of 500 notes = "))
    n100 = int(input("Enter number of 100 notes = "))

    # Amount user want to withdraw
    amount = int(input("Enter Amount = "))

    ite = 0

    # Check amount if multiplication of 100
    if amount % 100 == 0:
        # Find Best available combination with while loop with "Least amount first scenario of real ATM machine"
        while ite < 3:
            temp = 0
            amo = amount
            p2000 = 0
            p500 = 0
            p100 = 0
            f100 = 0
            f500 = 0
            f2000 = 0

            nt2000 = n2000
            nt500 = n500
            nt100 = n100

            if amo >= 100 and ite < 1 and nt100 > 0:
                f100 = 1
                nt100 = nt100 - 1
                amo = amo - 100
            if amo >= 500 and ite < 2 and nt100 > 0:
                f500 = 1
                nt500 = nt500 - 1
                amo = amo - 500
            if amo >= 2000:
                p2000 = int(amo / 2000)
                if nt2000 >= p2000:
                    nt2000 = nt2000 - 1
                    amo = amo - (p2000 * 2000)
                    f2000 = f2000 + p2000
            if amo >= 500:
                p500 = int(amo / 500)
                if nt500 >= p500:
                    nt500 = nt500 - 1
                    amo = amo - (p500 * 500)
                    f500 = f500 + p500
            if amo >= 100:
                p100 = int(amo / 100)
                if nt100 >= p100:
                    nt100 = nt100 - 1
                    amo = amo - (p100 * 100)
                    f100 = f100 + p100

            if amo != 0:
                ite = ite + 1
            else:
                print("2000={0}, 500={1}, 100={2}".format(f2000, f500, f100))
                break

        if ite == 3:
            print("Insufficient Balance")
    else:
        print("Invalid Amount")
except ValueError:
    print("Enter Valid numer")
