import random


def generate_draws():
    figures = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q']  # Массив с фигурами
    blocks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
              '20', '21', '22']  # Массив с блоками

    all_elements = figures + blocks  # Объединяем массивы
    draws = []  # Массив для хранения жеребьевок

    while len(draws) < 10:
        total_cost = random.choice([5, 6])  # Случайная сумма стоимости (5 или 6)
        draw = []
        current_cost = 0
        used_elements = set()  # Для отслеживания уже использованных элементов

        while current_cost < total_cost and len(draw) < len(all_elements):
            # Выбираем случайный элемент
            element = random.choice(all_elements)

            # Определяем стоимость элемента
            cost = 1 if element in figures else 2

            # Проверяем, можем ли добавить элемент в жеребьевку
            if element not in used_elements and current_cost + cost <= total_cost:
                draw.append(element)
                used_elements.add(element)
                current_cost += cost

        # Проверяем, достигли ли мы нужной суммы стоимости
        if len([el for el in draw if el in figures]) <= 3:
            draws.append(draw)
            # Удаляем использованные элементы из общего списка
            all_elements = [el for el in all_elements if el not in used_elements]

    return draws


results = generate_draws()
a = '; '.join(results[0]) + "\n" + '; '.join(results[1]) + "\n" + '; '.join(results[2]) + "\n" + '; '.join(results[3]) + "\n" + '; '.join(results[4]) + "\n" + '; '.join(results[5]) + "\n" + '; '.join(results[6]) + "\n" + '; '.join(results[7]) + "\n" + '; '.join(results[8]) + "\n" + '; '.join(results[9])
print(a)
