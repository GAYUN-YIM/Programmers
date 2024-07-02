def solution(answers):
    # 패턴 분석
    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    
    # 점수 저장 리스트
    scores = [0] * 3
    
    # 일치 여부 확인
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i%len(pattern)]:
                scores[j]+=1
                
    max_score = max(scores)
    
    # 수포자 번호 찾기
    highest = []
    for k, score in enumerate(scores):
        if score == max_score:
            highest.append(k+1)
    return highest