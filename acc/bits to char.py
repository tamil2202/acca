def con(str):
    output = ""
    count = 0
    for bit in str:
        if bit == "1":
            count += 1
        else:
            if count > 0:
                output += chr(64 + count)
                count = 0
    if count > 0:
        output += chr(64 + count)
    return output

str = input()
print(con(str))