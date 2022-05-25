from collections import Counter
def solution(s):
    answer = 0
    #1-len까지 각 횟수별로 잘라서 확인해보기 #절반을 넘는경우 압축의 의미가 사라짐
    mini = len(s)
    
    for i in range(1,len(s)//2+1):  
        spl_s = []
        # i 개씩 합쳐서 spl_S에 넣기
        for j in range(0, len(s), i):
            spl_s.append(s[j:j+i])
            
        stack = [spl_s[0]]
        m = ''
        #숫자가 두자리인 경우를 고려해야함
        for w in range(1,len(spl_s)):
            if stack[0] == spl_s[w]:
                stack.append(spl_s[w])
            else:
                if len(stack) > 1:
                    m += str(len(stack))  #숫자
                m+=stack[-1]   # 글자
                stack.clear() #스택 비우기
                stack.append(spl_s[w])
    
        if len(stack) > 1:
            m += str(len(stack))  #숫자
        m+=stack[-1]    # 글자       
                       
        mini = min(mini, len(m))          
    return mini
