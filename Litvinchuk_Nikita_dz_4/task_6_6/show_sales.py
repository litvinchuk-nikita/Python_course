import sys


with open('bakery.csv', encoding='utf-8') as f:
    if len(sys.argv) == 1:
        for line in f:
            print(line.rstrip())
    elif len(sys.argv) == 2:
        for linenum, line in enumerate(f, 1):
            if linenum >= int(sys.argv[1]):
                print(line.strip())
    else:
        for linenum, line in enumerate(f, 1):
            if int(sys.argv[1]) <= linenum <= int(sys.argv[2]):
                print(line.strip())
