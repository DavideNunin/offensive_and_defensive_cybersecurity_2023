#! /usr/bin/python3
import z3
def check_flag(guess):
    if (guess[0xb] * -0x19 +
    guess[8] * 0x31 + guess[10] * 0xbb + -0x9c2a + guess[1] * 0x39 + guess[2] * 3 +
    guess[0x16] * 0xd7 + guess[9] * -0xbd + guess[0xc] * -0x47 + guess[0xd] * 0xb7 +
    guess[0xf] * -0x9b + guess[3] * 0x73 + guess[0x13] * -0x95 + guess[0xe] * 0xc6 +
    guess[4] * 0x9a + guess[0x11] * -0x66 + guess[0x10] * 0x7c + guess[0x12] * 0xb9 +
    guess[6] * -0xaa + guess[5] * -0x6a + guess[0x15] * 0xe1 + guess[0x14] * -0xa6 +
    guess[7] * -0xb5 + guess[0] * -0xb7 == 0):
        if (guess[0x15] * -0x55 +
        guess[0xe] * -0xe5 +
        guess[8] * -0xae + guess[6] * -0x58 + guess[0x14] * 0x7d + guess[1] * -0x3c +
        guess[0xf] * 0xe0 + guess[10] * 0xfc + guess[2] * -0x5e + guess[0x12] * -0xe0 +
        guess[5] * 0xee + guess[0x10] * 0xe7 + guess[7] * -0x61 + guess[0xb] * -0x89 +
        guess[4] * -0x80 + guess[0] * -0xfd + guess[0xc] * -0x9e + 0x9a2e +
        guess[0x16] * 2 + guess[0x16] * -0x10 + guess[0x13] * -0x11 + guess[0x11] * 0x30 +
        guess[0xd] * 0x83 + guess[9] * -0xde + guess[3] * 0xe2 == 0):
            if (guess[0x10] * -0x39 + guess[0x16] * 0xc6 + guess[0x15] * -0x6c + guess[9] * 0xd4 + guess[0xf] * -0xe2 + guess[0xd] * 0xc5 +
            guess[0x14] * 0x91 + guess[2] * 0x84 + guess[1] * 0x32 + guess[0xe] * 0x86 +
            -0x3124d + guess[5] * 0xd2 + guess[0x11] * 0xea + guess[0xb] * 0x1b +
            guess[0x12] * 0x97 + guess[3] * 0xf0 + guess[4] * -0x8a + guess[0xc] * 0x95 +
            guess[0x13] * 0x9f + guess[7] * -0x29 + guess[8] * 0xb3 + guess[0] * -0x31 +
            guess[10] * 0xd1 + guess[6] * 0x32 == 0):
                if (guess[7] * 0x5f + guess[10] * 0x60 + guess[0x14] * 0x8d + guess[0xc] * 0xab + guess[6] * -0x1a + guess[0xe] * 0xcb +
                guess[2] * 0x57 + guess[0x13] * -0x8d + guess[0x16] * -0xba + guess[0xf] * 0xa9
                + guess[0x10] * -0x14 + guess[5] * 0x52 + guess[0x11] * -0x23 + guess[1] * -0x68
                + guess[0x15] * 199 + guess[0x12] * 0x57 + guess[0xd] * 0xeb + guess[8] * -0xa8
                + guess[9] * 0x85 + guess[0] * -0x62 + -0x20c1e + guess[4] * 0xaf +
                guess[3] * -0x26 + guess[0xb] * 0xfb == 0):
                    if (guess[0xb] * 0x23 + guess[3] * -0x80 + guess[0x12] * 0xd0 + guess[0xd] * 0x8a + -0x1b8ed +
                    guess[0] * -0x51 + guess[2] * 0x8c + guess[1] * 4 + guess[0x13] * 0x86 +
                    guess[4] * 0xf0 + guess[5] * -0xc4 + guess[9] * -0x55 + guess[0x14] * 0xd8 +
                    guess[0x11] * -0xb5 + guess[0xe] * -0x14 + guess[7] * 0xea + guess[10] * -0xc3
                    + guess[8] * 0xeb + guess[0xf] * 0xba + guess[0x10] * -0xf5 +
                    guess[0x15] * 0xe7 + guess[0xc] * 0x97 + guess[0x16] * 0x97 + guess[6] * -0x4e
                    == 0) :
                        if (guess[0xc] * 0xd6 + guess[0x11] * -0x80 +
                        guess[3] * 0x21 + guess[0xf] * -0xe8 + guess[10] * 0xd + guess[4] * -0x7b +
                        guess[0x12] * 0x5a + guess[0x13] * 0xda + guess[6] * -0x66 +
                        guess[1] * -0x98 + guess[8] * 0x23 + guess[0x14] * 0x16 +
                        guess[0x15] * -0x89 + guess[9] * -0xba + guess[7] * 0x53 + guess[0xb] * 0x6e
                        + guess[2] * 0x8e + guess[5] * -0xe5 + guess[0xd] * 0xc5 + guess[0x10] * -7
                        + guess[0x16] * -0xee + guess[0] * 0xed + guess[0xe] * 0xab + -0x3da5 == 0):
                            if (guess[1] * 0xa8 + guess[7] * -0xa6 +  guess[6] * 0x7a + guess[2] * -0x50 + guess[0x12] * 0xdd +
                            guess[4] * -0xa7 + guess[5] * 0x8b + guess[0xc] * -0x26 +
                            guess[8] * -0x8c + guess[0x10] * -0x9f + guess[10] * -0xc6 -
                            guess[0x16]+0x100 *guess[17]+0x10000*guess[18]+0x1000000*guess[19] + guess[0xe] * -0x35 + guess[9] * 0xe +
                            guess[0x14] * -0x6f + guess[0xb] * 0x91 + 0xb2a6 + guess[0x11] * -0x8d +
                            guess[0xd] * -0xd + guess[3] * 0x39 + guess[0] * -0xcc + guess[0xf] * -0x45
                            + guess[0x13] * 0xe9 + guess[0x15] * -0x6a == 0) :
                                if (guess[0xe] * 0xe +
                                guess[0x15] * 0xeb +
                                guess[10] * 0x12 + guess[0x13] * 0xa3 + guess[3] * 0xa5 +
                                guess[4] * 0xb3 + guess[0xf] * -0x10 + guess[0xc] * -0x4d +
                                guess[2] * -0x65 + guess[0x10] * 0xc1 + guess[0x16] * 0x43 + -0x20fdc +
                                guess[0x11] * 0xeb + guess[0x14] * 0xb4 + guess[5] * 0x33 +
                                guess[0xd] * -0xe7 + guess[9] * 0x7a + guess[0] * -0x42 + guess[1] * 0xca
                                + guess[7] * 0xca + guess[8] * 0x35 + guess[0xb] * 0x4e +
                                guess[0x12] * 0x4d + guess[6] * -0xbe == 0) :
                                    if (guess[0x11] * -199 +
                                    guess[10] * -0x4e +
                                    guess[5] * -0xd8 + guess[0xd] * -0x17 + guess[7] * 0xc5 +
                                    guess[0xe] * 0x43 + guess[0x10] * 0xc4 + guess[0xf] * 0xaa + 0x4867 +
                                    guess[1] * -0xf5 + guess[3] * -0xa1 + guess[9] * 0x55 +
                                    guess[0x15] * 0x67 + guess[0xc] * -0x4e + guess[0x13] * 8 +
                                    guess[0] * -0xd3 + guess[0x16] * -0xb2 + guess[8] * 0x2d +
                                    guess[0xb] * -0xf + guess[4] * 0xd1 + guess[6] * 0xf2 +
                                    guess[2] * 0xf0 + guess[0x14] * -0x5b + guess[0x12] * 0x47 == 0) :
                                        if (guess[0x15] * 0xed +
                                        guess[0xe] * 0x5b +
                                        guess[4] * -0xf + guess[9] * -0xfd + guess[6] * 99 +
                                        guess[2] * -0xd1 + guess[0] * 0xf7 + guess[0x13] * 0xc3 +
                                        guess[0xf] * -0x6f + guess[8] * 0xca + guess[0x10] * 0x4a +
                                        guess[0x14] * 0xf9 + guess[3] * 0xd3 + -0x130f0 + guess[0x11] * -0xfc
                                        + guess[0x16] * -0xda + guess[5] * 0x56 + guess[10] * 0x3b +
                                        guess[0xb] * 0x87 + guess[0xd] * -0x3a + guess[0xc] * -0xa9 +
                                        guess[0x12] * 0xbb + guess[1] * 0xb4 + guess[7] * 0x8f == 0) :
                                            if (guess[0xf] * -0x20 +
                                            guess[0x16] * -0x22 +
                                            guess[0x15] * -0x7b + guess[0xb] * -99 + guess[0x13] * 0x86 +
                                            guess[0xe] * 0x9c + guess[5] * 0x89 + guess[0xd] * 0xe3 +
                                            guess[0x10] * -0x7c + guess[3] * -0x9c + 0x8354 + guess[0] * -0x45 +
                                            guess[1] * -0x51 + guess[0x11] * -0x7d + guess[7] * -0xa7 +
                                            guess[6] * 0xaf + guess[8] * -0xcf + guess[0x12] * -0xbf +
                                            guess[0x14] * 0x22 + guess[4] * -0x3a + guess[10] * -0x47 +
                                            guess[0xc] * -0x5d + guess[2] * 0xfe + guess[9] * 0xc9 == 0) :
                                                if (guess[10] * 0xcc +
                                                guess[0x13] * 0x33 +
                                                guess[2] * -0x69 + guess[3] * -0xa3 + guess[0x10] * 0x60 +
                                                guess[5] * 0xea + guess[0xb] * -0xb5 + guess[0xc] * 0x2a +
                                                guess[0x14] * 0xf1 + guess[6] * 0xb1 + guess[0xe] * -0x14 +
                                                guess[9] * 0x86 + guess[0x12] * -0x65 + -0x53c7 + guess[1] * -0x48
                                                + guess[4] * -0x30 + guess[0xf] * -0xde + guess[0x15] * -0x3e +
                                                guess[0] * 0x57 + guess[8] * -0x37 + guess[0xd] * 0x5a +
                                                guess[0x16] * 0x6c + guess[0x11] * 0xd6 + guess[7] * -0xe2 == 0) :
                                                    if (guess[4] * 0x39 +
                                                    guess[8] * 0x23 +
                                                    guess[3] * -0x4e + guess[0xb] * -0x99 + guess[0xe] * 0x47 +
                                                    guess[6] * -0xa7 + guess[9] * 0x74 + guess[0x14] * 2 + 0x2d4f +
                                                    guess[0x12] * -0x50 + guess[0xd] * -0xb8 + guess[0x16] * -0x4f +
                                                    guess[0x10] * -0x31 + guess[0xf] * 0xf2 + guess[0] * -7 +
                                                    guess[0xc] * -0xa4 + guess[0x11] * 0xc4 + guess[7] * -0x28 +
                                                    guess[0x13] * -0xb8 + guess[5] * 0xf0 + guess[1] * 0x1a +
                                                    guess[2] * -0x84 + guess[10] * 0x8d + guess[0x15] * -2 == 0):
                                                        if (guess[4] * 0xa8 + guess[7] * 0xe1 +
                                                        guess[0x12] * -0x1a + guess[2] * -0x3d + guess[0xf] * -0xc9 +
                                                        guess[0x16] * -0x7f + guess[0] * 0x2c + 0xeb6 +
                                                        guess[0xb] * 0x71 + guess[0x13] * -0x8f + guess[0x10] * -0xdd
                                                        + guess[10] * -0xe1 + guess[6] * -0xbb + guess[0x14] * 0x48 +
                                                        guess[0xe] * -0xb6 + guess[0xd] * 0xdc + guess[3] * 0xf2 +
                                                        guess[0x15] * -0x88 + guess[0xc] * -0x2e + guess[0x11] * 3 +
                                                        guess[5] * 0xb8 + guess[9] * 0x8c + guess[8] * -0x77 +
                                                        guess[1]+0x100 * guess[2]+0x10000*guess[3]+0x1000000*guess[4] + guess[1] * -8 == 0) :
                                                            if (guess[3] * 0xad +
                                                            guess[2] * 0x82 + guess[0xf] * 0xa7 + guess[7] * 0xd0 +
                                                            guess[0x14] * -0x4f + guess[0xc] * -0x91 +
                                                            guess[0x11] * -0x5a + guess[0x13] * -0x100 +
                                                            guess[0x10] * 0x27 + guess[8] * 0xec + guess[0xb] * 0x3c +
                                                            guess[6] * -0x4a + guess[5] * -0x1b + guess[4] * -0x47 +
                                                            guess[9] * 0x8c + guess[0] * -0x8e + guess[0x16] * 0x65 +
                                                            guess[10] * -0xb9 + guess[0x15] * 0x74 + guess[0xd] * -0x86
                                                            + guess[0xe] * 0x9e + guess[1] * 0xbb + guess[0x12] * -0x48
                                                            == 0x6469) :
                                                                if (guess[0x12] * -0xc0 +
                                                                guess[4] * 0xe7 +
                                                                guess[5] * 9 + guess[8] * 0xa4 + guess[0x15] * 0xf6 +
                                                                guess[2] * 0xd9 + guess[0x11] * 0x57 + guess[0xc] * -0x88
                                                                + guess[3] * 0xdd + guess[0x10] * -0x8a + guess[6] * -0x97
                                                                + guess[1] * 0x57 + guess[0x13] * 0xe2 + guess[7] * 0x61 +
                                                                guess[0x16] * 0x6c + guess[0x14] * -0xd0 + -0x1e27d +
                                                                guess[0xf] * 0x46 + guess[9] * 0xf0 + guess[0] * 0x5a +
                                                                guess[0xd] * -0x52 + guess[10] * 0xb9 + guess[0xb] * 0xb4
                                                                + guess[0xe] * -0xf8 == 0) :
                                                                    if (guess[3] * 0xc +
                                                                    guess[0xe] * 0x85 +
                                                                    guess[6] * -0xa9 + guess[0xb] * -0x36 +
                                                                    guess[0x13] * -0x93 + guess[8] * -0x17 + guess[5] * 6 +
                                                                    guess[0x14] * 0x99 + guess[0x10] * 0xd4 +
                                                                    guess[0xf] * 0xf2 + guess[0xc] * 0xb5 +
                                                                    guess[10] * -0xb8 + guess[2] * -0x35 + guess[9] * -0x98
                                                                    + guess[0xd] * -0xe5 + -0x65d + guess[4] * 0x3f +
                                                                    guess[0] * 0x9d + guess[1] * 0xe + guess[0x11] * 0xe +
                                                                    guess[0x16] * -0xdb + guess[0x12] * 0x61 +
                                                                    guess[7] * 0x1b + guess[0x15] * -0x97 == 0):
                                                                        if (guess[9] * 0xf6 +
                                                                        guess[4] * -0x28 + 0x11400 + guess[0xc] * -0xb2 +
                                                                        guess[10] * -0xe2 + guess[0xd] * -0x90 +
                                                                        guess[0x16] * 0x62 + guess[6] * 0xd3 +
                                                                        guess[0x11] * -0x7a + guess[0xb] * -0xad +
                                                                        guess[8] * 0x1d + guess[0x14] * 0x48 +
                                                                        guess[2] * -0x17 + guess[7] * -0x34 + guess[3] * 0x9b
                                                                        + guess[0x13] * -0x12 + guess[0xf] * 0x7a +
                                                                        guess[0x15] * -0x83 + guess[0x10] * 0xac +
                                                                        guess[5] * -0xe3 + guess[0xe] * -0xb5 +
                                                                        guess[0x12] * -0x8f + guess[0] * 0xfc == 0):
                                                                            if (guess[0x12] * -0x32 +
                                                                            guess[0x13] * 0x50 +
                                                                            guess[4] * -0x4f + guess[0xb] * 0x4f + guess[0] * 0x33
                                                                            + guess[3] * -0xab + guess[8] * -0x98 +
                                                                            guess[0x15] * -0xcb + guess[0x16] * 0x6a +
                                                                            guess[9] * 0x95 + 0xfde0 + guess[2] * -0xc1 +
                                                                            guess[6] * -0x99 + guess[5] * -0x40 +
                                                                            guess[0x14] * -0x72 + guess[0xf] * -0xf9 +
                                                                            guess[0xc] * -0xfb + guess[1] * 0xdc +
                                                                            guess[0xe] * -0xf9 + guess[0x11] * 0x17 +
                                                                            guess[0x10] * -0x14 + guess[7] * 0x7a +
                                                                            guess[0xd] * 0x3d + guess[10] * 0xdd == 0):
                                                                                if (guess[0x16] * -0xfd +
                                                                                guess[4] * 0x85 +
                                                                                guess[0xb] * -0x29 + guess[0x11] * 0x2a +
                                                                                guess[0] * 0xe3 + guess[1] * -0x84 + guess[9] * 0xad
                                                                                + guess[6] * 0x4c + guess[0x14] * 0xf4 +
                                                                                guess[5] * -0x2d + -0x21cf + guess[7] * -0xc6 +
                                                                                guess[0xe] * 0x4c + guess[0x15] * -0x5a +
                                                                                guess[3] * 0x65 + guess[0xf] * -0xfe +
                                                                                guess[8] * -0x29 + guess[2] * -0x17 +
                                                                                guess[0x13] * 0x8a + guess[0xd] * -0x78 +
                                                                                guess[0x10] * 0x6d + guess[0x12] * -0x30 +
                                                                                guess[10] * 0xa1 + guess[0xc] * 0x8a == 0):
                                                                                    if (guess[10] * -0xb +
                                                                                    guess[0xe] * 0x54 +
                                                                                    guess[0x14] * 0x5b + guess[2] * 0xda +
                                                                                    guess[3] * -0x8e + guess[0x13] * 0x4c +
                                                                                    guess[0x15] * -0xec + guess[0x10] * -0x81 +
                                                                                    guess[9] * -0x5c + guess[0x16] * -0xdd +
                                                                                    guess[4] * 0xac + guess[0xf] * 0xe5 +
                                                                                    guess[7] * -0xf9 + guess[8] * -0x32 +
                                                                                    guess[5] * 0xbd + guess[0x12] * -0xbd +
                                                                                    guess[0xd] * -100 + guess[0xb] * 0x5d +
                                                                                    guess[1] * 0x8b + guess[0xc] * 0x89 +
                                                                                    guess[0] * -0x1e + guess[0x11] * -0x7c + -0x9bf +
                                                                                    guess[6] * -0x1e == 0):
                                                                                        if (guess[0xb] * -0xe2 +
                                                                                        guess[6] * -0x4b +
                                                                                        guess[0x15] * -10 + guess[8] * 0x33 +
                                                                                        guess[0x16] * 0x72 + guess[0x14] * -0x80 +
                                                                                        guess[5] * -0xdf + guess[7] * 0xf9 +
                                                                                        guess[4] * 0x11 + guess[0x11] * -0xc1 +
                                                                                        guess[0] * 0x74 + guess[0x12] * 0xf6 +
                                                                                        guess[0x10] * 0xdc + guess[0xf] * 0x65 +
                                                                                        guess[0xe] * 0xb2 + guess[0xc] * -0x42 +
                                                                                        guess[10] * -0x42 + guess[2] * 0x24 +
                                                                                        guess[9] * -0xd4 + guess[0x13] * 0x73 +
                                                                                        guess[0xd] * -0x86 + guess[3] * 0xd7 + -0xe3f6 +
                                                                                        guess[1] * 0x76 == 0):
                                                                                            if (guess[0x10] * -0x9c +
                                                                                            guess[2] * 0x67 +
                                                                                            guess[0xc] * -0x23 + guess[8] * -0x48 +
                                                                                            guess[6] * -0xd7 + guess[7] * -0x84 +
                                                                                            guess[1] * 10 + guess[0xe] * -0xd7 +
                                                                                            guess[0xb] * 0x62 + guess[0xf] * -0x51 +
                                                                                            guess[0] * 0xbc + guess[0x16] * -0x4c + 0xd3bb +
                                                                                            guess[0x13] * -0x98 + guess[0xd] * -0x53 +
                                                                                            guess[0x11] * -0x77 + guess[0x15] * -0x6c +
                                                                                            guess[3] * 0x74 + guess[0x14] * 0x38 +
                                                                                            guess[5] * 0x46 + guess[9] * -0x9c +
                                                                                            guess[4] * 0xdb + guess[10] * -0x76 +
                                                                                            guess[0x12] * 0x2e == 0):
                                                                                                    var = 0
                                                                                            else:
                                                                                                var = 0x17
                                                                                        else:
                                                                                            var = 0x16
                                                                                    else:
                                                                                        var = 0x15
                                                                                else:
                                                                                    var = 0x14
                                                                            else:
                                                                                var = 0x13
                                                                        else:
                                                                            var = 0x12
                                                                    else:
                                                                        var = 0x11
                                                                else:
                                                                    var = 0x10
                                                            else:
                                                                var = 0xf
                                                        else:
                                                            var = 0xe
                                                    else:
                                                        var = 0xd
                                                else:
                                                    var = 0xc
                                            else:
                                                var = 0xb
                                        else:
                                            var = 10
                                    else:
                                        var = 9
                                else:
                                    var = 8
                            else:
                                var = 7
                        else:
                            var = 6
                    else:
                        var = 5
                else:
                    var = 4
            else:
                var = 3
        else:
            var = 2
    else:
        var = 1

    return var

len_input= 0x17
solver = z3.Solver()
inp = [z3.BitVec('char_{i}',8) for i in range(len_input)]
var = z3.Int('var')
solver.add(check_flag(inp) == 0)
print(solver.check())




