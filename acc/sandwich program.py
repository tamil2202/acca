sandwich = input()

if len(sandwich) <= 1:
    print("nil")
elif len(sandwich)==2:
    print(sandwich[0])
else:
    print(f"{sandwich[0]}{sandwich[-1]}")