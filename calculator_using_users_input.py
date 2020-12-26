import time
if __name__ == '__main__':
  try:
    users_input = input('Pls enter your expression but in python\'s format : ')
    answer = eval(users_input)
  except Exception as exception:
    print('Program crashed... because of',str(exception))
    print('Please check your code for more information')
