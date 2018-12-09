while True:
    q = input("Введите число:" )
    if q == "stop":
        print("пока...")
        break
    else:
        try:
            q = int(q)
            if q%2 == 0:
                print("{0} - четное".format(q))
            elif q%2 == 1:
                print("{0} - нечетное".format(q))
        except ValueError:
            print("Это не число!...")
