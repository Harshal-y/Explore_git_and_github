try:
  def func1(noranli, *apps, **pasas):
    '''I am Harshal and i have made this code to let you know that i am a python programmer and can help u if u want to learn python'''
    print('Remeber that you can take as many args and as many kwargs as you want but normal arguement will not support and changes automatically accordingly u need to do changes manually')
    print('I am a normal argument', noranli)
    print('I am an optional argument and can be passed in any way inside this function but when i take this argument i turn the argument in a tuple : ', str(type(apps)))
    for i in apps:
      print(i)
    for pie, pro in pasas.items():
      print(pie, pro)
    return pie, pro
except Exception as exe:
  print(f'Program crashed because of {str(exe)}')
if __name__ == '__main__':
  print(func1.__doc__)
if __name__ == '__main__':
    a = {'k', 'p', 'g'}
    pi, li, ji = a
    apka = {'pie':'pro', 'rope':'joke'}
    print(func1(pi, *a, **apka))
