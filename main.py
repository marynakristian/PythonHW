# # /!1
# def test(age: int, name: str) -> str:
#     return f"Hello, {name}, your age is {age}"

# text = test(age=45, name="John")
# print(text)

# # /!2
# def test(l: list):
#     l.append
#     return l

# tu = [1, 2, 3]

# new_tu = test(tu)
# print(new_tu)
# print(tu)

# # /!3
# def pow(num: int, exponent: int = 2) -> int:
#     return num ** exponent

# first, second, *li = [1, 2, 3, 4, 5, 6, 7,]
# print(first)
# print(second)
# print(li)

# # /!3.0
# def pow(num: int, exponent: int = 2) -> int:
#     return num ** exponent

# d = {"num": 4, "exponent": 5}
# print(pow(**d))

# # /!4
# l = [1,2,3,4]
# k = ['5', '6', '7', '8']

# zipped_data = list(zip(l, k))
# print(zipped_data)

# /!5
# def qiucksort(numbers: list) -> list:
#     if not numbers:
#         return[]
#     if len(numbers) == 1:
#         return numbers
#     basic_element = numbers[0]
#     left = [num for num in numbers[1:] if num < basic_element]
#     right = [num for num in numbers[1:] if num >= basic_element]
#     return qiucksort(left) + [basic_element] + qiucksort(right)

# li = [4, 6, 18, 2, 8, 5, 1, 0, 10, 3, 63]
# result = qiucksort(li)
# print(result)

# # /!6
# def calculate_sum(x: int, y: int) ->int:
#     return x + y

# result = calculate_sum(23, 94)
# print(result)

# /!7
# def calculate_average(li: list[int]) ->float:
#     return sum(li) / len(li)

# print(calculate_average([1, 25, 7]))
# print(calculate_average([34, 872, 9392]))

# # /!8
# def factorial(n: int) -> int:
#     result = 1
#     for i in range(1, n +1):
#         result *= i
#         return result
    
#     print(factorial(5))
#     print(factorial(15))

# # /!9
# def filter_even(li: list[int]) -> list[int]:
#     return list(filter(lambda x: x % 2 == 0, li))

# print(filter_even([1, 2, 3, 4, 5, 6]))
# print(filter_even([12, 23, 34, 45, 56, 67]))

# # /!10
# def is_palindrome(s: str) -> bool:
#     return s == s[::-1]

# print(is_palindrome("abba"))
# print(is_palindrome("abbasdasdas"))

# # /!11
# def modify_list(li: list[int]) -> list[int]:
#     return list(map(lambda x: x ** 2, li))

# print(modify_list([1, 2, 4, 7]))
# print(modify_list([21, 12, 41, 74]))

# # /! 12
# def finbonaci(n: int) -> int:
#     a = 1
#     b = 1
#     if n == 1:
#         return [1]
#     if n == 2:
#         return [1, 1]
#     result = [1, 1]
#     for _ in range(2, n):
#         a, b = b, a + b
#         result.append(b)
#     return result

# print(finbonaci(10))

# # /!13
# def fib_recursive(n: int) -> list:
#     if n == 1:
#         return [1]
#     elif n == 2:
#         return[1, 1]
#     else:
#         fib_list = fib_recursive(n - 1)
#         fib_list.append(fib_list[-1] +fib_list[-2])
#         return fib_list
    
# print(fib_recursive(10))

# /!14
# with open("main.txt", "r") as file:
#     content = file.read()
# file.close()


# /! 15
