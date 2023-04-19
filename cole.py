for d1 in range(1, 7):
    for d2 in range(1, 7):
        for d3 in range(1, 7):
            for d4 in range(1, 7):
                for d5 in range(1, 7):
                    for d6 in range(1, 7):
                        for d7 in range(1, 7):
                            for d8 in range(1, 7):
                                if (d1 + d3 + d5 + d7 == 12 and
                                    d2 + d4 + d6 + d8 == 11 and
                                    d2 * d3 * d7 == 24 and
                                    d1 * d2 * d3 * d5 == 60 and
                                    d7 - d2 + d3 - d4 == 0 and
                                    d6 + d1 + d8 == 10 and d8 > 3):
                                        print("Flag: ", d1, d2, d3, d4, d5, d6, d7, d8)