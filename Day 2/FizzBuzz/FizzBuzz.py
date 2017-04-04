def fizz_buzz(argument):
  if argument % 5 == 0 and argument%3 == 0:
    return 'FizzBuzz'
  elif argument % 5 != 0 and argument%3 != 0:
    return argument
  elif argument % 3 == 0:
    return 'Fizz'
  elif argument % 5 == 0:
    return 'Buzz'

__author__ = 'Justin M'
