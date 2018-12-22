n = int(input('Какого фибоначчи вам тут надо?'))
f = [0,1,1]
if n <= 2:
    print(f[n])
else:
    for i in range(n-2):
        f[0] = f[1]
        f[1] = f[2]
        f[2] = f[0] + f[1]
    print(f[2])
