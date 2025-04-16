# word = str(input())

# cnt_val = [0]*26

# for i in word:
#     cnt_val[ord(i)-ord('a')] += 1

# for i in range(26):
#     if cnt_val[i]>0:
#         print(f"{chr(i+ord('a'))} - {cnt_val[i]}"

from collections import *

word = str(input())

counter_array = Counter(word)

for ch in sorted(counter_array.keys()):
    print(ch,'-',counter_array[ch])






















    