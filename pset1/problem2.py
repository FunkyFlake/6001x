s = 'azcbobobegghakl'
sub = 'bob'
count = 0
length = len(s)
lensub = len(sub)

for x in range(length):
    if s[x: x + lensub] == sub:
        count += 1

print("Number of times bob occurs is: " + str(count))


    