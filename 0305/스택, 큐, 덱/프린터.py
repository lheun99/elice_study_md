from collections import deque
deq = deque()


def solution(priorities, location):
    for idx, pri in enumerate(priorities):
        deq.append((pri, idx))

    answer = 0
    # true -> break했는데 런타임 에러
    while True:
        doc = deq.popleft()
        # deq and 해줘야 한 개 남았을때 처리 가능!
        if deq and (max(deq))[0] > doc[0]:
            deq.append(doc)
        else:
            answer += 1
            if doc[1] == location:
                return answer


print(solution([1, 1, 9, 1, 1, 1], 0))
