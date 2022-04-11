n_o_t = input("Введите количество билетов = ")  # number of tickets
N = int(n_o_t)
age = list(range(1, N + 1))
cost = list(range(1, N + 1))
# print(type(age))
for i in range(0, N):
    age[i] = input("Введите возраст посетителя = ")
    if int(age[i]) < 18:
        cost[i] = 0
    elif 18 <= int(age[i]) < 25:
        cost[i] = 990
    elif int(age[i]) >= 25:
        cost[i] = 1390

if N > 3:
    total_cost = float(sum(cost)) * 0.9
else:
    total_cost = int(sum(cost))

print("Итоговая цена =", total_cost)
