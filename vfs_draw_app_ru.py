import sys
import random
import signal

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import *


def generate_draws_4way():
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


def generate_draws_inter_bb():
    bb_figures = ['BB-A', 'BB-B', 'BB-C', 'BB-D', 'BB-E', 'BB-F', 'BB-G', 'BB-H', 'BB-J', 'BB-K',
                  'BB-L']  # Массив с фигурами BB
    bb_blocks = ['BB-01', 'BB-02']  # Массив с блоками BB

    all_elements = bb_figures + bb_blocks  # Объединяем массивы
    draws = []  # Массив для хранения жеребьевок

    while len(draws) < 2:
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
            # Удаляем использованные элементы из общего списка
            all_elements = [el for el in all_elements if el not in used_elements]

    return draws


def generate_draws_inter_hu():
    hu_figures = ['HU-A', 'HU-B', 'HU-C', 'HU-D', 'HU-E', 'HU-F', 'HU-G', 'HU-H', 'HU-J']  # Массив с фигурами HU
    hu_blocks = ['HU-01', 'HU-02', 'HU-03', 'HU-04']  # Массив с блоками HU

    all_elements = hu_figures + hu_blocks  # Объединяем массивы
    draws = []  # Массив для хранения жеребьевок

    while len(draws) < 3:
        total_cost = random.choice([3, 4])  # Случайная сумма стоимости (3 или 4)
        draw = []
        current_cost = 0
        used_elements = set()  # Для отслеживания уже использованных элементов

        while current_cost < total_cost and len(draw) < len(all_elements):
            # Выбираем случайный элемент
            element = random.choice(all_elements)

            # Определяем стоимость элемента
            cost = 1 if (element in hu_figures) else 2

            # Проверяем, можем ли добавить элемент в жеребьевку
            if element not in used_elements and current_cost + cost <= total_cost:
                draw.append(element)
                used_elements.add(element)
                current_cost += cost

        # Проверяем, достигли ли мы нужной суммы стоимости
        if len([el for el in draw if el in hu_figures]) <= 3:
            draws.append(draw)
            # Удаляем использованные элементы из общего списка
            all_elements = [el for el in all_elements if el not in used_elements]

    return draws


def generate_draws_aclass_bb():
    bb_figures = ['BB-A', 'BB-B', 'BB-C', 'BB-D', 'BB-E', 'BB-F', 'BB-G', 'BB-H', 'BB-J', 'BB-K', 'BB-L']  # Массив с фигурами BB
    bb_blocks = ['BB-01', 'BB-02']  # Массив с блоками BB

    all_elements = bb_figures + bb_blocks  # Объединяем массивы
    draws = []  # Массив для хранения жеребьевок

    while len(draws) < 2:
        total_cost = random.choice([5, 6])  # Случайная сумма стоимости (5 или 6)
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
        if current_cost == total_cost:
            draws.append(draw)
            # Удаляем использованные элементы из общего списка
            all_elements = [el for el in all_elements if el not in used_elements]

    return draws


def generate_draws_aclass_hu():
    hu_figures = ['HU-A', 'HU-B', 'HU-C', 'HU-D', 'HU-E', 'HU-F', 'HU-G', 'HU-H', 'HU-J']  # Массив с фигурами HU
    hu_blocks = ['HU-01', 'HU-02', 'HU-03', 'HU-04']  # Массив с блоками HU
    hd_figures = ['HD-A', 'HD-B', 'HD-C', 'HD-E', 'HD-F', 'HD-G', 'HD-H', 'HD-J', 'HD-K']  # Массив с фигурами HD
    hd_blocks = ['HD-01', 'HD-02', 'HD-03', 'HD-04', 'HD-05']  # Массив с блоками HD

    all_elements = hu_figures + hu_blocks + hd_figures + hd_blocks  # Объединяем массивы
    draws = []  # Массив для хранения жеребьевок

    while len(draws) < 3:
        total_cost = random.choice([5, 6])  # Случайная сумма стоимости (5 или 6)
        draw = []
        current_cost = 0
        used_elements = set()  # Для отслеживания уже использованных элементов

        while current_cost < total_cost and len(draw) < len(all_elements):
            # Выбираем случайный элемент
            element = random.choice(all_elements)

            # Определяем стоимость элемента
            cost = 1 if (element in hu_figures) or (element in hd_figures) else 2

            # Проверяем, можем ли добавить элемент в жеребьевку
            if element not in used_elements and current_cost + cost <= total_cost:
                draw.append(element)
                used_elements.add(element)
                current_cost += cost

        # Проверяем, достигли ли мы нужной суммы стоимости
        if current_cost == total_cost:
            draws.append(draw)
            # Удаляем использованные элементы из общего списка
            all_elements = [el for el in all_elements if el not in used_elements]

    return draws


