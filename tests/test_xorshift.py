"""Tests for Xorshift classes"""
from numba_pokemon_prngs.xorshift import (
    Xorshift128,
    Xoroshiro128PlusRejection,
    SplitMixXoroshiro128Plus,
)


def test_init():
    """Test initialization re_init() functions"""
    test_splitmixxoroshiro128plus = SplitMixXoroshiro128Plus(0)
    assert tuple(
        tuple(test_splitmixxoroshiro128plus.state)
        for _ in (
            test_splitmixxoroshiro128plus.re_init(seed)
            for seed in (0x12345678, 0x87654321, 0xCAFEBEEF, 0xDEADBEEF, 0xBEEFCAFE)
        )
    ) == (
        (4103302876398381935, 16133041902329894167),
        (15779530522407162504, 18036422292597032046),
        (16974760463792686510, 6191428841595969426),
        (5395234354446855067, 16021672434157553954),
        (6041607748924030458, 8399375536991227553),
    )


def test_next():
    """Test next/previous advance functions"""
    test_xorshift128 = Xorshift128(0x12345678, 0x87654321, 0xDEADBEEF, 0xBEEFCAFE)
    test_splitmixxoroshiro128plus = SplitMixXoroshiro128Plus(0x12345678)
    test_xoroshiro128plusrejection = Xoroshiro128PlusRejection(0x12345678)

    assert tuple(test_xorshift128.next() for _ in range(5)) == (
        249089229,
        2735340156,
        283144756,
        3499684588,
        418312854,
    )

    assert tuple(test_xorshift128.previous() for _ in range(5)) == (
        418312854,
        3499684588,
        283144756,
        2735340156,
        249089229,
    )

    assert tuple(test_splitmixxoroshiro128plus.next() for _ in range(5)) == (
        416673884,
        10456666,
        1220117690,
        3668624070,
        2653509652,
    )

    assert tuple(test_splitmixxoroshiro128plus.previous() for _ in range(5)) == (
        2653509652,
        3668624070,
        1220117690,
        10456666,
        416673884,
    )

    assert tuple(test_xoroshiro128plusrejection.next() for _ in range(5)) == (
        9413281288113209555,
        5254920089485994697,
        13325847552699995764,
        18221136201721511112,
        15617030143133486355,
    )

    assert tuple(test_xoroshiro128plusrejection.previous() for _ in range(5)) == (
        15617030143133486355,
        18221136201721511112,
        13325847552699995764,
        5254920089485994697,
        9413281288113209555,
    )


def test_next_rand():
    """Test next_randrange/next_rand/next_float_randrange bounded rand functions"""
    test_xorshift128 = Xorshift128(0x12345678, 0x87654321, 0xDEADBEEF, 0xBEEFCAFE)
    test_splitmixxoroshiro128plus = SplitMixXoroshiro128Plus(0x12345678)
    test_xoroshiro128plusrejection = Xoroshiro128PlusRejection(0x12345678)

    assert tuple(
        tuple(test_xorshift128.next_rand(maximum) for _ in range(5))
        for maximum in (2, 5, 25, 100, 256)
    ) == (
        (1, 0, 0, 0, 0),
        (1, 1, 0, 2, 2),
        (3, 22, 8, 19, 21),
        (30, 40, 93, 72, 39),
        (82, 60, 116, 44, 6),
    )

    assert tuple(
        tuple(test_xorshift128.next_randrange(minimum, maximum) for _ in range(5))
        for minimum, maximum in ((0, 2), (2, 5), (10, 25), (50, 100), (240, 256))
    ) == (
        (1, 1, 1, 0, 1),
        (2, 4, 3, 2, 4),
        (19, 13, 10, 15, 14),
        (94, 91, 99, 91, 91),
        (250, 243, 240, 255, 247),
    )

    assert tuple(
        tuple(test_xorshift128.next_float_randrange(minimum, maximum) for _ in range(5))
        for minimum, maximum in (
            (0.0, 2.0),
            (2.0, 5.0),
            (3.0, 12.0),
            (10.0, 25.0),
            (50.0, 100.0),
            (240.0, 256.0),
        )
    ) == (
        (
            1.4062709212303162,
            1.8026826083660126,
            0.3794565200805664,
            1.508473813533783,
            1.1949046850204468,
        ),
        (
            4.62663896381855,
            4.7586337104439735,
            2.6715264320373535,
            4.023965150117874,
            3.1387452483177185,
        ),
        (
            7.068772077560425,
            10.153619647026062,
            3.4334449768066406,
            7.900472640991211,
            11.595278233289719,
        ),
        (
            11.794858694076538,
            20.038075536489487,
            19.8233343064785,
            13.392053842544556,
            10.621049404144287,
        ),
        (
            87.25868308544159,
            73.74181962013245,
            64.16280388832092,
            54.820579051971436,
            56.12268877029419,
        ),
        (
            253.61190795898438,
            254.23838806152344,
            255.02412223815918,
            252.3646469116211,
            245.0315704345703,
        ),
    )

    assert tuple(
        tuple(test_xorshift128.next_alternate_rand(maximum) for _ in range(5))
        for maximum in (2, 5, 25, 100, 256)
    ) == (
        (1, 0, 1, 0, 1),
        (1, 0, 2, 3, 4),
        (13, 0, 0, 20, 2),
        (78, 81, 17, 80, 66),
        (154, 56, 253, 228, 88),
    )

    assert tuple(
        tuple(test_splitmixxoroshiro128plus.next_rand(maximum) for _ in range(5))
        for maximum in (2, 5, 25, 100, 256)
    ) == (
        (0, 0, 0, 0, 0),
        (4, 4, 1, 3, 1),
        (15, 12, 24, 5, 20),
        (33, 83, 8, 75, 86),
        (124, 99, 230, 179, 252),
    )

    assert tuple(
        tuple(test_xoroshiro128plusrejection.next_rand(maximum) for _ in range(5))
        for maximum in (2, 5, 25, 100, 256)
    ) == (
        (1, 1, 0, 0, 1),
        (3, 1, 3, 2, 1),
        (20, 5, 22, 18, 15),
        (71, 41, 5, 57, 59),
        (217, 128, 23, 79, 63),
    )
