def solution(numbers):
    fanswer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            fanswer.append(numbers[i]+numbers[j])
    
    answer = list(set(fanswer))
    answer.sort()
    return answer