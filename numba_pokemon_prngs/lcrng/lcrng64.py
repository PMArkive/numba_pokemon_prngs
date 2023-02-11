"""64bit Linear Congruential Pseudo Random Number Generator"""

from __future__ import annotations
from typing import Type, Callable
import enum
import numba
import numpy as np


class LCRNG64RandomDistribution(enum.IntEnum):
    """
    Various LCRNG64 random distribution types

    MULTIPLICATION_SHIFT -> (next_u32() * maximum) >> 32
    """

    NONE = 0
    MULTIPLICATION_SHIFT = 1


class LCRNG64:
    """64-bit LCRNG parent class"""

    seed: numba.uint64

    def __init__(self, seed: np.uint64) -> None:
        self.seed: np.uint64 = seed

    def next(self) -> np.uint64:
        """
        Generate and return the next full 64-bit random uint

        () -> seed = seed * mult + add
        """
        raise NotImplementedError()

    def jump(self, adv: np.uint64) -> np.uint64:
        """Jump ahead the LCRNG sequence by adv"""
        raise NotImplementedError()

    def advance(self, adv: np.uint64) -> np.uint64:
        """Advance the LCRNG sequence by adv"""
        for _ in range(adv):
            self.next()
        return self.seed

    def next_u32(self) -> np.uint32:
        """Generate and return the next 32-bit random uint"""
        return self.next() >> 32

    def next_rand(self, maximum: np.uint32) -> np.uint32:
        """
        Generate and return the next [0, maximum) random uint

        () -> distribution(self.next_u32(), maximum)
        """
        raise NotImplementedError()


def lcrng64_init(
    *,
    add: np.uint64,
    mult: np.uint64,
    distribution: LCRNG64RandomDistribution = LCRNG64RandomDistribution.NONE,
    reverse: bool = False,
) -> Callable[[Type[LCRNG64]], Type[LCRNG64]]:
    """Initialize a LCRNG64 class with constants and random distribution"""
    if reverse:
        mult = pow(mult, -1, 0x10000000000000000)
        add = (-add * mult) & 0xFFFFFFFFFFFFFFFF

    jump_table = [(add, mult)]
    for i in range(63):
        jump_table.append(
            (
                (jump_table[i][0] * (jump_table[i][1] + 1)) & 0xFFFFFFFFFFFFFFFF,
                (jump_table[i][1] * jump_table[i][1]) & 0xFFFFFFFFFFFFFFFF,
            )
        )
    jump_table = tuple(jump_table)

    def wrap(lcrng_class: Type[LCRNG64]) -> Type[LCRNG64]:
        def next_(self: LCRNG64) -> np.uint32:
            self.seed = self.seed * mult + add
            return self.seed

        def jump(self: LCRNG64, adv: np.uint64):
            i = 0
            while adv:
                if adv & 1:
                    add, mult = jump_table[i]
                    self.seed = self.seed * mult + add
                adv >>= 1
            return self.seed

        if distribution == LCRNG64RandomDistribution.MULTIPLICATION_SHIFT:

            def next_rand(self: LCRNG64, maximum: np.uint32) -> np.uint32:
                return (self.next_u32() * maximum) >> 32

        else:

            def next_rand(self: LCRNG64, maximum: np.uint32) -> np.uint32:
                raise NotImplementedError()

        lcrng_class.next = next_
        lcrng_class.jump = jump
        lcrng_class.next_rand = next_rand
        return lcrng_class

    return wrap
