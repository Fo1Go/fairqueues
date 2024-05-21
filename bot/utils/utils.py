from random import choice


def create_new_code(length: int) -> str:
    symbols = '1234567890'
    code = ''
    for _ in range(length):
        code += choice(symbols)

    return code


def check_username_or_id(data: str) -> int | str:
    if data.isnumeric():
        return int(data)
    return data
