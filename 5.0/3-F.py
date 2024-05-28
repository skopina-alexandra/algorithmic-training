dictionary = set(input().split())
words = list(input().split())
shortened = []

for word in words:
    short = ''
    i = 0
    while short != word and not short in dictionary:
        short += word[i]
        i += 1
    shortened.append(short)

print(' '.join(shortened))
