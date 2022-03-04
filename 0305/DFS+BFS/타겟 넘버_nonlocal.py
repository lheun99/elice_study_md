def solution(numbers, target):
    cal = 0
    idx = 0
    answer = 0

    def dfs(idx, cal):
        nonlocal answer
        if idx == len(numbers):
            if cal == target:
                answer += 1

        else:
            dfs(idx+1, cal+numbers[idx])
            dfs(idx+1, cal-numbers[idx])

    dfs(idx, cal)
    return answer


print(solution([4, 1, 2, 1], 4))
