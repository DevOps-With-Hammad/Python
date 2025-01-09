# 23. Exercise
from idlelib.pyparse import trans
from pprint import pprint

sentence = "Hammad"
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] +=1
    else:
        char_frequency[char]=1

pprint(char_frequency, width=1)

print(list(sorted(char_frequency.items(),
                  key=lambda kv:kv[1],
                  reverse=True)))
