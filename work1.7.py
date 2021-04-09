from datetime import date
gastroli = {
    'members': {
        'fredyy Mercury': {
            'role': 'singer',
            'date': date(1995, 12, 12)
        },
        'mirbek atabekov': {
            'role': 'singer',
            'date': date(1987, 1, 12)
        },
        'filip Kirkorov': {
            'role': 'singer',
            'date': date(1988, 8, 12)

        },
    },
    'concerts': {
        'london': {
            'concert_date': date(2021, 10, 12),
            'expenses': [100, 100, 100],
            'income': 10000
        },

        'Bishkek': {
            'concert_date': date(2021, 12, 12),
            'expenses': [100, 100, 110],
            'income': 10000

        },


        'Osh': {
            'concert_date': date(2021, 11, 12),
            'expenses': [100, 100, 100],
            'income': 10000
        },
    }
}

# Добавление участника

# def add_new_member(gastroli, **kwargs):
#     gastroli['members'].update(kwargs)
#     return gastroli


# print(add_new_member(gastroli, **{'Nikolai Baskov': {'role': 'gj', 'date': date(1988, 9, 11)}}))


# Удаление учаника

# def remove(gastroli, name):
#     return gastroli['members'].pop(name)


# remove(gastroli, 'filip Kirkorov')
# print(gastroli['members'])


# Добавление концерта
# def add_new_concert(gastroli, **kwargs):
#     gastroli['concerts'].update(kwargs)
#     return gastroli


# print(add_new_concert(gastroli, **{'Talas': {
#     'concert_date': date(2021, 8, 12),
#     'expenses': [100, 122, 123, ],
#     'income': 10000
# }}))


# Напишите функцию, которая высчитывает общую сумму затрат за концерт.

# Перивый вариант для одного концерта

# def func_(gastroli,**kwargs):
#     total = 0
#     for i in gastroli:
#         a = gastroli[i]['expenses']
#         total += sum(a)
#         return total
# print(func_(gastroli['concerts']))

# Второй вариант за 3 концерта
# def func_(gastroli):
#     total = 0
#     for i in gastroli:
#         total += i
#     return total

# print(func_(gastroli['concerts']['london']['expenses']))
# print(func_(gastroli['concerts']['Bishkek']['expenses']))
# print(func_(gastroli['concerts']['Osh']['expenses']))


# Напишите функцию, высчитывающую выгоду за концерт(разницу между затратами и суммой контракта)
# def calcu_expenses(*args):
#     return sum(args)


# def func(gastroli, concert_name):
#     income = gastroli['concerts'][concert_name]['income']
#     return income - calcu_expenses(*gastroli['concerts'][concert_name]['expenses'])


# print(func(gastroli, 'london'))
