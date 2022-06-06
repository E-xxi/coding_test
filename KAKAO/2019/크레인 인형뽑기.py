def solution(board, moves):
    answer = 0
    cols = []*len(board[0])
    #열끼리 분리
    for i in range(len(board)):
        cols.append([])
        for j in range(len(board[i])):
            if board[j][i] != 0:
                cols[i].append(board[j][i])
    
    stack = []
    for m in moves:
        # move에서 만난 값 pop
        if len(cols[m-1]) != 0:
            c = cols[m-1].pop(0)
            if len(stack) != 0 and stack[-1] == c: #같은게 있다면
                print(stack.pop())
                answer += 2
                continue
            stack.append(c)
    
    return answer
