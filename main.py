from math import log2, gcd


# Multiplies, then reduces, two fractions
def multiply(frac0: tuple[int, int], frac1: tuple[int, int]) -> tuple[int, int]:
    result = frac0[0] * frac1[0], frac0[1] * frac1[1]
    factor = gcd(result[0], result[1])
    return result[0] // factor, result[1] // factor


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


# Assigns a fraction to each note name as a ratio back to C
def note_name_to_factor(name: str) -> tuple[int, int]:
    switch = {
        'F': (4, 3),
        'C': (1, 1),
        'G': (3, 2),
        'D': (9, 8),
        'A': (27, 16),
        'E': (81, 64),
        'B': (243, 128),
    }

    return switch.get(name[0])


def parse_input(note_raw: str) -> tuple[int, int]:
    # Starts on the Pythagorean note name
    note_fraction = note_name_to_factor(note_raw[0])

    # Fractional ratios for the different available accidentals
    # Adjacent accidentals are inverses of each other
    accidentals = {
        '#': (2187, 2048),  # Sharp and flat are pythagorean
        'b': (2048, 2187),  # '#' = 3^7 / 2^11

        '-': (80, 81),      # Syntonic comma, factor of 5
        '+': (81, 80),      # '-' = 5 * 2^4 / 3^4

        '7': (63, 64),      # Septimal comma, factor of 7
        'L': (64, 63),      # '7' = 7 * 3^2 / 2^6

        'u': (33, 32),      # Undecimal comma, factor of 11
        'd': (32, 33),      # 'u' = 11 * 3 / 2^5

        '3': (1053, 1024),  # Tridecimal comma, factor of 13
        'e': (1024, 1053),  # '3' = 13 * 3^4 / 2^10
    }

    # Applies each accidental iteratively
    for c in note_raw[1:]:
        note_fraction = multiply(note_fraction, accidentals.get(c))

    return note_fraction


def main() -> None:
    note = input("Enter a Note: ")

    while note != "X":
        steps = note_to_12TET_steps(note)

        total_factor = parse_input(note)
        print(f"Ratio to C: {total_factor[0]} / {total_factor[1]}")
        total_cents = 12 * log2(total_factor[0] / total_factor[1])

        diff = 100 * (total_cents - steps)

        print(f"Cents difference: {diff}\n")

        note = input("Enter a Note: ")


if __name__ == '__main__':
    main()
