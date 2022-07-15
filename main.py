from math import log2


# One step = one half-step (eg. C to Db)
# Is allowed to be negative and greater than 12
def note_to_12TET_steps(name: str) -> int:
    switch = {
        'C': 0,
        'D': 2,
        'E': 4,
        'F': 5,
        'G': 7,
        'A': 9,
        'B': 11
    }

    steps = switch.get(name[0])

    for c in name[1:]:
        if c == '#':
            steps += 1
        if c == 'b':
            steps -= 1

    return steps


# Determines how many factors of 3 a natural note is away from C
# Tuple is (factors of 2, factors of 3)
def note_name_to_factor(name: str) -> tuple[int, int]:
    switch = {
        'F': (2, -1),
        'C': (0, 0),
        'G': (-1, 1),
        'D': (-3, 2),
        'A': (-4, 3),
        'E': (-6, 4),
        'B': (-7, 5),
    }

    return switch.get(name[0])


def parse_factors(note_raw: str) -> dict[int, int]:
    factors = {
        2: 0,
        3: 0,
        5: 0,
        7: 0,
        11: 0,
        13: 0
    }

    # Tuple structure is as unpacked below: (factor, amount, correction2, correction3)
    # factor should always be a prime number and is the accidental's primary factor
    # amount is the exponent of the primary factor, will generally be 1 or -1
    # The two corrections are the factors of 2 and 3 respectively.
    # Adjacent accidentals are inverses.
    accidentals = {
        '#': (3, 7, -11, 0),    # Sharp and flat are pythagorean
        'b': (3, -7, 11, 0),    # '#' = 2187 / 2048

        '-': (5, 1, 4, -4),     # Syntonic comma
        '+': (5, -1, -4, 4),    # '-' = 80 / 81

        '7': (7, 1, -6, 2),     # Septimal comma
        'L': (7, -1, 6, -2),    # '7' = 63 / 64

        'u': (11, 1, -5, 1),    # Undecimal comma
        'd': (11, -1, 5, -1),   # 'u' = 33 / 32

        '3': (13, 1, -10, 4),   # Tridecimal comma
        'e': (13, -1, 10, -4),  # '3' = 1053 / 1024
    }

    # Accounts for the note name itself contributing factors
    factors[2], factors[3] = note_name_to_factor(note_raw[0])

    # Applies each accidental iteratively
    for c in note_raw[1:]:
        factor, amount, correction2, correction3 = accidentals.get(c)
        factors[factor] += amount
        factors[2] += correction2
        factors[3] += correction3

    return factors


def evaluate_factors(factors: dict[int, int]) -> float:
    total_factor = 1
    for factor, amount in factors.items():
        total_factor *= factor ** amount
    return total_factor


def main() -> None:
    note = input("Enter a Note: ")

    while note != "X":
        steps = note_to_12TET_steps(note)
        print(f"12TET Steps: {steps}")

        total_factor = evaluate_factors(parse_factors(note))
        print(f"Ratio: {total_factor}")
        total_cents = 12 * log2(total_factor)

        diff = 100 * (total_cents - steps)

        print(f"Cents difference: {diff}\n")

        note = input("Enter a Note: ")


if __name__ == '__main__':
    main()
