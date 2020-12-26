import time
if __name__ == '__main__':
  try:
    num = 0
    ask_numbers_in_use = int(input('Please enter how many numbers you want to use : '))
    str_of_ask_numbers_in_use = str(ask_numbers_in_use)
    time.sleep(1)
    numbers = []
    while '-' in str_of_ask_numbers_in_use:
      print('Invalid value, value cannot be negative')
      ask_numbers_in_use = int(input('Please enter how many numbers you want to use : '))
      time.sleep(1)
    while ask_numbers_in_use == 1:
      print('Invalid value please choose a value greater than 1')
      ask_numbers_in_use = int(input('Please enter how many numbers you want to use : '))
      time.sleep(1)
    while ask_numbers_in_use == 0:
      print('Invalid value, value cannot be 0')
      ask_numbers_in_use = int(input('Please enter how many numbers you want to use : '))
      time.sleep(1)
    else:
      while num < ask_numbers_in_use:
        num += 1
        number = input('Please enter number {} : '.format(num))
        numbers.append(number)
        time.sleep(1)
      operator = input('Please choose the operator you would like to apply on your selected values : ')
      time.sleep(1)
      what_i_have_to_do = operator.join(numbers)
      my_answer = eval(what_i_have_to_do)
      print('Output : {}'.format(my_answer))
  except Exception as exce:
    print('Program Crashed... because of {}'.format(str(exce)))
    print('Please check your code for more information...')
  
  
