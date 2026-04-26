def max_subarray_sum(arr: list[int], k: int) -> int:
	"""
	Найти максимальную сумму среди всех подмассивов длины k.

	Используется массив префиксных сумм:
	sum(arr[l:r]) = prefix[r] - prefix[l].
	"""
	if k <= 0 or k > len(arr):
		raise ValueError("k должно быть в диапазоне от 1 до длины массива")

	prefix: list[int] = [0]
	for value in arr:
		prefix.append(prefix[-1] + value)

	best = prefix[k] - prefix[0]

	for right in range(k + 1, len(prefix)):
		current = prefix[right] - prefix[right - k]
		if current > best:
			best = current

	return best


def subarray_sum_equals_k(nums: list[int], k: int) -> int:
	"""
	Посчитать количество непрерывных подмассивов с суммой k.

	Используется префиксная сумма и словарь частот уже встреченных
	префиксных сумм.
	"""
	prefix_sum = 0
	count = 0
	prefix_count: dict[int, int] = {0: 1}

	for num in nums:
		prefix_sum += num
		count += prefix_count.get(prefix_sum - k, 0)
		prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

	return count


def max_equal_zero_one_subarray_length(nums: list[int]) -> int:
	"""
	Найти максимальную длину подмассива, где количество 0 и 1 одинаково.

	Идея: заменить 0 на -1, тогда задача сводится к поиску
	самого длинного подмассива с суммой 0.
	"""
	prefix_sum = 0
	best = 0
	first_index: dict[int, int] = {0: -1}

	for i, value in enumerate(nums):
		if value == 0:
			prefix_sum -= 1
		else:
			prefix_sum += 1

		if prefix_sum in first_index:
			length = i - first_index[prefix_sum]
			if length > best:
				best = length
		else:
			first_index[prefix_sum] = i

	return best


def find_rotation_index(nums: list[int]) -> int:
	"""
	Найти индекс минимального элемента в отсортированном повернутом массиве.

	Если массив не повернут, вернется 0.
	Для пустого массива выбрасывается ValueError.
	"""
	if not nums:
		raise ValueError("массив не должен быть пустым")

	left, right = 0, len(nums) - 1

	while left < right:
		mid = (left + right) // 2

		if nums[mid] > nums[right]:
			left = mid + 1
		else:
			right = mid

	return left


def is_valid_parentheses_prefix(s: str) -> bool:
	"""
	Проверить корректность скобочной последовательности из '(' и ')'.

	Префиксная сумма (баланс):
	- '(' увеличивает баланс на 1;
	- ')' уменьшает баланс на 1.
	"""
	balance = 0

	for ch in s:
		if ch == '(':
			balance += 1
		elif ch == ')':
			balance -= 1
		else:
			return False

		if balance < 0:
			return False

	return balance == 0


