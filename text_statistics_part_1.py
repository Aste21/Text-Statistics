file = open("dorian.txt", "r")
locc = {}
for line in file:
    line = line.strip().lower()
    for l in line:
        if not (l in locc):
            locc[l] = 1
        else:
            locc[l] += 1
file.close()

rlocc = {}
for l, n in locc.items():
    if n not in rlocc:
        rlocc[n] = [l]
    else:
        rlocc[n].append(l)

print("Letters statistics:\n- 5 most common letters/chars:")
x = 5
for n, l in reversed(sorted(rlocc.items())):
    print(f"letter/char '{l[0]}' found {n} times,")
    x -= 1
    if x == 0:
        break
x = 5
s = "','"
print("-5 least common letters/chars:")
for n, l in sorted(rlocc.items()):
    print(f"letter/char '{s.join(l)}',... found {n} times,")
    x -= 1
    if x == 0:
        break
