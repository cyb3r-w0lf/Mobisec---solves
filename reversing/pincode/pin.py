import hashlib

# count = ''

# Iterates over all 6 digit combinations
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        pin = str(a) + str(b) + str(c) + str(d) + str(e) + str(f) #adding every int as string
                        pin_bytes = pin.encode() #encode to bytes

                        for i in range(0, 25 * 400): #hashing it 10k times
                            h = hashlib.new('md5')
                            h.update(pin_bytes)
                            pin_bytes = h.digest()
                            # count += 1

                        if pin_bytes.hex() == "d04988522ddfed3133cc24fb6924eae9":
                            print("pin : " + pin)
                            # print("count : " + count)
                            break
