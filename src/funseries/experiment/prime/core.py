"""素数判定和生成函数。"""

import math
import random


def is_prime(n: int, d: int = 2) -> bool:
    """判断整数是否为素数。

    Args:
        n: 待判断的整数。
        d: 递归试除起点，仅供递归调用使用。
    Returns:
        n 为素数时返回 True。
    """
    if n < 2:
        return False
    if d > math.isqrt(n):
        return True
    return n % d != 0 and is_prime(n, d + 1)


def is_prime2(n: int, trials: int = 10) -> bool:
    """使用 Miller-Rabin 概率算法判断整数是否为素数。"""
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
    """生成不超过上限数量和数值的素数列表。"""
    if max_size < 0:
        raise ValueError("max_size 不能为负数")
    if max_value is not None and max_value < 2:
        raise ValueError("max_value 必须至少为 2")
    limit = max_value or 100_000_000_000
    return [n for n in range(2, limit) if is_prime(n)][:max_size]
