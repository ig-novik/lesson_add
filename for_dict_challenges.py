
def max_repeat(list1):
  # функция возврвщает наиболее часто встречающееся в списке значение
  return max(list1, key=list1.count)

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
from collections import Counter

students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
list_name=[]

for std in students:
  list_name.append(std['first_name'])
cnt = Counter(list_name)  # список(в виде словаря) всех имён с указанием количества их повторов

for nm in cnt:
  print(f'{nm} : {cnt[nm]}')

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
list_name=[]

for std in students:
  list_name.append(std['first_name'])
print(f'Самое частое имя среди учеников: {max_repeat(list_name)}')

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]


cl=0
for class_student in school_students:
  list_name = []
  for students in class_student:
    list_name.append(students['first_name'])
  cl += 1
  print(f'Самое частое имя в классе {cl}: {max_repeat(list_name)}')


# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
for class_ in school:
  girls = 0
  boys = 0
  for std in class_['students']:
    if is_male[std['first_name']]:
      boys += 1
    else:
      girls +=1
  print(f'В классе {class_["class"]} {girls} девочки и {boys} мальчика')
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

sex = []

for class_ in school:
  sex_class = {}
  sex_class['class'] = class_['class']
  sex_class['boys'] = 0
  sex_class['girls'] = 0
  for std in class_['students']:
    if is_male[std['first_name']]:
      sex_class['boys'] += 1
    else:
      sex_class['girls'] +=1
  sex.append(sex_class)

if sex[0]['boys'] > sex[1]['boys']:
  max_boys_class = sex[0]['class']
else:
  max_boys_class = sex[1]['class']
if sex[0]['girls'] > sex[1]['girls']:
  max_girls_class = sex[0]['class']
else:
  max_girls_class = sex[1]['class']
print(f'Больше всего мальчиков в классе {max_boys_class}')
print(f'Больше всего девочек в классе {max_girls_class}')
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a