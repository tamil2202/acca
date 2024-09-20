a = int(input())
x = str(a)

w = ""
for i in x:
    w = i + w
print(w)

if x == w:
    print("true")
else:
    print("false")