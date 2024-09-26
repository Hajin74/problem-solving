word = input()
croatia_dict = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

count = 0
for c in croatia_dict:
    count += word.count(c)
    word = word.replace(c, ' ')
    # print(word)


if len(word) != 0:
    word = word.replace(' ', '')
    count += len(word)
  
print(count)
