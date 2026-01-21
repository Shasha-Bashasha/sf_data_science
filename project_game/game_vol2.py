# вариант 2 подхода 3
import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    # задаем минимум из диапазона random
    low = 1
    # задаем максимум из диапазона random
    high = 100
    predict = np.random.randint(1, 101)  # сохраняем точно так, как было

    while number != predict:
        count += 1
        # если предполагаемое число меньше загаданного:
        if number > predict:
            # увеличиваем минимум на 1
            low = predict + 1
        # в противном случае:
        else:
            # уменьшаем максимум на 1
            high = predict - 1
        # теперь берем середину диапазона
        predict = (low + high) // 2

    return count