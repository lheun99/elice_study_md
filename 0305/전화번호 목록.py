def solution(phone_book):
    phone_book.sort()
    try:
        for idx in range(len(phone_book)):
            if phone_book[idx+1].startswith(phone_book[idx]):
                return False
        return True
    except IndexError:
        return True


print(solution(["123", "456", "789"]))
