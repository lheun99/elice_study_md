from heapq import *


def solution(scoville, K):
    heapify(scoville)
    mixCnt = 0
    while scoville[0] < K and len(scoville) > 1:
        first = heappop(scoville)
        second = heappop(scoville)
        sc = first + (second*2)
        heappush(scoville, sc)
        mixCnt += 1

    if scoville[0] > K:
        return mixCnt
    else:
        return -1


scoville = [1, 1]
print(solution(scoville, 7))
