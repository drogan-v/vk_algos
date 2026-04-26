"""Тесты для алгоритма Дейкстры"""
import pytest

from homework_07.solutions import dijkstra


class TestDijkstra:
    def test_shortest_paths_basic_graph(self):
        """Базовый граф с несколькими вариантами путей"""
        graph = {
            1: [(2, 4), (3, 1)],
            2: [(4, 1)],
            3: [(2, 2), (4, 5)],
            4: [],
        }

        assert dijkstra(graph, 1) == {
            1: 0.0,
            2: 3.0,
            3: 1.0,
            4: 4.0,
        }

    def test_disconnected_graph(self):
        """Недостижимые вершины должны иметь расстояние inf"""
        graph = {
            1: [(2, 3)],
            2: [],
            3: [(4, 1)],
            4: [],
        }

        result = dijkstra(graph, 1)
        assert result[1] == 0.0
        assert result[2] == 3.0
        assert result[3] == float("inf")
        assert result[4] == float("inf")

    def test_start_not_in_graph(self):
        """Если стартовой вершины нет в графе, возвращаем пустой словарь"""
        assert dijkstra({1: [(2, 1)], 2: []}, 5) == {}

    def test_negative_weight_raises_error(self):
        """Алгоритм Дейкстры не работает с отрицательными весами"""
        graph = {
            1: [(2, -1)],
            2: [],
        }

        with pytest.raises(ValueError):
            dijkstra(graph, 1)

    def test_zero_weights(self):
        """Нулевые веса ребер допустимы"""
        graph = {
            1: [(2, 0), (3, 2)],
            2: [(3, 0)],
            3: [],
        }

        assert dijkstra(graph, 1) == {
            1: 0.0,
            2: 0.0,
            3: 0.0,
        }