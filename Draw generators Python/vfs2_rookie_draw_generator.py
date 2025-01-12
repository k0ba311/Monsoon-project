import random


def generate_draws():
    bb_figures = ['BB-A', 'BB-B', 'BB-C', 'BB-D', 'BB-E', 'BB-F', 'BB-G', 'BB-H', 'BB-J', 'BB-K',
                  'BB-L']  # Массив с фигурами BB
    bb_blocks = ['BB-01', 'BB-02']  # Массив с блоками BB

    all_elements = bb_figures + bb_blocks  # Объединяем массивы
    draws = []  # Массив для хранения жеребьевок

    while len(draws) < 5:
        total_cost = random.choice([3, 4])  # Случайная сумма стоимости (3 или 4)
        draw = []
        current_cost = 0
        used_elements = set()  # Для отслеживания уже использованных элементов

        while current_cost < total_cost and len(draw) < len(all_elements):
            # Выбираем случайный элемент
            element = random.choice(all_elements)

            # Определяем стоимость элемента
            cost = 1 if element in bb_figures else 2

            # Проверяем, можем ли добавить элемент в жеребьевку
            if element not in used_elements and current_cost + cost <= total_cost:
                draw.append(element)
                used_elements.add(element)
                current_cost += cost

        # Проверяем, достигли ли мы нужной суммы стоимости
        if len([el for el in draw if el in bb_figures]) <= 3:
            draws.append(draw)

    return draws


results = generate_draws()
for draw in results:
    print('; '.join(draw))
