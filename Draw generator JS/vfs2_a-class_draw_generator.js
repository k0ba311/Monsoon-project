function generateDrawsBB() {
    const bb_figures = ['BB-A', 'BB-B', 'BB-C', 'BB-D', 'BB-E', 'BB-F', 'BB-G', 'BB-H', 'BB-J', 'BB-K', 'BB-L']; // Массив с фигурами BB
    const bb_blocks = ['BB-01', 'BB-02']; // Массив с блоками BB

    let allElements = [...bb_figures, ...bb_blocks]; // Объединяем массивы
    let draws = []; // Массив для хранения жеребьевок

    while (draws.length < 2) {
        let totalCost = Math.random() < 0.5 ? 5 : 6; // Случайная сумма стоимости (5 или 6)
        let draw = [];
        let currentCost = 0;
        let usedElements = []; // Для отслеживания уже использованных элементов

        while (currentCost < totalCost && draw.length < allElements.length) {
            // Выбираем случайный элемент
            let randomIndex = Math.floor(Math.random() * allElements.length);
            let element = allElements[randomIndex];

            // Определяем стоимость элемента
            let cost = bb_figures.includes(element) ? 1 : 2;

            // Проверяем, можем ли добавить элемент в жеребьевку
            if (!usedElements.includes(element) && currentCost + cost <= totalCost) {
                draw.push(element);
                usedElements.push(element);
                currentCost += cost;
            }
        }

        // Проверяем, достигли ли мы нужной суммы стоимости
        if (currentCost === totalCost) {
            draws.push(draw);
            // Удаляем использованные элементы из общего списка
            allElements = allElements.filter(el => !usedElements.includes(el));
        }
    }

    return draws;
}

function generateDrawsHU() {
    const hu_figures = ['HU-A', 'HU-B', 'HU-C', 'HU-D', 'HU-E', 'HU-F', 'HU-G', 'HU-H', 'HU-J']; // Массив с фигурами HU
    const hu_blocks = ['HU-01', 'HU-02', 'HU-03', 'HU-04']; // Массив с блоками HU
    const hd_figures = ['HD-A', 'HD-B', 'HD-C', 'HD-E', 'HD-F', 'HD-G', 'HD-H', 'HD-J', 'HD-K']; // Массив с фигурами HD
    const hd_blocks = ['HD-01', 'HD-02', 'HD-03', 'HD-04', 'HD-05']; // Массив с блоками HD

    let allElements = [...hu_figures, ...hu_blocks, ...hd_figures, ...hd_blocks]; // Объединяем массивы
    let draws = []; // Массив для хранения жеребьевок

    while (draws.length < 3) {
        let totalCost = Math.random() < 0.5 ? 5 : 6; // Случайная сумма стоимости (5 или 6)
        let draw = [];
        let currentCost = 0;
        let usedElements = []; // Для отслеживания уже использованных элементов

        while (currentCost < totalCost && draw.length < allElements.length) {
            // Выбираем случайный элемент
            let randomIndex = Math.floor(Math.random() * allElements.length);
            let element = allElements[randomIndex];

            // Определяем стоимость элемента
            let cost = (hu_figures.includes(element)) || (hd_figures.includes(element)) ? 1 : 2;

            // Проверяем, можем ли добавить элемент в жеребьевку
            if (!usedElements.includes(element) && currentCost + cost <= totalCost) {
                draw.push(element);
                usedElements.push(element);
                currentCost += cost;
            }
        }

        // Проверяем, достигли ли мы нужной суммы стоимости
        if (currentCost === totalCost) {
            draws.push(draw);
            // Удаляем использованные элементы из общего списка
            allElements = allElements.filter(el => !usedElements.includes(el));
        }
    }

    return draws;
}

const results = [...generateDrawsBB(), ...generateDrawsHU()];
for (let i = 0; i < results.length; i++) {
    console.log(results[i].join('; '))
}