"""Tests for LCRNG classes"""
from numba_pokemon_prngs.lcrng import (
    PokeRNGDiv,
    PokeRNGMod,
    PokeRNGRDiv,
    PokeRNGRMod,
    ARNG,
    ARNGR,
    XDRNG,
    XDRNGR,
    BWRNG,
    BWRNGR,
)


def test_lcrng32_next():
    """Test LCRNG32 next() calls for full seed"""
    test_pokerng_div = PokeRNGDiv(0x12345678)
    test_pokerng_mod = PokeRNGMod(0x12345678)
    test_arng = ARNG(0x12345678)
    test_xdrng = XDRNG(0x12345678)

    test_pokerngr_div = PokeRNGRDiv(0x12345678)
    test_pokerngr_mod = PokeRNGRMod(0x12345678)
    test_arngr = ARNGR(0x12345678)
    test_xdrngr = XDRNGR(0x12345678)
    assert tuple(test_pokerng_div.next() for _ in range(5)) == (
        192004491,
        2229936802,
        3649731437,
        4108329948,
        646229279,
    )
    assert tuple(test_pokerng_mod.next() for _ in range(5)) == (
        192004491,
        2229936802,
        3649731437,
        4108329948,
        646229279,
    )
    assert tuple(test_arng.next() for _ in range(5)) == (
        775181657,
        499207454,
        4082793175,
        2119206356,
        103760037,
    )
    assert tuple(test_xdrng.next() for _ in range(5)) == (
        3018423131,
        1530878130,
        3423460525,
        3768712380,
        1536596111,
    )

    assert tuple(test_pokerngr_div.next() for _ in range(5)) == (
        1358145273,
        3431847134,
        687875895,
        3556988756,
        4100256197,
    )
    assert tuple(test_pokerngr_mod.next() for _ in range(5)) == (
        1358145273,
        3431847134,
        687875895,
        3556988756,
        4100256197,
    )
    assert tuple(test_arngr.next() for _ in range(5)) == (
        2408337579,
        2286114914,
        3692372301,
        373632348,
        1342820287,
    )
    assert tuple(test_xdrngr.next() for _ in range(5)) == (
        3745948697,
        399063950,
        1307699815,
        631669108,
        1486693829,
    )


def test_lcrng32_next_u16():
    """Test LCRNG32 next_u16() calls for 16-bit rand"""
    test_pokerng_div = PokeRNGDiv(0x12345678)
    test_pokerng_mod = PokeRNGMod(0x12345678)
    test_arng = ARNG(0x12345678)
    test_xdrng = XDRNG(0x12345678)

    test_pokerngr_div = PokeRNGRDiv(0x12345678)
    test_pokerngr_mod = PokeRNGRMod(0x12345678)
    test_arngr = ARNGR(0x12345678)
    test_xdrngr = XDRNGR(0x12345678)
    assert tuple(test_pokerng_div.next_u16() for _ in range(5)) == (
        2929,
        34026,
        55690,
        62688,
        9860,
    )
    assert tuple(test_pokerng_mod.next_u16() for _ in range(5)) == (
        2929,
        34026,
        55690,
        62688,
        9860,
    )
    assert tuple(test_arng.next_u16() for _ in range(5)) == (
        11828,
        7617,
        62298,
        32336,
        1583,
    )
    assert tuple(test_xdrng.next_u16() for _ in range(5)) == (
        46057,
        23359,
        52237,
        57505,
        23446,
    )

    assert tuple(test_pokerngr_div.next_u16() for _ in range(5)) == (
        20723,
        52365,
        10496,
        54275,
        62564,
    )
    assert tuple(test_pokerngr_mod.next_u16() for _ in range(5)) == (
        20723,
        52365,
        10496,
        54275,
        62564,
    )
    assert tuple(test_arngr.next_u16() for _ in range(5)) == (
        36748,
        34883,
        56341,
        5701,
        20489,
    )
    assert tuple(test_xdrngr.next_u16() for _ in range(5)) == (
        57158,
        6089,
        19953,
        9638,
        22685,
    )


