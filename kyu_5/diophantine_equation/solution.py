#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def sol_equa(n: int) -> list:
    """
    Finds all integers x, y (x >= 0, y >= 0)
    solutions of a diophantine equation of the form:
            x2 - 4 * y2 = n
    """
    result = list()

    if n % 2 == 0:
        for x in range(n//2, 0, -2):
            for y in range(x//2, -1, -1):

                if (x - 2*y) * (x + 2*y) == n:
                    result.append([x, y])
                    break
    else:
        for x in range(n//2 + 1, 0, -2):
            for y in range(x//2, -1, -1):

                if (x - 2 * y) * (x + 2 * y) == n:
                    result.append([x, y])
                    break

    return result
