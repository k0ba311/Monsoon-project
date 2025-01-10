function generateDraws() {
    const figures = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q']; // Массив с фигурами
    const blocks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22']; // Массив с блоками

    let allElements = [...figures, ...blocks]; // Объединяем массивы
    let draws = []; // Массив для хранения жеребьевок

    while (draws.length < 10) {
        let totalCost = Math.random() < 0.5 ? 5 : 6; // Случайная сумма стоимости (5 или 6)
        let draw = [];
        let currentCost = 0;
        let usedElements = []; // Для отслеживания уже использованных элементов

        while (currentCost < totalCost && draw.length < allElements.length) {
            // Выбираем случайный элемент
            let randomIndex = Math.floor(Math.random() * allElements.length);
            let element = allElements[randomIndex];

            // Определяем стоимость элемента
            let cost = figures.includes(element) ? 1 : 2;

            // Проверяем, можем ли добавить элемент в жеребьевку
            if (!usedElements.includes(element) && currentCost + cost <= totalCost) {
                draw.push(element);
                usedElements.push(element);
                currentCost += cost;
            }
        }

        // Проверяем, достигли ли мы нужной суммы стоимости
        if ((draw.filter(el => figures.includes(el)).length) <= 3) {
            draws.push(draw)
            // Удаляем использованные элементы из общего списка
            allElements = allElements.filter(el => !usedElements.includes(el));
        }
    }

    return draws;
}

const results = generateDraws();
for (let i = 0; i < results.length; i++) {
    console.log(results[i].join('; '))
}