def test_lcrng32_next_rand():
    """Test LCRNG32 next_rand() calls for bounded rand"""
    test_pokerng_div = PokeRNGDiv(0x12345678)
    test_pokerng_mod = PokeRNGMod(0x12345678)
    test_arng = ARNG(0x12345678)
    test_xdrng = XDRNG(0x12345678)

    test_pokerngr_div = PokeRNGRDiv(0x12345678)
    test_pokerngr_mod = PokeRNGRMod(0x12345678)
    test_arngr = ARNGR(0x12345678)
    test_xdrngr = XDRNGR(0x12345678)
    assert tuple(
        tuple(test_pokerng_div.next_rand(maximum) for _ in range(5))
        for maximum in (2, 5, 25, 100, 256)
    ) == (
        (0, 1, 1, 1, 0),
        (2, 2, 0, 2, 1),
        (19, 1, 11, 14, 3),
        (70, 74, 25, 72, 68),
        (230, 42, 92, 133, 221),
    )
    assert tuple(
        tuple(test_pokerng_mod.next_rand(maximum) for _ in range(5))
        for maximum in (2, 5, 25, 100, 256)
    ) == (
        (1, 0, 0, 0, 0),
        (2, 2, 3, 3, 3),
        (8, 3, 18, 2, 0),
        (94, 1, 8, 41, 61),
        (76, 93, 38, 12, 132),
    )
    assert tuple(
        tuple(test_arng.next_rand(maximum) for _ in range(5))
        for maximum in (2, 5, 25, 100, 256)
    ) == (
        (0, 1, 0, 0, 1),
        (2, 4, 3, 4, 1),
        (1, 13, 11, 3, 20),
        (15, 33, 57, 36, 87),
        (105, 49, 75, 45, 63),
    )
    assert tuple(
        tuple(test_xdrng.next_rand(maximum) for _ in range(5))
        for maximum in (2, 5, 25, 100, 256)
    ) == (
        (1, 1, 1, 1, 0),
        (2, 3, 3, 3, 2),
        (3, 17, 4, 0, 12),
        (35, 44, 94, 7, 23),
        (8, 0, 173, 89, 232),
    )

    assert tuple(
        tuple(test_pokerngr_div.next_rand(maximum) for _ in range(5))
        for maximum in (2, 5, 25, 100, 256)
    ) == (
        (0, 1, 0, 1, 1),
        (4, 2, 3, 1, 4),
        (3, 10, 15, 24, 15),
        (86, 91, 20, 45, 44),
        (143, 22, 59, 75, 170),
    )
    assert tuple(
        tuple(test_pokerngr_mod.next_rand(maximum) for _ in range(5))
        for maximum in (2, 5, 25, 100, 256)
    ) == (
        (1, 1, 0, 1, 0),
        (3, 1, 0, 3, 4),
        (19, 4, 9, 18, 2),
        (56, 39, 23, 86, 53),
        (51, 229, 5, 237, 186),
    )
    assert tuple(
        tuple(test_arngr.next_rand(maximum) for _ in range(5))
        for maximum in (2, 5, 25, 100, 256)
    ) == (
        (0, 1, 1, 1, 1),
        (4, 1, 1, 0, 0),
        (6, 22, 15, 11, 1),
        (18, 95, 43, 14, 43),
        (65, 82, 251, 148, 64),
    )
    assert tuple(
        tuple(test_xdrngr.next_rand(maximum) for _ in range(5))
        for maximum in (2, 5, 25, 100, 256)
    ) == (
        (0, 1, 1, 0, 1),
        (3, 4, 4, 0, 1),
        (19, 3, 21, 8, 23),
        (14, 84, 97, 77, 67),
        (253, 125, 122, 133, 99),
    )


