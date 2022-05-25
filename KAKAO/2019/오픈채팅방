nicname = {}
def menu(order, user):
    if order == 'Enter':
        return f"{nicname[user]}님이 들어왔습니다."
    elif order == 'Leave':
        return f"{nicname[user]}님이 나갔습니다."

def solution(record):
    answer = []
    l= [r.split() for r in record]
    
    # 전체 확인해서 id, nicname 부터 확정
    for i in range(len(l)):
        if l[i][0] != 'Leave':
            nicname[l[i][1]] = l[i][2]
            
    for i in range(len(l)):
        if l[i][0] != 'Change':
            answer.append(menu(l[i][0],l[i][1]))
    
    return answer
