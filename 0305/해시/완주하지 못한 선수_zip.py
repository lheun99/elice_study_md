def solution(participants, completion):
    participants.sort()
    completion.sort()
    for a, b in zip(participants, completion):
        if a != b:
            return a
        return participants[-1]


print(">", solution(["marina", "josipa", "nikola", "vinko",
      "filipa"], ["josipa", "filipa", "marina", "nikola"]))
