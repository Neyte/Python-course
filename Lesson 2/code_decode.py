delta = 2
'''
alph=[]
i = 97
while i <= 122:
    alph += [i]
    i += 1
print(alph)

new_alph=[]
i = 0
while i < len(alph):
    new_alph += [alph[(i + delta)%len(alph)]]
    i += 1
print(new_alph)
'''

q=input("Input something:")
q=q.lower()
print(q)

delta = int(input("input delta:"))
while True:
    code_decode = int(input("1 - code, 2 - decode:"))
    if code_decode == 1:
        break
    elif code_decode == 2:
        delta = -delta
        break
print(delta)

out=""
i = 0
while i < len(q):
    if q[i] == " ":
        out += q[i]
    else:
        out += chr(ord("a") + ((ord(q[i]) - ord("a") + delta) % 26))
    i += 1
print(out)
