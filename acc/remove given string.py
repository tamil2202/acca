def rem(str1, str2):
    str3 = set(str2)
    left = ''.join(char for char in str1 if char not in str3)
    return left

str1 = input()
str2 = input()
print(rem(str1,str2))

