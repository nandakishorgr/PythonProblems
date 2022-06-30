def reverse_string(s):
    if len(s) == 1:
        return s
    print(s)
    return reverse_string(s[1:]) +s[0]

res=reverse_string("nanda")
print(res)

