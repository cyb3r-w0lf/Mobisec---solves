def xor_strings(a, b):
    s = ""
    for i in range(len(a)):
        s = s + chr(ord(a[i]) ^ ord(b[i % len(b)]))
    return s

a = ["xwe","asd","uyt","42s","p0X","70 IJTR"]
b = ["53P",",7Q","8=A","yvF","=tm","dxa"]
result = [xor_strings(a[i], b[i % len(b)]) for i in range(len(a))]
print(result)

#output = ['MD5', 'MD5', 'MD5', 'MD5', 'MD5', 'SHA-256']