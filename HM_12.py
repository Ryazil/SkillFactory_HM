per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input('money = ')
deposit = list(dict.values(per_cent))
for i in range(len(deposit)):
    deposit[i] *= int(money)/100
print('deposit = ', deposit)
print('Максимальная сумма, которую вы можете заработать = ', max(deposit))