def test_lcrng32_jump():
    """Test LCRNG32 jump() calls for full seed"""
    test_pokerng_div = PokeRNGDiv(0x12345678)
    test_pokerng_mod = PokeRNGMod(0x12345678)
    test_arng = ARNG(0x12345678)
    test_xdrng = XDRNG(0x12345678)

    test_pokerngr_div = PokeRNGRDiv(0x12345678)
    test_pokerngr_mod = PokeRNGRMod(0x12345678)
    test_arngr = ARNGR(0x12345678)
    test_xdrngr = XDRNGR(0x12345678)

    assert tuple(
        tuple(test_pokerng_div.jump(adv) for _ in range(5))
        for adv in (
            1,
            12,
            123,
            1234,
            12345,
            123456,
            1234567,
            12345678,
            123456789,
            1234567890,
        )
    ) == (
        (192004491, 2229936802, 3649731437, 4108329948, 646229279),
        (2443977505, 1931263475, 3293745685, 1988560903, 606272585),
        (3863795695, 2404443749, 76878123, 848557505, 2719434151),
        (3563840338, 3229125905, 2774120340, 2153296075, 2647165670),
        (1907878308, 4094009970, 3061081296, 4211434558, 526661692),
        (1106492490, 2876501992, 1886967446, 1680496596, 3926204194),
        (3733184135, 240296208, 2651596429, 1997700878, 2153045987),
        (926439135, 1933925659, 2162347671, 486590291, 181707599),
        (3613309471, 1816405231, 1359078335, 1716844175, 3057278303),
        (1868602267, 1364313367, 3958765011, 3824847311, 2479758603),
    )

    assert tuple(
        tuple(test_pokerng_mod.jump(adv) for _ in range(5))
        for adv in (
            1,
            12,
            123,
            1234,
            12345,
            123456,
            1234567,
            12345678,
            123456789,
            1234567890,
        )
    ) == (
        (192004491, 2229936802, 3649731437, 4108329948, 646229279),
        (2443977505, 1931263475, 3293745685, 1988560903, 606272585),
        (3863795695, 2404443749, 76878123, 848557505, 2719434151),
        (3563840338, 3229125905, 2774120340, 2153296075, 2647165670),
        (1907878308, 4094009970, 3061081296, 4211434558, 526661692),
        (1106492490, 2876501992, 1886967446, 1680496596, 3926204194),
        (3733184135, 240296208, 2651596429, 1997700878, 2153045987),
        (926439135, 1933925659, 2162347671, 486590291, 181707599),
        (3613309471, 1816405231, 1359078335, 1716844175, 3057278303),
        (1868602267, 1364313367, 3958765011, 3824847311, 2479758603),
    )

    assert tuple(
        tuple(test_arng.jump(adv) for _ in range(5))
        for adv in (
            1,
            12,
            123,
            1234,
            12345,
            123456,
            1234567,
            12345678,
            123456789,
            1234567890,
        )
    ) == (
        (775181657, 499207454, 4082793175, 2119206356, 103760037),
        (3450747459, 2416635697, 3671767791, 276016381, 4097337563),
        (2657732181, 177699359, 2431986361, 2855293603, 3087786077),
        (912148846, 4226841811, 3005148444, 2503987225, 3913719770),
        (2408380172, 4055789646, 1283489824, 140009218, 588392820),
        (2145976310, 45623048, 4273809194, 3618827484, 3427657886),
        (2537904765, 332520416, 291689143, 2740944178, 2338443457),
        (142535909, 2484119113, 2550317293, 3784327377, 1571252725),
        (1270872997, 3047539029, 3462642437, 1078257845, 3704900197),
        (233438153, 3541667437, 3897951825, 2663753589, 3798332889),
    )

    assert tuple(
        tuple(test_xdrng.jump(adv) for _ in range(5))
        for adv in (
            1,
            12,
            123,
            1234,
            12345,
            123456,
            1234567,
            12345678,
            123456789,
            1234567890,
        )
    ) == (
        (3018423131, 1530878130, 3423460525, 3768712380, 1536596111),
        (405865345, 2101941763, 3701378197, 142804919, 218704873),
        (1275647967, 2757121893, 2108869627, 3727334177, 2164182615),
        (3173628898, 3555499249, 1231267764, 804990107, 1774424406),
        (3377988420, 3773268482, 3514039568, 4070864878, 2526407196),
        (145301274, 1590007400, 2982765446, 2099121652, 246051122),
        (1776714295, 2093436752, 3690047693, 1944395838, 2978286963),
        (2472450127, 1743897963, 2587848903, 3213538915, 238350911),
        (439119247, 3895913695, 2591125551, 1966667647, 791315151),
        (603785195, 2327087943, 3018598627, 4225580223, 2071683803),
    )

    assert tuple(
        tuple(test_pokerngr_div.jump(adv) for _ in range(5))
        for adv in (
            1,
            12,
            123,
            1234,
            12345,
            123456,
            1234567,
            12345678,
            123456789,
            1234567890,
        )
    ) == (
        (1358145273, 3431847134, 687875895, 3556988756, 4100256197),
        (2191608355, 1121904593, 558356047, 2687587613, 2715006907),
        (2402485621, 3965277055, 3547912281, 3632012931, 837133437),
        (4083688238, 3564660403, 300432284, 1847712185, 1673069850),
        (1267538828, 467031566, 1438284064, 1573096770, 1232797428),
        (904249014, 539582728, 2783067754, 1894945628, 1926406238),
        (1120891549, 2135796960, 2815683351, 2065787250, 3002024801),
        (1555842565, 1518145001, 3264470797, 3990502769, 2592402709),
        (2423950533, 2245779573, 1301538853, 1506649045, 1811157893),
        (3156726633, 4208663693, 1587507953, 1759615637, 2047711097),
    )

    assert tuple(
        tuple(test_pokerngr_mod.jump(adv) for _ in range(5))
        for adv in (
            1,
            12,
            123,
            1234,
            12345,
            123456,
            1234567,
            12345678,
            123456789,
            1234567890,
        )
    ) == (
        (1358145273, 3431847134, 687875895, 3556988756, 4100256197),
        (2191608355, 1121904593, 558356047, 2687587613, 2715006907),
        (2402485621, 3965277055, 3547912281, 3632012931, 837133437),
        (4083688238, 3564660403, 300432284, 1847712185, 1673069850),
        (1267538828, 467031566, 1438284064, 1573096770, 1232797428),
        (904249014, 539582728, 2783067754, 1894945628, 1926406238),
        (1120891549, 2135796960, 2815683351, 2065787250, 3002024801),
        (1555842565, 1518145001, 3264470797, 3990502769, 2592402709),
        (2423950533, 2245779573, 1301538853, 1506649045, 1811157893),
        (3156726633, 4208663693, 1587507953, 1759615637, 2047711097),
    )

    assert tuple(
        tuple(test_arngr.jump(adv) for _ in range(5))
        for adv in (
            1,
            12,
            123,
            1234,
            12345,
            123456,
            1234567,
            12345678,
            123456789,
            1234567890,
        )
    ) == (
        (2408337579, 2286114914, 3692372301, 373632348, 1342820287),
        (833083521, 1996901395, 319942389, 1991661991, 2390497449),
        (1463924879, 1296486725, 3867925579, 2385217313, 2862158663),
        (61901586, 4036775025, 8797716, 3510745067, 876383782),
        (865666596, 3891926578, 3671604688, 3053322366, 407356860),
        (1239726346, 2819664360, 1082059734, 3001955924, 463308002),
        (2755731495, 4023013904, 88889453, 1085471054, 3011786755),
        (3600114047, 2811277883, 4207904311, 1523349875, 811558895),
        (4256414911, 1491133839, 3829654111, 863613743, 2606716927),
        (526180539, 3435687095, 3390347251, 445726319, 1776778283),
    )

    assert tuple(
        tuple(test_xdrngr.jump(adv) for _ in range(5))
        for adv in (
            1,
            12,
            123,
            1234,
            12345,
            123456,
            1234567,
            12345678,
            123456789,
            1234567890,
        )
    ) == (
        (3745948697, 399063950, 1307699815, 631669108, 1486693829),
        (152981939, 2779737521, 1030184255, 1885587421, 1213987083),
        (3623690997, 1167992303, 1817084025, 4038169875, 889670205),
        (827472734, 3176504515, 1666051708, 2242964697, 1519415658),
        (1293696236, 259292990, 529894624, 3090452050, 578396180),
        (2717315750, 1956965000, 3253420090, 1996431420, 3290319630),
        (3041341789, 2888755872, 212214087, 2608337154, 998720961),
        (3548564485, 1962150537, 2611987789, 2259353681, 3946774421),
        (2675693765, 868881909, 1410643749, 3297164373, 2441815429),
        (1216445449, 1787547341, 3266781649, 3421813013, 77469849),
    )


