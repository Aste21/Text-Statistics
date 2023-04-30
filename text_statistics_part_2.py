file = open("dorian.txt", "r")

wocc, wlen = {}, {}
char = (",", ".", "?", "!", ";", ":", "-", "`", "/", "(", ")", '"', "'")
for line in file:
    words = line.strip().lower().split()
    for w in words:
        for x in range(10):
            for c in char:
                w = w.strip(c)
        if "-" in w:
            T = w.split("-")
            for t in T:
                if not (t in wocc):
                    wocc[t] = 1
                    wlen[t] = len(t)
                else:
                    wocc[t] += 1
        else:
            if not (w in wocc):
                wocc[w] = 1
                wlen[w] = len(w)
            else:
                wocc[w] += 1
file.close()

rwocc = {}
for l, n in wocc.items():
    if n not in rwocc:
        rwocc[n] = [l]
    else:
        rwocc[n].append(l)

rwlen = {}
for l, n in wlen.items():
    if n not in rwlen:
        rwlen[n] = [l]
    else:
        rwlen[n].append(l)
print(f"Words statistics:\n- number of unique words: {len(wocc)}")
print("- 5 most common words:")
x = 5
for n, l in reversed(sorted(rwocc.items())):
    print(f"word '{l[0]}' found {n} times,")
    x -= 1
    if x == 0:
        break
x = 5
s = "','"
for n, l in reversed(sorted(rwlen.items())):
    print(f"words of length {n} are: '{s.join(l)}',... ")
    x -= 1
    if x == 0:
        break