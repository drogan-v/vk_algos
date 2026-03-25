def binary_search_square_root(x: int) -> int:
    # Алгоритм работает за O(log(x)), потому что использует бинарный поиск
    # Граница поиска определяется тем, что квадрат корня не может быть больше x // 2 для x >= 2
    if x < 2:
        return x

    left, right = 1, x // 2
    while left <= right:
        mid = left + (right - left) // 2
        if mid ** 2  == x:
            return mid
        elif mid ** 2 < x:
            left = mid + 1
        else:
            right = mid - 1

    return right


def copy_time(n: int, x: int, y: int) -> int:
    # Условие достаточности времени проверяется напрямую:
    # Мы просто делим все время на x и y, чтобы узнать, 
    # сколько копий может быть сделано двумя ксероксами за время mid
    l = 0
    r = (n - 1) * max(x, y)
    while l + 1 < r:
        mid = (l + r) // 2
        if mid // x + mid // y < n - 1:
            l = mid
        else:
            r = mid
    return r + min(x, y)


def feed_animals(animals: list[int], food: list[int]) -> int:
    # Данная стратегия дает максимальное количество накормленных животных, 
    # потому что мы всегда пытаемся накормить самого маленького 
    # самым маленьким доступным кормом. Нет доступного корма, для
    # самого маленького, нет и для более крупной скотины.
    if len(animals) == 0 or len(food) == 0:
        return 0
    animals.sort()
    food.sort()
    count = 0
    for f in food:
        if f >= animals[count]:
            count += 1
        if count == len(animals):
            break
    return count


def extra_letter(a: str, b: str) -> str:
    # Решение работает за O(n), потому что мы проходим по обоим строкам один раз,
    # а операции со словарем выполняются за O(1).
    # Мы просто считаем количество каждого символа в строке a,
    # а затем, если увидели его в строке b, выбрасываем один раз этот
    # символ. Если в строке b есть символ, которого нет в a, мы его
    # не находим в хеше и сразу возвращаем.

    hash_map_a: dict[str, int] = {}
    for i in range(len(a)):
        hash_map_a.setdefault(a[i], 0)
        hash_map_a[a[i]] += 1
    
    for i in range(len(b)):
        if b[i] in hash_map_a:
            hash_map_a[b[i]] -= 1
            if hash_map_a[b[i]] == 0:
                hash_map_a.pop(b[i])
                continue
            continue
        return b[i]
    return ''


def two_sum(data: list[int], target: int) -> list[int]:
    # Мы взяли число и вычитаем его из target.
    # Если результат уже есть в хеше, значит мы можем суммой двух
    # чисел из списка получить target. Если не можем, добавляем
    # число в хеш и идем по списку дальше.
    cache: dict[int, int] = {}
    for i in range(len(data)):
        diff = target - data[i]
        if diff in cache:
            return [i, cache[diff]]
        cache[data[i]] = i
        
    return []


def shell_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    gap = len(arr) // 2
    while gap > 0:
        for current_pos in range(gap, n):
            m_gap = current_pos
            while m_gap >= gap and arr[m_gap] < arr[m_gap - gap]:
                arr[m_gap], arr[m_gap - gap] = arr[m_gap - gap], arr[m_gap]
                m_gap -= gap
        gap //= 2
    return arr


def anagramms(words: list[str]) -> list[list[str]]:
    anagramms_map: dict[str, list[str]] = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagramms_map.setdefault(sorted_word, [])
        anagramms_map[sorted_word].append(word)
    return list(anagramms_map.values())
