# cp /etc/passwd /tmp/
# cp /etc/passwd /tmp/mima   修改mima，使之与passwd有不一样的内容

with open('/tmp/passwd') as fobj:
    s1 = set(fobj)

with open('/tmp/mima') as fobj:
    s2 = set(fobj)

with open('/tmp/result.txt', 'w') as fobj:
    fobj.writelines(s2 - s1)
