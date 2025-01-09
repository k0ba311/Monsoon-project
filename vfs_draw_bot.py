import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram import F

waiting_for_user_message = False
appeal_type = ''


def generate_draws_4_way():
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
    bb_figures = ['BB-A', 'BB-B', 'BB-C', 'BB-D', 'BB-E', 'BB-F', 'BB-G', 'BB-H', 'BB-J', 'BB-K',
                  'BB-L']  # Массив с фигурами BB
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
    bb_figures = ['BB-A', 'BB-B', 'BB-C', 'BB-D', 'BB-E', 'BB-F', 'BB-G', 'BB-H', 'BB-J', 'BB-K',
                  'BB-L']  # Массив с фигурами BB
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
    hd_figures = ['HD-A', 'HD-B', 'HD-C', 'HD-D', 'HD-E', 'HD-F', 'HD-G', 'HD-H', 'HD-J',
                  'HD-K']  # Массив с фигурами HD
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


def get_keyboard_dis():
    buttons_dis = [
        [types.InlineKeyboardButton(text="VFS 2-WAY", callback_data="2-way")],
        [types.InlineKeyboardButton(text="VFS 4-WAY", callback_data="4-way")]
    ]

    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons_dis)
    return keyboard


def get_keyboard_class():
    buttons_class = [
        [types.InlineKeyboardButton(text="Inter", callback_data="inter")],
        [types.InlineKeyboardButton(text="A-class", callback_data="a-class")],
        [types.InlineKeyboardButton(text="Open", callback_data="open")]
    ]

    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons_class)
    return keyboard


def get_keyboard_draw():
    buttons_draw = [
        [types.InlineKeyboardButton(text="Назад", callback_data="back")]
    ]

    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons_draw)
    return keyboard


BOT_TOKEN = "7797752086:AAHG8ik6lgYoI24JDgMphWJMh_sZbtsZSXE"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Выберите дисциплину:",
        reply_markup=get_keyboard_dis()
    )


@dp.callback_query(F.data == "back")
async def show_dis_menu(callback: types.CallbackQuery):
    await callback.message.answer(
        "Выберите дисциплину:",
        reply_markup=get_keyboard_dis()
    )


@dp.callback_query(F.data == "2-way")
async def show_class_menu(callback: types.CallbackQuery):
    await callback.message.answer(
        "Выберите класс:",
        reply_markup=get_keyboard_class()
    )


@dp.callback_query(F.data == "4-way")
async def show_4way_draw(callback: types.CallbackQuery):
    results = generate_draws_4_way()
    await callback.message.answer(
        '1) ' + '; '.join(results[0]) + "\n\n" + '2) ' + '; '.join(results[1]) + "\n\n" + '3) ' + '; '.join(
            results[2]) + "\n\n" + '4) ' + '; '.join(
            results[3]) + "\n\n" + '5) ' + '; '.join(results[4]) + "\n\n" + '6) ' + '; '.join(
            results[5]) + "\n\n" + '7) ' + '; '.join(
            results[6]) + "\n\n" + '8) ' + '; '.join(results[7]) + "\n\n" + '9) ' + '; '.join(
            results[8]) + "\n\n" + '9) ' + '; '.join(results[9]),
        reply_markup=get_keyboard_draw()
    )


@dp.callback_query(F.data == "inter")
async def show_inter_draw(callback: types.CallbackQuery):
    results = generate_draws_inter_bb() + generate_draws_inter_hu()
    await callback.message.answer(
        '<b>Inter</b>\n\n' + '1) ' + '; '.join(results[0]) + "\n\n" + '2) ' + '; '.join(results[1]) + "\n\n" + '3) ' + '; '.join(
            results[2]) + "\n\n" + '4) ' + '; '.join(
            results[3]) + "\n\n" + '5) ' + '; '.join(results[4]),
        parse_mode=ParseMode.HTML,
        reply_markup=get_keyboard_draw()
    )


@dp.callback_query(F.data == "a-class")
async def show_aclass_draw(callback: types.CallbackQuery):
    results = generate_draws_aclass_bb() + generate_draws_aclass_hu()
    await callback.message.answer(
        '<b>A-class</b>\n\n' + '1) ' + '; '.join(results[0]) + "\n\n" + '2) ' + '; '.join(results[1]) + "\n\n" + '3) ' + '; '.join(
            results[2]) + "\n\n" + '4) ' + '; '.join(
            results[3]) + "\n\n" + '5) ' + '; '.join(results[4]),
        parse_mode=ParseMode.HTML,
        reply_markup=get_keyboard_draw()
    )


@dp.callback_query(F.data == "open")
async def show_open_draw(callback: types.CallbackQuery):
    results = generate_draws_open_bb() + generate_draws_open_hu()
    await callback.message.answer(
        '<b>Open</b>\n\n' + '1) ' + '; '.join(results[0]) + "\n\n" + '2) ' + '; '.join(results[1]) + "\n\n" + '3) ' + '; '.join(
            results[2]) + "\n\n" + '4) ' + '; '.join(
            results[3]) + "\n\n" + '5) ' + '; '.join(results[4]) + "\n\n" + '6) ' + '; '.join(results[5]),
        parse_mode=ParseMode.HTML,
        reply_markup=get_keyboard_draw()
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
