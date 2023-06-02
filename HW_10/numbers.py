import random

num_multi = random.randint(1, 10)

def number():
    return random.randint(1, 50)

def number_multi():
    return random.randint(1, 10)

def sum_num(num_one: int, num_two: int) -> int:
    return int(num_one + num_two)

def multi_num(num_one: int, num_two: int) -> int:
    return int(num_one * num_two)

def diff_num(num_one: int, num_two: int) -> int:
    return int(num_one - num_two)

def division_num(num_one: int, num_two: int) -> int:
    return int(num_one // num_two)


# Действия прописать в контроллере, подсоединить туда numbers. Сначала view с примером и ответом
# всместе с numbers  потом model по занесению очков.