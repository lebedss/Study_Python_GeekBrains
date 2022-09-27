# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input('Введите порядковый номер дня недели чтобы узнать является ли этот день выходным: '))
if day == 6 or day == 7:
    print('Да - это выходной!')
elif day in [1, 2, 3, 4, 5]:
    print('Нет - это рабочий день')
else:
    print('Ошибка ввода данных - попробуйте ещё раз')
