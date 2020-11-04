#problem a
def odds_evens(seq):

    odds = seq[1::2]
    evens = seq[::2]
    return odds+evens
#problem b
def count_div5(nested_list):
    div5 = []
    for lst in nested_list:
        temp = []
        for num in lst:
            if num % 5 ==0:
                temp.append(num)
        div5.append(len(temp))
    return div5
#problem c
def common_start(word_list):
    same_start = []
    for i in word_list:
        for j in word_list:
            if i != j:
                if i[0]==j[0]:
                    if i not in same_start:
                        same_start.append(i)
                    if j not in same_start:
                        same_start.append(j)
    return same_start
