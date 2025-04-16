word = str(input())

if word=='z':
    print('a')
else:
    if word.islower():
        print(chr(ord(word)+1))       