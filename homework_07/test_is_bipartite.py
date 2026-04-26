"""Тесты для проверки двудольности графа"""
from homework_07.solutions import is_bipartite


class TestIsBipartite:
    def test_empty_graph(self):
        """Пустой граф считается двудольным"""
        assert is_bipartite({}) is True

    def test_single_vertex(self):
        """Граф из одной вершины двудольный"""
        assert is_bipartite({1: []}) is True

    def test_even_cycle_is_bipartite(self):
        """Четный цикл является двудольным"""
        graph = {
            1: [2, 4],
            2: [1, 3],
            3: [2, 4],
            4: [1, 3],
        }
        assert is_bipartite(graph) is True

    def test_odd_cycle_is_not_bipartite(self):
        """Нечетный цикл не является двудольным"""
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2],
        }
        assert is_bipartite(graph) is False

    def test_disconnected_graph_all_components_bipartite(self):
        """Несвязный граф двудольный, если двудольна каждая компонента"""
        graph = {
            1: [2],
            2: [1],
            3: [4],
            4: [3],
            5: [],
        }
        assert is_bipartite(graph) is True

    def test_disconnected_graph_with_non_bipartite_component(self):
        """Если хотя бы одна компонента не двудольна, весь граф не двудолен"""
        graph = {
            1: [2],
            2: [1],
            3: [4, 5],
            4: [3, 5],
            5: [3, 4],
        }
        assert is_bipartite(graph) is False

    def test_self_loop_is_not_bipartite(self):
        """Петля делает граф недвудольным"""
        assert is_bipartite({1: [1]}) is False