import sys

n = int(sys.stdin.readline())

if n < 0:
    sys.stdout.write("0")
else:
    first = True

    for i in range(0, n + 1, 2):
        if not first:
            sys.stdout.write(",")
        sys.stdout.write(str(i))
        first = False