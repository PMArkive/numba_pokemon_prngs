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
        (3217940315, 2989472983, 1881563539, 3165858191, 2153296075),
        (884291604, 1663541777, 2082535634, 1887281063, 2025557024),
        (3011737306, 1905980836, 3245851390, 262176104, 3955640162),
        (3287845061, 3956680460, 3808542695, 2116860230, 1948537945),
        (3476392857, 4053402329, 2324806169, 2304553305, 490399897),
        (1341700934, 1149868455, 2488120972, 4194967557, 4183583842),
        (2393760392, 3229015614, 3240924420, 4267819098, 2417425856),
        (3312129815, 2870499730, 313239201, 2214150644, 110078075),
        (3277903853, 4242316335, 3551096257, 2703579427, 796073685),
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
        (3217940315, 2989472983, 1881563539, 3165858191, 2153296075),
        (884291604, 1663541777, 2082535634, 1887281063, 2025557024),
        (3011737306, 1905980836, 3245851390, 262176104, 3955640162),
        (3287845061, 3956680460, 3808542695, 2116860230, 1948537945),
        (3476392857, 4053402329, 2324806169, 2304553305, 490399897),
        (1341700934, 1149868455, 2488120972, 4194967557, 4183583842),
        (2393760392, 3229015614, 3240924420, 4267819098, 2417425856),
        (3312129815, 2870499730, 313239201, 2214150644, 110078075),
        (3277903853, 4242316335, 3551096257, 2703579427, 796073685),
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
        (2059994633, 1837952173, 3282172049, 832728501, 2503987225),
        (3217108124, 3588603859, 3821681646, 1624086109, 3474377424),
        (1072799846, 3763464972, 629050434, 2258979208, 403319902),
        (392782015, 1464228516, 2553020445, 2707427194, 2534113355),
        (3654754059, 2397044171, 1558584459, 715750219, 518658571),
        (2148380026, 2903157853, 2374249252, 1278080895, 3745085278),
        (4030584936, 4261643522, 4218264492, 2253422310, 2044228912),
        (3709996141, 1783775022, 2265963203, 264438460, 2230246889),
        (2174380631, 863304725, 2815105699, 1214955905, 412631087),
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
        (1470939563, 2904402183, 3123210915, 3194643071, 804990107),
        (2031465524, 3652704753, 1568712034, 3799234647, 162965472),
        (2496165162, 2188128068, 1723461806, 207439848, 3748517746),
        (816231621, 2785352812, 1613083287, 802858166, 2598231161),
        (1424149945, 2827353849, 889679929, 3651608953, 3047494329),
        (1244206774, 3099017815, 2524372972, 497743365, 3430077554),
        (758870024, 132227566, 2840764324, 2979443370, 909285504),
        (377957703, 1912586274, 2943181569, 3122866964, 2020829131),
        (4036214061, 2494838303, 942134049, 438417587, 3271511893),
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
        (3934733737, 2187981, 2138623281, 535709909, 1847712185),
        (1707027228, 1187219891, 801154478, 3141081725, 1217466832),
        (3478750502, 4280455052, 1519288962, 4194243464, 1000389662),
        (3553287711, 2847739428, 456760381, 941914298, 1504392491),
        (584125419, 3462144683, 2064415083, 2275545131, 2463950571),
        (1388369594, 1159983229, 3402116772, 1719053535, 2838816542),
        (98119272, 3292689218, 439116844, 660108198, 2564323376),
        (703748749, 183054574, 3696835235, 3832780092, 1664289161),
        (1914160823, 723243829, 3572754051, 746105889, 2007475087),
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
        (3934733737, 2187981, 2138623281, 535709909, 1847712185),
        (1707027228, 1187219891, 801154478, 3141081725, 1217466832),
        (3478750502, 4280455052, 1519288962, 4194243464, 1000389662),
        (3553287711, 2847739428, 456760381, 941914298, 1504392491),
        (584125419, 3462144683, 2064415083, 2275545131, 2463950571),
        (1388369594, 1159983229, 3402116772, 1719053535, 2838816542),
        (98119272, 3292689218, 439116844, 660108198, 2564323376),
        (703748749, 183054574, 3696835235, 3832780092, 1664289161),
        (1914160823, 723243829, 3572754051, 746105889, 2007475087),
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
        (3525561467, 975277175, 1518971827, 1182795311, 3510745067),
        (3519573652, 2568634737, 1679765650, 651636039, 229094176),
        (390035866, 1597805092, 279619390, 2111686504, 667419938),
        (2712696741, 1063768716, 1010378119, 3365830790, 520300217),
        (1136449017, 4108436793, 2578576505, 3647824825, 2605978361),
        (4149035654, 2251745095, 525775372, 2976679653, 4151904802),
        (3392977032, 4231477886, 1510856068, 227988250, 2024661184),
        (4066279095, 863607122, 1479486465, 259034228, 834789787),
        (1801694669, 887936207, 779484961, 3655919939, 3277423541),
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
        (3465855049, 1141413645, 3016338961, 2563590485, 2242964697),
        (3145044476, 1731344323, 2699889118, 1097068605, 3749552656),
        (1804372374, 727093484, 1413994898, 528644360, 1769396430),
        (2017014159, 1553568708, 2478534653, 182409226, 2839318523),
        (1530401979, 1384372603, 1977605691, 3960218363, 466134971),
        (1419888138, 4096456253, 3769417796, 3270696527, 3701861326),
        (2285228264, 2968536146, 1953006732, 3283559446, 661105008),
        (977960141, 4101597982, 1473467955, 276397852, 2661835561),
        (4178531815, 823946933, 1990761747, 1655985281, 1823698047),
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