def test_lcrng64_next():
    """Test LCRNG64 next() calls for full seed"""
    test_bwrng = BWRNG(0x1234567887654321)
    test_bwrngr = BWRNGR(0x1234567887654321)

    assert tuple(test_bwrng.next() for _ in range(5)) == (
        16002821226169746376,
        2040015457476601003,
        2028497181719615802,
        16094432643137068197,
        16420378533051693276,
    )
    assert tuple(test_bwrngr.next() for _ in range(5)) == (
        2641392895229885446,
        6370139599609869703,
        9218825391134224756,
        13553550761165321565,
        11857309827725451154,
    )


def test_lcrng64_next_u16():
    """Test LCRNG64 next_u32() calls for 64-bit rand"""
    test_bwrng = BWRNG(0x1234567887654321)
    test_bwrngr = BWRNGR(0x1234567887654321)

    assert tuple(test_bwrng.next_u32() for _ in range(5)) == (
        3725947166,
        474978112,
        472296304,
        3747277111,
        3823167302,
    )
    assert tuple(test_bwrngr.next_u32() for _ in range(5)) == (
        614997207,
        1483163703,
        2146425049,
        3155681947,
        2760745079,
    )


def test_lcrng64_next_rand():
    """Test LCRNG64 next_rand() calls for bounded rand"""
    test_bwrng = BWRNG(0x1234567887654321)
    test_bwrngr = BWRNGR(0x1234567887654321)
    assert tuple(
        tuple(test_bwrng.next_rand(maximum) for _ in range(5))
        for maximum in (2, 5, 25, 100, 256)
    ) == (
        (1, 0, 0, 1, 1),
        (1, 1, 1, 0, 3),
        (10, 3, 8, 24, 23),
        (67, 16, 63, 83, 84),
        (123, 158, 75, 92, 208),
    )
    assert tuple(
        tuple(test_bwrngr.next_rand(maximum) for _ in range(5))
        for maximum in (2, 5, 25, 100, 256)
    ) == (
        (0, 0, 0, 1, 1),
        (2, 2, 1, 3, 4),
        (7, 18, 21, 16, 19),
        (63, 70, 17, 58, 55),
        (77, 72, 230, 10, 131),
    )


