from math import ceil

#[95, 90, 99, 99, 80, 99]
#[1, 1, 1, 1, 1, 1]


def solution(progresses, speeds):
    duration = []  # *각 작업의 배포까지 걸리는 기간
    for process, speed in zip(progresses, speeds):
        duration.append(ceil((100 - process)/speed))
        # [5, 10, 1, 1, 20, 1]

    releaseCnt = 1  # 5
    answer = []
    for idx in range(len(duration)):
        # 5 10 (1):10 (1):10 20
        # (1):20 -> IndexError

        try:
            # *앞에 있는 기능 배포 기간 < 뒤에 있는 기능 배포 기간
            if duration[idx] < duration[idx+1]:
                answer.append(releaseCnt)  # *: 앞에 있는 기능(들)을 배포한다
                releaseCnt = 1  # *releaseCnt를 1로 바꿔놓는다

            # 5 < 10 -> 5 (releaseCnt = 1 : answer = [1]) 5
            # 10 < 20 -> (releaseCnt = 3 : answer = [1, 3]) 10 1 1

            # *앞에 있는 기능 배포 기간 >= 뒤에 있는 기능 배포 기간
            elif duration[idx] >= duration[idx+1]:
                # *: 뒤에 있는 기능 배포 기간은 비교에 필요없어지므로,
                duration[idx+1] = duration[idx]
                # *: 더 큰 앞에 있는 기능 배포 기간과 바꾼다
                # *(뒤에 있는 기능들과의 비교를 위해서)

                releaseCnt += 1  # *더 작은 수였던 뒤에 있는 기능은 앞의 있는 기능 배포 기간과 같이
                # *배포가 가능해지므로 releaseCnt를 +1 해준다

            # 10 > 1 -> releaseCnt = 2
            # 10 > 1 -> releaseCnt = 3
            # 20 > 1 -> releaseCnt = 2

        # *마지막 인덱스는 항상 IndexError가 발생한다
        except IndexError:
            answer.append(releaseCnt)  # *이전까지의 구해진 releaseCnt를 배포
            # (1):20  -> (releaseCnt = 2 : answer = [1, 3, 2]) 20 1

    return answer
    #[1, 3, 2]


print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
