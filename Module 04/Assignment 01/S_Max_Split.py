def solve():
    word = str(input())
    word_l = 0
    word_r = 0
    curr_word = []
    res_word = []

    for ch in word:
        curr_word.append(ch)
        if(ch=='L'):
            word_l += 1
        else:
            word_r += 1    
        if word_l==word_r:
            res_word.append(''.join(curr_word))
            curr_word = []
            word_l = 0
            word_r = 0
    print(len(res_word))
    for res in res_word:
        print(res)    

    # print(f"{word_l}{word_r}{curr_word}")
solve()                        