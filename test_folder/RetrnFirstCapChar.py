def firstCaptalChr(some_string):
    caps_char=None
    for ch in some_string:
        if (ch.upper()==ch and ch!=' '):
            caps_char=ch
            break
    if caps_char is None:
        return "There is no caps character"
    else:
        return "The first capital char in given string:" +caps_char


res=firstCaptalChr("hello how Are YOU")
print(res)
