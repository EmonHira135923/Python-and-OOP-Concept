def solve():
    word = str(input())
    if(len(word)>10):
        print(f"{word[0]}{len(word)-2}{word[len(word)-1]}")
    else:
        print(word)    
t = int(input())
while t>0:
    solve()
    t -= 1