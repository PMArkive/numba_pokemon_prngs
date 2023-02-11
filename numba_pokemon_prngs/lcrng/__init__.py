"""Linear Congruential Pseudo Random Number Generators"""
import numba
from .lcrng32 import (
    LCRNG32,
    LCRNG32RandomDistribution,
    lcrng32_init,
)

# pylint: disable=abstract-method


@numba.experimental.jitclass()
@lcrng32_init(
    add=0x6073, mult=0x41C64E6D, distribution=LCRNG32RandomDistribution.MODULO
)
class PokeRNGMod(LCRNG32):
    """Standard Pokemon LCRNG with modulo random distribution"""


@numba.experimental.jitclass()
@lcrng32_init(
    add=0x6073,
    mult=0x41C64E6D,
    distribution=LCRNG32RandomDistribution.RECIPROCAL_DIVISION,
)
class PokeRNGDiv(LCRNG32):
    """Standard Pokemon LCRNG with reciprocal division random distribution"""


@numba.experimental.jitclass()
@lcrng32_init(
    add=0x6073,
    mult=0x41C64E6D,
    distribution=LCRNG32RandomDistribution.MODULO,
    reverse=True,
)
class PokeRNGRMod(LCRNG32):
    """Reversed Standard Pokemon LCRNG with modulo random distribution"""


@numba.experimental.jitclass()
@lcrng32_init(
    add=0x6073,
    mult=0x41C64E6D,
    distribution=LCRNG32RandomDistribution.RECIPROCAL_DIVISION,
    reverse=True,
)
class PokeRNGRDiv(LCRNG32):
    """Reversed Standard Pokemon LCRNG with reciprocal division random distribution"""


@numba.experimental.jitclass()
@lcrng32_init(
    add=0x1,
    mult=0x6C078965,
    distribution=LCRNG32RandomDistribution.MODULO,
)
class ARNG(LCRNG32):
    """Alternative Pokemon LCRNG with modulo random distribution"""


@numba.experimental.jitclass()
@lcrng32_init(
    add=0x1,
    mult=0x6C078965,
    distribution=LCRNG32RandomDistribution.MODULO,
    reverse=True,
)
class ARNGR(LCRNG32):
    """Reversed Alternative Pokemon LCRNG with modulo random distribution"""


@numba.experimental.jitclass()
@lcrng32_init(
    add=0x269EC3,
    mult=0x343FD,
    distribution=LCRNG32RandomDistribution.MODULO,
)
class XDRNG(LCRNG32):
    """Pokemon Colosseum/XD/Channel LCRNG with modulo random distribution"""


@numba.experimental.jitclass()
@lcrng32_init(
    add=0x269EC3,
    mult=0x343FD,
    distribution=LCRNG32RandomDistribution.MODULO,
    reverse=True,
)
class XDRNGR(LCRNG32):
    """Reversed Pokemon Colosseum/XD/Channel LCRNG with modulo random distribution"""


# pylint: enable=abstract-method
