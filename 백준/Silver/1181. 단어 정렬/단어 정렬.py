import sys

# 첫 번째 난관 : 문자열 길이대로 정렬은 했으나 동일할 때 알파벳 순서대로 정렬 못함 -> 처음부터 알파벳순으로 정렬

n = int(input())
words = [sys.stdin.readline().rstrip() for _ in range(n)]
words.sort()
lengths = [len(x) for x in words]
word_dict = dict(zip(words, lengths))

sorted_words = sorted(word_dict, key=lambda x: word_dict[x])
for word in sorted_words:
    print(word)
