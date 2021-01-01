# A Python file
if __name__ == '___main__':
  try:
    def func1(noranli, *apps, **pasas):
      print('Remeber that you can take as many args and as many kwargs as you want but normal arguement will not support and changes automatically accordingly u need to do changes manually')
      print('I am a normal argument', noranli)
      print('I am an optional argument and can be passed in any way inside this function but when i take this argument i turn the argument in a tuple', type(apps))
      for i in apps:
        print(i)
      for pie, pro in pasas:
        print(pie, pro)
  except Exception as exe:
    print(f'Program crashed because of {str(exe)}')
