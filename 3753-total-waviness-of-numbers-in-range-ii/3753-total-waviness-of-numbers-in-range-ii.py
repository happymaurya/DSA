from functools import cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def g(x):
            if x <= 0:
                return 0

            sx = str(x)
            N = len(sx)

            @cache
            def f(index, zero, prefix, prev_digit, prev_prev_digit):
                if index == N:
                    return 0

                c = int(sx[index])
                total = 0

                if zero:
                    if prefix:
                        total += f(index + 1, True, False, None, None)

                        for d in range(1, c):
                            total += f(index + 1, False, False, d, None)

                        total += f(index + 1, False, True, c, None)

                    else:
                        total += f(index + 1, True, False, None, None)

                        for d in range(1, 10):
                            total += f(index + 1, False, False, d, None)

                else:
                    if prefix:

                        for d in range(0, c):
                            delta = 0

                            if prev_prev_digit is not None:
                                if prev_digit > prev_prev_digit and prev_digit > d:
                                    delta += 1

                                if prev_digit < prev_prev_digit and prev_digit < d:
                                    delta += 1

                            total += f(
                                index + 1,
                                False,
                                False,
                                d,
                                prev_digit,
                            )

                            total += delta * pow(10, N - index - 1)

                        delta = 0

                        if prev_prev_digit is not None:
                            if prev_digit > prev_prev_digit and prev_digit > c:
                                delta += 1

                            if prev_digit < prev_prev_digit and prev_digit < c:
                                delta += 1

                        total += f(
                            index + 1,
                            False,
                            True,
                            c,
                            prev_digit,
                        )

                        total += delta * (
                            int("0" + sx[index + 1:]) + 1
                        )

                    else:

                        for d in range(10):
                            delta = 0

                            if prev_prev_digit is not None:
                                if prev_digit > prev_prev_digit and prev_digit > d:
                                    delta += 1

                                if prev_digit < prev_prev_digit and prev_digit < d:
                                    delta += 1

                            total += f(
                                index + 1,
                                False,
                                False,
                                d,
                                prev_digit,
                            )

                            total += delta * pow(
                                10,
                                N - index - 1,
                            )

                return total

            return f(0, True, True, None, None)

        return g(num2) - g(num1 - 1)