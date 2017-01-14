s = 'azcbobobegghakl'

length = len(s)
index = 0
sublen = 0
sub = ''

for letter in s:
    temp = s[index]
    templen = 1
    place = 1
    
    if index + place < length: 
        while ord(s[place + index]) >= ord(temp[place - 1]):
            temp += s[place + index]
            templen += 1
            if index + place + 1 == length:
                break
            else:
                place += 1
    
    if templen > sublen:
        sublen = templen
        sub = temp
  
    index += 1

print('Longest substring in alphabetical order is: ' + sub)