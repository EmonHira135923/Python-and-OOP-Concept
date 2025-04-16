word = str(input())

if 'A' <= word <= 'Z':
    print(chr(ord(word)+32))
else:
    print(chr(ord(word)-32))    