s = []
for i in range(4000, 5000):
    if (i%7==0) and (i%5!=0):
        s.append(str(i))

print ','.join(i)

