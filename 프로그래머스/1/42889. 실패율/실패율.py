def solution(N, stages):
    # 스테이지별 도전자 수
    challenger = [0] * (N+2)
    for stage in stages:
        challenger[stage] += 1
        
    # 스테이지별 실패자 수
    fails = { }
    total = len(stages)
    
    # 각 스테이지별 실패율 계산
    for i in range(1, N+1):
        if challenger[i] == 0:
            fails[i] = 0
        else:
            fails[i] = challenger[i] / total
            total -= challenger[i]
            
    # 내림차순 정렬하여 인덱스 반환
    answer = sorted(fails, key = lambda x : fails[x], reverse=True)
    return answer