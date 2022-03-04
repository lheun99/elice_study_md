def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        print(f"phone number > {phone_number}")
        for number in phone_number:
            print(f"number > {number}")
            temp += number
            print(f"temp > {temp}")
            if temp in hash_map and temp != phone_number:
                answer = False
                return answer
    return answer


print(solution(["12", "123", "1235", "567", "88"]))
