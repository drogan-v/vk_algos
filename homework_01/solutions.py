def reverse_array(arr: list[int], left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def solution_01(arr: list[int], k: int) -> list[int]:
    # Решение работает за O(n), потому что мы 3 раза вызываем
    # функцию, которая сама по себе просто проходится по массиву 1 раз,
    # причем делает примерно n/2 итераций. то есть всего ~1.5n итераций.
    # O(1.5n) = O(n)
    #
    # Дополнительная память не используется, потому что мы делаем in-place
    # изменения
    if len(arr) == 0:
        return []

    n = len(arr)
    k %= n

    reverse_array(arr, 0, n - 1)
    reverse_array(arr, 0, k - 1)
    reverse_array(arr, k, n - 1)

    return arr


def solution_02(arr_1: list[int], arr_2: list[int]) -> list[int]:
    new_arr = []
    i, j = 0, 0
    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] < arr_2[j]:
            new_arr.append(arr_1[i])
            i += 1
        else:
            new_arr.append(arr_2[j])
            j += 1
    new_arr.extend(arr_1[i:])
    new_arr.extend(arr_2[j:])
    return new_arr


def solution_03(arr1: list[int], arr2: list[int]) -> list[int]:
    # Используем три указателя и пишем в arr1 с конца, тем самым
    # не затираем еще не обработанные числа
    pointer1 = len(arr1) - len(arr2) - 1
    pointer2 = len(arr2) - 1
    pointer3 = len(arr1) - 1
    while pointer2 >= 0:
        if pointer1 >= 0 and arr1[pointer1] > arr2[pointer2]:
            arr1[pointer3] = arr1[pointer1]
            pointer1 -= 1
        else:
            arr1[pointer3] = arr2[pointer2]
            pointer2 -= 1
        pointer3 -= 1
    return arr1


def solution_04(arr: list[int]):
    # время линейное, потому что в худшем случае код n раз пройдет тело цикла
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] == 1:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
        else:
            left += 1
    return arr


def solution_05(nums: list[int]):
    # Границы чисел обеспечиваются указателем mid
    # low - граница хвоста нулей, mid - текущий индекс обхода
    # high = граница головы двоек
    low = 0
    mid = 0
    high = len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        elif nums[mid] == 2:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


def solution_06(nums: list[int]) -> list[int]:
    # Решение стабильно только для четных чисел, потому что любые два
    # четных числа не перепыгивают при итерировании
    even_index = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[i], nums[even_index] = nums[even_index], nums[i]
            even_index += 1
    return nums


def solution_07(nums: list[int]) -> list[int]:
    # Решение делает n итераций. Поэтому сложность O(n)
    # Решение стабильное, потому что все ненулевые элементы 
    # переносятся вперед в порядке итерирования. Каждый ненулевой меняется
    # местами с элементом на позиции ins, который либо равен ему самому, 
    # либо расположен левее и уже не ноль
    ins = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[ins] = nums[ins], nums[i]
            ins += 1

    return nums
