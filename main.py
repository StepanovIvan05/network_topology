from enum import Enum
from typing import List, Tuple


class ConnectionType(Enum):
    TIRE = 1
    RING = 2
    STAR = 3


def is_full_connected(v: int, r: int, links: List[Tuple[int, int]]) -> bool:
    # Реализация функции проверки полной связности графа

    for i in range(1, v):
        for j in range(i+1, v+1):
            if (i, j) not in links and (j, i) not in links:
                return False
    return True


def connection_type(v: int, r: int, links: List[Tuple[int, int]]) -> int:
    # Реализация функции определения типа топологии сети
    # Проверка наличия связей для определения типа топологии сети
    counts = {}
    one = 0
    two = 0
    for (i, j) in links:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
        if j in counts:
            counts[j] += 1
        else:
            counts[j] = 1

    for key, count in counts.items():
        if count == 1:
            one += 1
        if count == 2:
            two += 1

    is_tire = (one == 2 and two == v-2)
    is_ring = (two == v)
    is_star = (one == v-1)

    if is_tire:
        return ConnectionType.TIRE.value
    elif is_ring:
        return ConnectionType.RING.value
    elif is_star:
        return ConnectionType.STAR.value
    else:
        print("Данная сеть не относится ни к одной типологии")
        return False


while True:
    graph_links = []
    try:
        s = input("Введите число вершин и ребер через пробел(exit для выхода): ")
        if s == "exit":
            break
        vertices, edges = map(int, s.split())
        if vertices <= 4 or edges <= 3:
            int("")
        print("Введите ребра без повторений")
        for index in range(edges):
            i, j = map(int, input().split())
            if (i, j) in graph_links or (j, i) in graph_links or i > vertices or i < 1 or j > vertices or j < 1:
                int("")
            graph_links.append((i, j))
        while True:
            choice = input("Меню:\n"
                           "1. Узнать полносвязная ли сеть\n"
                           "2. Узнать тип связи\n"
                           "3. Выйти\n"
                           "Выберите(1-3): ")
            if choice == "1":
                if is_full_connected(vertices, edges, graph_links):
                    print("Сеть полносвязная ")
                else:
                    print("Сеть неполносвязная")
            elif choice == "2":
                network_type = connection_type(vertices, edges, graph_links)
                if network_type:
                    print(f"Тип сети: {ConnectionType(network_type).name}")
            elif choice == "3":
                break
            else:
                print("Некорректный выбор")
    except:
        print("Некорректные данные")
