"""Тесты для проверки, является ли граф деревом"""
from homework_07.solutions import is_tree


class TestIsTree:
    def test_single_vertex(self):
        """Одна вершина без ребер является деревом"""
        assert is_tree({1: []}, 1) is True

    def test_chain_graph(self):
        """Связный граф без циклов является деревом"""
        graph = {
            1: [2],
            2: [1, 3],
            3: [2, 4],
            4: [3],
        }
        assert is_tree(graph, 1) is True

    def test_triangle_not_tree(self):
        """Граф с циклом не является деревом"""
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2],
        }
        assert is_tree(graph, 1) is False

    def test_disconnected_graph_not_tree(self):
        """Несвязный граф не является деревом"""
        graph = {
            1: [2],
            2: [1],
            3: [4],
            4: [3],
        }
        assert is_tree(graph, 1) is False

    def test_start_not_in_graph(self):
        """Если стартовой вершины нет в графе, это не дерево"""
        assert is_tree({1: []}, 2) is False

    def test_cycle_in_larger_graph(self):
        """Более длинный цикл тоже должен обнаруживаться"""
        graph = {
            1: [2],
            2: [1, 3],
            3: [2, 4],
            4: [3, 1],
        }
        assert is_tree(graph, 1) is False