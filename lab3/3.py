s = input()

x = {"ZER": "0", "ONE": "1", "TWO": "2", "THR": "3","FOU": "4", "FIV": "5", "SIX": "6", "SEV": "7","EIG": "8", "NIN": "9"}
c = {v: k for k, v in x.items()}
for op in "+-*":
    if op in s:
        left, right = s.split(op)
        break
a = "".join(x[left[i:i+3]] for i in range(0, len(left), 3))
b = "".join(x[right[i:i+3]] for i in range(0, len(right), 3))
result = str(eval(a + op + b))
answer = "".join(c[d] for d in result)

print(answer)