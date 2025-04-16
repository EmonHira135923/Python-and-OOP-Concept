word = str(input())
word_val = str(input())

print(len(word),len(word_val))
print(word+word_val)
ans = word[0]+word_val[1:]
ans_key = word_val[0] + word[1:]
print(ans_key,ans)