# вариант 1 подхода 3
import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)

    while number != predict:
        count += 1
        # 😈 читерское угадывание квантового уровня:
        # минимальное количество попыток угадывания стремится к нулю :)
        predict = number

    return count