def generate_draws_open_bb():
    bb_figures = ['BB-A', 'BB-B', 'BB-C', 'BB-D', 'BB-E', 'BB-F', 'BB-G', 'BB-H', 'BB-J', 'BB-K', 'BB-L']  # Массив с фигурами BB
    bb_blocks = ['BB-01', 'BB-02']  # Массив с блоками BB

    all_elements = bb_figures + bb_blocks  # Объединяем массивы
    draws = []  # Массив для хранения жеребьевок

    while len(draws) < 2:
        total_cost = random.choice([5, 6])  # Случайная сумма стоимости (5 или 6)
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
        if current_cost == total_cost:
            draws.append(draw)
            # Удаляем использованные элементы из общего списка
            all_elements = [el for el in all_elements if el not in used_elements]

    return draws


def generate_draws_open_hu():
    hu_figures = ['HU-A', 'HU-B', 'HU-C', 'HU-D', 'HU-E', 'HU-F', 'HU-G', 'HU-H', 'HU-J']  # Массив с фигурами HU
    hu_blocks = ['HU-01', 'HU-02', 'HU-03', 'HU-04']  # Массив с блоками HU
    hd_figures = ['HD-A', 'HD-B', 'HD-C', 'HD-D', 'HD-E', 'HD-F', 'HD-G', 'HD-H', 'HD-J', 'HD-K']  # Массив с фигурами HD
    hd_blocks = ['HD-01', 'HD-02', 'HD-03', 'HD-04', 'HD-05', 'HD-06']  # Массив с блоками HD

    all_elements = hu_figures + hu_blocks + hd_figures + hd_blocks  # Объединяем массивы
    draws = []  # Массив для хранения жеребьевок

    while len(draws) < 4:
        total_cost = random.choice([5, 6])  # Случайная сумма стоимости (5 или 6)
        draw = []
        current_cost = 0
        used_elements = set()  # Для отслеживания уже использованных элементов

        while current_cost < total_cost and len(draw) < len(all_elements):
            # Выбираем случайный элемент
            element = random.choice(all_elements)

            # Определяем стоимость элемента
            cost = 1 if (element in hu_figures) or (element in hd_figures) else 2

            # Проверяем, можем ли добавить элемент в жеребьевку
            if element not in used_elements and current_cost + cost <= total_cost:
                draw.append(element)
                used_elements.add(element)
                current_cost += cost

        # Проверяем, достигли ли мы нужной суммы стоимости
        if current_cost == total_cost:
            draws.append(draw)
            # Удаляем использованные элементы из общего списка
            all_elements = [el for el in all_elements if el not in used_elements]

    return draws


class Main_window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Генератор жеребьевки VFS')
        self.resize(600, 400)

        label = QLabel('Выберите дисциплину:')
        self.button_1 = QPushButton('VFS 2-way')
        self.button_2 = QPushButton('VFS 4-way')

        label.setFont(QFont('Arial', 12, QFont.Bold))
        self.button_1.setFont(QFont('Arial', 10))
        self.button_2.setFont(QFont('Arial', 10))

        self.button_1.setFixedWidth(400)
        self.button_2.setFixedWidth(400)

        main_layout = QVBoxLayout()

        main_layout.addWidget(label, alignment=Qt.AlignCenter)
        main_layout.addWidget(self.button_1, alignment=Qt.AlignCenter)
        main_layout.addWidget(self.button_2, alignment=Qt.AlignCenter)

        self.setLayout(main_layout)

        self.button_1.clicked.connect(self.open_win_1)
        self.button_2.clicked.connect(self.open_win_2)

    def open_main_win(self):
        self.main_win = Main_window()
        self.main_win.show()

    def open_win_1(self):
        self.win_1 = Window_1()
        self.win_1.show()

    def open_win_2(self):
        self.win_2 = Window_2()
        self.win_2.show()


