# Задача 26: Напишите программу, которая на вход принимает 
# два числа A и B, и возводит число А в целую степень B с 
# помощью рекурсии.
# Example:
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def number_degree(number: int, degree: int):
  if degree == 0:
    return 1
  if degree == 1:
    return number
  else:
    return number * number_degree(number, degree - 1)

number = int(input('Eneter a number: '))
degree = int(input('Enter a degree of the number: '))
print(f'The result of calculation - number {number} in degree {degree} is {number_degree(number, degree)}')
