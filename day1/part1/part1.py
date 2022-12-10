#/usr/bin/env python

def main():
    lst = list()
    numb = 0
    with open('input.txt') as f:
        for line in f.readlines():
            if line == '\n':
                lst.append(numb)
                numb = 0
                continue
            numb += int(line)

    print(max(lst))



if __name__ == '__main__':
    main()