def test_lcrng64_next_u32():
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
            2952680919966118040,
            15482879799003017492,
            15918991341253301840,
            13432280392932867148,
            13997425193480191752,
        ),
        (
            2834420249872142365,
            15396525225438894622,
            11553731727932019803,
            2050655070523452644,
            9705967490120080777,
        ),
        (
            15051046580031164323,
            16061200406499065133,
            16514475758798409895,
            1766227417220706449,
            3700961937258880875,
        ),
        (
            9305589310236415634,
            11296007194735646293,
            14572090361080656164,
            15519740244018856751,
            7364370606377408870,
        ),
        (
            1221997400390291622,
            13776399561554020326,
            6076273224782610214,
            5545534153401529958,
            5563785253732036006,
        ),
        (
            6836853389648876847,
            8034639571703432932,
            8263589254808898005,
            5295211214637225426,
            15123490579893660779,
        ),
        (
            7083129394886559921,
            9040573140935884263,
            1079923295994093965,
            15773485178116171043,
            4232055513966360105,
        ),
        (
            14809851356512464724,
            4334561893928930075,
            7737449239820308142,
            18160188915248036605,
            7660212805292345272,
        ),
        (
            2870030792215668154,
            5118572541699903724,
            14671201821043113422,
            13179403563742563552,
            11198964096877374114,
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
            13007287705257166518,
            4968350959549326490,
            10605539870655823166,
            2131965556264539298,
            7569248279389695686,
        ),
        (
            11352778351261555173,
            7746639895509042288,
            15939327349344483031,
            14519608158806340170,
            13528639294474477497,
        ),
        (
            8185013964881000975,
            10108458850261981909,
            14709910204702813067,
            12518400974384419249,
            6769641592313499335,
        ),
        (
            13899140821661972956,
            8841026402049167789,
            3695793284911979530,
            11975551762905612419,
            7532151235728584040,
        ),
        (
            2083092400858241064,
            1095295107007038184,
            15153242916020268456,
            11844347680691935336,
            812378222475985704,
        ),
        (
            11699477786092834435,
            2639770092101896266,
            14923089274833825325,
            10284573593868502172,
            9675240087455003079,
        ),
        (
            16042249122471901585,
            7579791363401847371,
            6175040640602104437,
            4879117100365130895,
            9836584107060227865,
        ),
        (
            6142945447607690330,
            16614305369146520599,
            15009198128235853408,
            9983924943922223877,
            6221009122616208022,
        ),
        (
            5900747234915404020,
            9630074591514987266,
            15833019308693851200,
            4210509196466959406,
            6898835439005849164,
        ),
    )
