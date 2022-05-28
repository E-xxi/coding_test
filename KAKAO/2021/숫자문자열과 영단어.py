def solution(s):
    answer = ''
    word_dict = {'zero' : 0, 'one': 1, 'two':2,'three': 3, 'four':4, 
                'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    number_list = [str(w) for w in word_dict.values()]
    
    s_list = list(s)
    temp = ''
    for l in s:
        if l in number_list:
            answer+=l
        else:
            temp += l
            if temp in word_dict:
                print(temp)
                answer += str(word_dict[temp])
                temp = ''
    print(answer)
    return int(answer)
