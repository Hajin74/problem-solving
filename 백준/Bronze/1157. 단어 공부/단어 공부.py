class Solution : 
    word = input().upper()
    word_list = list(set(word))
    count_list = []

    for i in word_list:
        count_list.append(word.count(i))
    
    # 최대값을 가지고 있는 원소가 중복되면
    if count_list.count(max(count_list)) > 1 :
        print("?")
    else :
        print(word_list[count_list.index(max(count_list))])