def test_lcrng64_jump():
    """Test LCRNG64 jump() calls for full seed"""
    test_bwrng = BWRNG(0x1234567887654321)
    test_bwrngr = BWRNGR(0x1234567887654321)
    assert tuple(
        tuple(test_bwrng.jump(adv) for _ in range(5))
        for adv in (
            1,
            12,
            123,
            1234,
            12345,
            123456,
            1234567,
            12345678,
            123456789,
            1234567890,
        )
    ) == (
        (
            16002821226169746376,
            2040015457476601003,
            2028497181719615802,
            16094432643137068197,
            16420378533051693276,
        ),
        (
            5090280609823288110,
            2854742739464299696,
            7932084128341255650,
            6626323601674754884,
            17314431422604262742,
        ),
        (
            8932657915544991916,
            3000185761518630962,
            15769072970957277544,
            14235162957003048398,
            15472936095090504420,
        ),
        (
            2970916893879399131,
            14320630354287920414,
            5600065023222879133,
            13997425193480191752,
            16708811053662938575,
        ),
        (
            7895965119874584877,
            1791461317186220795,
            5282272525162052281,
            6696915818268767207,
            14960799037456328197,
        ),
        (
            12683788349753160851,
            16090389273701105425,
            8090812255847055615,
            3556298622231376349,
            5626878743557236011,
        ),
        (
            4044592095396288964,
            4409224721310702841,
            10920442486307074138,
            18158677375287566135,
            3319231003970213792,
        ),
        (
            1816547551103995548,
            1483860766820069976,
            15412652462480187092,
            14825914923247874064,
            16683456896266158604,
        ),
        (
            6351658459697092060,
            263264831582066092,
            3386616449394311548,
            8064922848661870924,
            7868223879065443612,
        ),
        (
            11318794924193941720,
            18361761200577494356,
            12802980071449646736,
            4115839933324898444,
            17686800077037070152,
        ),
    )
    assert tuple(
        tuple(test_bwrngr.jump(adv) for _ in range(5))
        for adv in (
            1,
            12,
            123,
            1234,
            12345,
            123456,
            1234567,
            12345678,
            123456789,
            1234567890,
        )
    ) == (
        (
            2641392895229885446,
            6370139599609869703,
            9218825391134224756,
            13553550761165321565,
            11857309827725451154,
        ),
        (
            10864674503238331872,
            14033009489174613982,
            5304444438693569804,
            15858272904633211114,
            14310104608584057592,
        ),
        (
            5602589484985230658,
            8740612725479783740,
            5567226937753247078,
            10628815543376004160,
            18082707164951231562,
        ),
        (
            8401166712685949015,
            5063010862366413168,
            13923986727136724581,
            7569248279389695686,
            16202302842213167075,
        ),
        (
            15077184005216798421,
            2331873347330035255,
            98890430202282633,
            6480979383422450763,
            15478039337171636221,
        ),
        (
            1993700890945449503,
            12291911514933674801,
            1533599831395850163,
            997199748934332453,
            10442000189087460615,
        ),
        (
            426148467864766058,
            16382113900452327497,
            12316300906901619540,
            9466201500801380859,
            14302491951670639470,
        ),
        (
            8605420530269862866,
            6183254696759652086,
            4810298522237753562,
            3547165437524655486,
            1934288579521585378,
        ),
        (
            3291153389461101202,
            3351171253830082626,
            11469650778733523442,
            1369949790156509090,
            18402803675697494354,
        ),
        (
            8429132306121782390,
            15926931429132265050,
            13252614831004406526,
            7093818609526292066,
            3607687025514441862,
        ),
    )
