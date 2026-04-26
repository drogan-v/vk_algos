"""Тесты для проверки баланса скобок через префиксные суммы"""
from homework_08.solutions import is_valid_parentheses_prefix


class TestIsValidParenthesesPrefix:
	def test_empty_string(self):
		"""Пустая строка считается корректной"""
		assert is_valid_parentheses_prefix("") is True

	def test_simple_valid(self):
		"""Простая корректная последовательность"""
		assert is_valid_parentheses_prefix("()") is True

	def test_nested_valid(self):
		"""Вложенные скобки корректны"""
		assert is_valid_parentheses_prefix("(()())") is True

	def test_invalid_prefix(self):
		"""Если в префиксе закрывающих больше, чем открывающих, последовательность некорректна"""
		assert is_valid_parentheses_prefix(")(()") is False

	def test_unclosed_open_bracket(self):
		"""Незакрытая открывающая скобка делает строку некорректной"""
		assert is_valid_parentheses_prefix("(()") is False

	def test_only_closing(self):
		"""Строка только из закрывающих скобок некорректна"""
		assert is_valid_parentheses_prefix(")))") is False

	def test_invalid_characters(self):
		"""Если есть посторонние символы, возвращается False"""
		assert is_valid_parentheses_prefix("()a()") is False