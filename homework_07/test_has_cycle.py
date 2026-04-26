"""Тесты для поиска цикла в графе"""
from homework_07.solutions import has_cycle


class TestHasCycle:
    def test_empty_graph(self):
        """Пустой граф не содержит цикл"""
        assert has_cycle({}) is False

    def test_single_vertex_without_edges(self):
        """Одна вершина без ребер не содержит цикл"""
        assert has_cycle({1: []}) is False

    def test_chain_without_cycle(self):
        """Линейный граф без цикла"""
        graph = {
            1: [2],
            2: [1, 3],
            3: [2, 4],
            4: [3],
        }
        assert has_cycle(graph) is False

    def test_triangle_cycle(self):
        """Простейший цикл из трех вершин"""
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2],
        }
        assert has_cycle(graph) is True

    def test_cycle_in_disconnected_component(self):
        """Цикл может быть в отдельной компоненте связности"""
        graph = {
            1: [2],
            2: [1],
            3: [4, 5],
            4: [3, 5],
            5: [3, 4],
        }
        assert has_cycle(graph) is True

    def test_self_loop(self):
        """Петля в вершине считается циклом"""
        assert has_cycle({1: [1]}) is True

    def test_multiple_components_without_cycle(self):
        """Несколько компонент без циклов"""
        graph = {
            1: [2],
            2: [1],
            3: [],
            4: [5],
            5: [4],
        }
        assert has_cycle(graph) is False