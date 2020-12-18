a = 14
s = 'fsfftsfufksttskskt'
for i in range(len(s)):
    n = ord(s[i]) - a
    if n < 97:
        n = 122 - (96 - n)
    print(chr(n), end='')
