from collections import deque


def solution(prices):
    deq = deque(prices)
    answer = []

    while deq:
        price = deq.popleft()
        sec = 0

        for d in deq:
            sec += 1
            
            if price > d:
                break

        answer.append(sec)
    return answer


print(solution([1, 2, 3, 2, 3]))
