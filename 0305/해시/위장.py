import collections


def solution(clothes):
    typeList = []
    for cloth, type in clothes:
        typeList += [type]
    count = collections.Counter(typeList)
    answer = 1
    for cnt in count.values():
        answer *= cnt+1

    return answer-1


print(solution([["yellowhat", "headgear"], [
      "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
