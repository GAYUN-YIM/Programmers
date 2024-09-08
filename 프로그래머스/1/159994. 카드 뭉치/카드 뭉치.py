def solution(cards1, cards2, goal):
    i, j = 0, 0  # 카드 더미의 인덱스
    for word in goal:
        if i < len(cards1) and cards1[i] == word:
            i += 1
        elif j < len(cards2) and cards2[j] == word:
            j += 1
        else:
            return "No"
    return "Yes"