class Window_1(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Генератор жеребьевки VFS 2-way')
        self.resize(450, 400)

        label_win_1 = QLabel('Выберите класс:')
        self.button_win_1_1 = QPushButton('Inter')
        self.button_win_1_2 = QPushButton('A-class')
        self.button_win_1_3 = QPushButton('Open')
        self.button_win_1_4 = QPushButton('Назад')

        label_win_1.setFont(QFont('Arial', 12, QFont.Bold))
        self.button_win_1_1.setFont(QFont('Arial', 10))
        self.button_win_1_2.setFont(QFont('Arial', 10))
        self.button_win_1_3.setFont(QFont('Arial', 10))
        self.button_win_1_4.setFont(QFont('Arial', 10))

        self.button_win_1_1.setFixedWidth(400)
        self.button_win_1_2.setFixedWidth(400)
        self.button_win_1_3.setFixedWidth(400)
        self.button_win_1_4.setFixedWidth(400)

        main_layout_1 = QVBoxLayout()

        main_layout_1.addWidget(label_win_1, alignment=Qt.AlignCenter)
        main_layout_1.addWidget(self.button_win_1_1, alignment=Qt.AlignCenter)
        main_layout_1.addWidget(self.button_win_1_2, alignment=Qt.AlignCenter)
        main_layout_1.addWidget(self.button_win_1_3, alignment=Qt.AlignCenter)
        main_layout_1.addWidget(self.button_win_1_4, alignment=Qt.AlignCenter)

        self.setLayout(main_layout_1)

        self.button_win_1_1.clicked.connect(self.open_inter_win)
        self.button_win_1_2.clicked.connect(self.open_aclass_win)
        self.button_win_1_3.clicked.connect(self.open_open_win)
        self.button_win_1_4.clicked.connect(self.open_main_win_1)

    def open_inter_win(self):
        self.inter_win = Inter_window()
        self.inter_win.show()

    def open_aclass_win(self):
        self.aclass_win = Aclass_window()
        self.aclass_win.show()

    def open_open_win(self):
        self.open_win = Open_window()
        self.open_win.show()

    def open_main_win_1(self):
        self.main_win = Main_window()
        self.main_win.show()


class Inter_window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('VFS 2-way Inter')
        self.resize(450, 400)

        results = generate_draws_inter_bb() + generate_draws_inter_hu()

        self.label_win_inter = QLabel('; '.join(results[0]) + "\n" + '; '.join(results[1]) + "\n" +
                                      '; '.join(results[2]) + "\n" + '; '.join(results[3]) + "\n" +
                                      '; '.join(results[4]))
        self.button_win_inter_1 = QPushButton('Сгенерировать еще')
        self.button_win_inter_2 = QPushButton('Назад')

        self.label_win_inter.setFont(QFont('Arial', 12, QFont.Bold))
        self.button_win_inter_1.setFont(QFont('Arial', 10))
        self.button_win_inter_2.setFont(QFont('Arial', 10))

        self.button_win_inter_1.setFixedWidth(400)
        self.button_win_inter_2.setFixedWidth(400)

        main_layout_inter = QVBoxLayout()

        main_layout_inter.addWidget(self.label_win_inter, alignment=Qt.AlignCenter)
        main_layout_inter.addWidget(self.button_win_inter_1, alignment=Qt.AlignCenter)
        main_layout_inter.addWidget(self.button_win_inter_2, alignment=Qt.AlignCenter)

        self.setLayout(main_layout_inter)

        self.button_win_inter_1.clicked.connect(self.get_draws_inter)
        self.button_win_inter_2.clicked.connect(self.open_win_1)

    def open_win_1(self):
        self.win_1 = Window_1()
        self.win_1.show()

    def get_draws_inter(self):
        results = generate_draws_inter_bb() + generate_draws_inter_hu()
        self.label_win_inter.setText('; '.join(results[0]) + "\n" + '; '.join(results[1]) + "\n" +
                                     '; '.join(results[2]) + "\n" + '; '.join(results[3]) + "\n" +
                                     '; '.join(results[4]))


class Aclass_window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('VFS 2-way A-class')
        self.resize(450, 400)

        results = generate_draws_aclass_bb() + generate_draws_aclass_hu()

        self.label_win_aclass = QLabel('; '.join(results[0]) + "\n" + '; '.join(results[1]) + "\n" +
                                       '; '.join(results[2]) + "\n" + '; '.join(results[3]) + "\n" +
                                       '; '.join(results[4]))
        self.button_win_aclass_1 = QPushButton('Сгенерировать еще')
        self.button_win_aclass_2 = QPushButton('Назад')

        self.label_win_aclass.setFont(QFont('Arial', 12, QFont.Bold))
        self.button_win_aclass_1.setFont(QFont('Arial', 10))
        self.button_win_aclass_2.setFont(QFont('Arial', 10))

        self.button_win_aclass_1.setFixedWidth(400)
        self.button_win_aclass_2.setFixedWidth(400)

        main_layout_aclass = QVBoxLayout()

        main_layout_aclass.addWidget(self.label_win_aclass, alignment=Qt.AlignCenter)
        main_layout_aclass.addWidget(self.button_win_aclass_1, alignment=Qt.AlignCenter)
        main_layout_aclass.addWidget(self.button_win_aclass_2, alignment=Qt.AlignCenter)

        self.setLayout(main_layout_aclass)

        self.button_win_aclass_1.clicked.connect(self.get_draws_aclass)
        self.button_win_aclass_2.clicked.connect(self.open_win_1)

    def open_win_1(self):
        self.win_1 = Window_1()
        self.win_1.show()

    def get_draws_aclass(self):
        results = generate_draws_aclass_bb() + generate_draws_aclass_hu()
        self.label_win_aclass.setText('; '.join(results[0]) + "\n" + '; '.join(results[1]) + "\n" +
                                     '; '.join(results[2]) + "\n" + '; '.join(results[3]) + "\n" +
                                     '; '.join(results[4]))


class Open_window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('VFS 2-way Open')
        self.resize(450, 400)

        results = generate_draws_open_bb() + generate_draws_open_hu()

        self.label_win_open = QLabel('; '.join(results[0]) + "\n" + '; '.join(results[1]) + "\n" +
                                     '; '.join(results[2]) + "\n" + '; '.join(results[3]) + "\n" +
                                     '; '.join(results[4]) + "\n" + '; '.join(results[5]))
        self.button_win_open_1 = QPushButton('Сгенерировать еще')
        self.button_win_open_2 = QPushButton('Назад')

        self.label_win_open.setFont(QFont('Arial', 12, QFont.Bold))
        self.button_win_open_1.setFont(QFont('Arial', 10))
        self.button_win_open_2.setFont(QFont('Arial', 10))

        self.button_win_open_1.setFixedWidth(400)
        self.button_win_open_2.setFixedWidth(400)

        main_layout_open = QVBoxLayout()

        main_layout_open.addWidget(self.label_win_open, alignment=Qt.AlignCenter)
        main_layout_open.addWidget(self.button_win_open_1, alignment=Qt.AlignCenter)
        main_layout_open.addWidget(self.button_win_open_2, alignment=Qt.AlignCenter)

        self.setLayout(main_layout_open)

        self.button_win_open_1.clicked.connect(self.get_draws_open)
        self.button_win_open_2.clicked.connect(self.open_win_1)

    def open_win_1(self):
        self.win_1 = Window_1()
        self.win_1.show()

    def get_draws_open(self):
        results = generate_draws_open_bb() + generate_draws_open_hu()
        self.label_win_open.setText('; '.join(results[0]) + "\n" + '; '.join(results[1]) + "\n" +
                                     '; '.join(results[2]) + "\n" + '; '.join(results[3]) + "\n" +
                                     '; '.join(results[4]))


class Window_2(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Генератор жеребьевки VFS 4-way')
        self.resize(450, 400)

        results = generate_draws_4way()

        self.label_win_2 = QLabel('; '.join(results[0]) + "\n" + '; '.join(results[1]) + "\n" +
                                  '; '.join(results[2]) + "\n" + '; '.join(results[3]) + "\n" +
                                  '; '.join(results[4]) + "\n" + '; '.join(results[5]) + "\n" +
                                  '; '.join(results[6]) + "\n" + '; '.join(results[7]) + "\n" +
                                  '; '.join(results[8]) + "\n" + '; '.join(results[9]))
        self.button_win_2_1 = QPushButton('Сгенерировать еще')
        self.button_win_2_2 = QPushButton('Назад')

        self.label_win_2.setFont(QFont('Arial', 12, QFont.Bold))
        self.button_win_2_1.setFont(QFont('Arial', 10))
        self.button_win_2_2.setFont(QFont('Arial', 10))

        self.button_win_2_1.setFixedWidth(400)
        self.button_win_2_2.setFixedWidth(400)

        main_layout_2 = QVBoxLayout()

        main_layout_2.addWidget(self.label_win_2, alignment=Qt.AlignCenter)
        main_layout_2.addWidget(self.button_win_2_1, alignment=Qt.AlignCenter)
        main_layout_2.addWidget(self.button_win_2_2, alignment=Qt.AlignCenter)

        self.setLayout(main_layout_2)

        self.button_win_2_1.clicked.connect(self.get_draws_4way)
        self.button_win_2_2.clicked.connect(self.open_main_win_2)

    def open_main_win_2(self):
        self.main_win = Main_window()
        self.main_win.show()

    def get_draws_4way(self):
        results = generate_draws_4way()
        self.label_win_2.setText('; '.join(results[0]) + "\n" + '; '.join(results[1]) + "\n" +
                                 '; '.join(results[2]) + "\n" + '; '.join(results[3]) + "\n" +
                                 '; '.join(results[4]) + "\n" + '; '.join(results[5]) + "\n" +
                                 '; '.join(results[6]) + "\n" + '; '.join(results[7]) + "\n" +
                                 '; '.join(results[8]) + "\n" + '; '.join(results[9]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    main_win = Main_window()
    main_win.show()
    sys.exit(app.exec_())
