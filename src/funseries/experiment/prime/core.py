"""素数判定和生成函数。"""

import math
import random


def is_prime(n: int, d: int = 2) -> bool:
    """判断整数是否为素数。

    Args:
        n: 待判断的整数。
        d: 试除起点，仅供内部调用使用。
    Returns:
        n 为素数时返回 True。
    """
    if n < 2:
        return False
    while d <= math.isqrt(n):
        if n % d == 0:
            return False
        d += 1
    return True


def is_prime2(n: int, trials: int = 10) -> bool:
    """使用 Miller-Rabin 概率算法判断整数是否为素数。

    Args:
        n: 待判断的整数，必须至少为 2。
        trials: 随机底数测试次数，必须为正数。

    Returns:
        通过全部概率测试时返回 True，确定为合数时返回 False。

    Raises:
        ValueError: n 小于 2 或 trials 不是正数。
    """
    if n < 2 or trials < 1:
        raise ValueError("n 必须至少为 2，trials 必须为正数")
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    def try_composite(a: int) -> bool:
        if pow(a, d, n) in (1, n - 1):
            return False
        return all(pow(a, 2**i * d, n) != n - 1 for i in range(1, s))

    return not any(try_composite(random.randrange(2, n)) for _ in range(trials))


def prime_generate(max_size: int = 10, max_value: int | None = None) -> list[int]:
    """生成不超过数量和数值上限的素数列表。

    Args:
        max_size: 最多返回的素数数量，不能为负数。
        max_value: 可选的闭区间数值上限，必须至少为 2。

    Returns:
        从 2 开始按升序排列的素数列表。

    Raises:
        ValueError: max_size 为负数或 max_value 小于 2。
    """
    if max_size < 0:
        raise ValueError("max_size 不能为负数")
    if max_value is not None and max_value < 2:
        raise ValueError("max_value 必须至少为 2")
    result = []
    candidate = 2
    while len(result) < max_size and (max_value is None or candidate <= max_value):
        if is_prime(candidate):
            result.append(candidate)
        candidate += 1
    return result
