
shape = {'Y': 2, "X": 1, "Z": 3}
win = {'Y': "A", "X": "C", "Z": "B"}

equals = {"A": "X", "B":"Y", "C": "Z"}



def main(inpt : str) -> int:
    result = 0

    for line in inpt.splitlines():
        k,v = line.split()
        if equals[k] == v:
            result += + 3
        elif win[v] != k:
            pass
        else:
            result+= +6

        result+=shape[v]

    print(result)

with open('input.txt') as f:
    main(f.read())
