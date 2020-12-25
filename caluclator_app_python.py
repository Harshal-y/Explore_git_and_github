import time
if __name__ == '__main__':
  try:
    num = 0
    ask_numbers_in_use = int(input('Please enter the first number : '))
    time.sleep(1)
    while num < ask_numbers_in_use:
      num += 1
      number = []
      number = int(input('Please enter number {} : '.format(num)))
      numbers.append(number)
      time.sleep(1)
      operator = input('Please choose the operator you would like to apply on your selected values : ')
      time.sleep(1)
  except:
    print('Program Crashed...')
  
  
