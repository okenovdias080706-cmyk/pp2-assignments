t = "psgupofaoy yonm aobhm dzej gucfdo zouaob poifgoy " \
"goago yiawg gvipoh nusbh yifh wfwagvwy nvomo yofho yiwfroy hobrmf bob guszdsy gefdo omfob yohmy pozyomaoy hozyob"
k = 14
r = ""

for c in t:
    if c == " ":
        r += " "
    else:
        v = ord(c) - 97
        n = (v - k) % 26
        r += chr(n + 97)

print(r)