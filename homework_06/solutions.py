from functools import lru_cache

def find_LIS(arr: list[int]) -> int:
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 1
    dp: list[int] = len(arr) * [1]
    for i in range(1, len(arr)):
        if arr[i - 1] < arr[i]:
            dp[i] = dp[i - 1] + 1
    return max(dp)


def pascal_triangle(n: int) -> list[list[int]]:
    @lru_cache(None)
    def worker(row, col):
        if col == 0 or row == col:
            return 1
        else:
            return worker(row - 1, col - 1) + worker(row - 1, col)
    
    dp: list[list[int]] = []
    for row in range(n):
        current_row = []
        for col in range(row + 1):
            current_row.append(worker(row, col))
        dp.append(current_row)
    return dp


def coin_change(coins: list[int], amount: int) -> int:
    """Возвращает минимальное количество монет, необходимых для формирования суммы ``amount``.

    Использует bottom-up динамическое программирование:
    dp[s] = минимальное количество монет для получения суммы s.
    """
    if amount == 0:
        return 0

    # amount + 1 безопаснее "infinity" потому что ответ не может превышать amount
    # когда существует монета 1, и для невозможных состояний она остается равной infinity.
    inf = amount + 1
    dp = [inf] * (amount + 1)
    dp[0] = 0

    for s in range(1, amount + 1):
        for coin in coins:
            if coin <= s:
                dp[s] = min(dp[s], dp[s - coin] + 1)

    return -1 if dp[amount] == inf else dp[amount]


def longest_palindrome(s: str) -> str:
    """Возвращает самую длинную палиндромную подстроку в ``s``.

    Использует расширение от каждого центра (как нечетные, так и четные центры).
    """
    if len(s) < 2:
        return s

    def expand(left: int, right: int) -> tuple[int, int]:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    best_left, best_right = 0, 0

    for i in range(len(s)):
        l1, r1 = expand(i, i)
        l2, r2 = expand(i, i + 1)

        if r1 - l1 > best_right - best_left:
            best_left, best_right = l1, r1
        if r2 - l2 > best_right - best_left:
            best_left, best_right = l2, r2

    return s[best_left : best_right + 1]



