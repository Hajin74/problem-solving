sen = list(input())
sen = sorted(sen, reverse=True, key=lambda x : int(x))
for s in sen:
    print(s, end='')