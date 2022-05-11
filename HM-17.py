input_numbers = [int(x) for x in input("Введите числа от 1 до 999 в любом порядке, через пробел: ").split()]


def sort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return sort(less) + equal + sort(greater)  # Just use the + operator to join lists
    else:
        return array


print(sort(input_numbers))


def binary_search(array, element, left, right):
    if left > right:
        return False
    elif array[right] < element:
        return right

    middle = (right + left) // 2
    if array[middle] < element:
        if element <= array[middle + 1]:
            return middle
        else:
            return binary_search(array, element, middle + 1, right)
    else:
        return binary_search(array, element, left, middle - 1)


while True:
    try:
        element = int(input("Введите одно число от 1 до 999: "))
        if element < 0 or element > 999:
            raise Exception
        break
    except ValueError:
        print("Нужно ввести число!")
    except Exception:
        print("Неправильный диапазон!")


print("Номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен "
      " = ", binary_search(sort(input_numbers), element, 0, len(input_numbers)-1))
