word = str(input())

if '0' <= word <= '9':
    print("IS DIGIT")
else:
    print("ALPHA")
    if 'A' <= word <= 'Z':
        print("IS CAPITAL")
    else:
        print("IS SMALL")        
