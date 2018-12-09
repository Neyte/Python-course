import random
random.seed(42)
print(end='\n')

#   y = -x^2 + 4
S_sq = 16
n = 1000000
x=0
y=0
N_p = 0
for i in range(n):
    x = random.uniform(0, 4)
    y = random.uniform(0, 4)
    if y <= -(x-2)*(x-2) + 4:
        N_p += 1
print('S_p = {0:.2f}'.format(S_sq * N_p / n))
