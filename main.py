from math import log2


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

    accidentals = {
        '#': (3, 7, -11, 0),
        'b': (3, -7, 11, 0),
        '-': (5, 1, 4, -4),
        '+': (5, -1, -4, 4),
        '7': (7, 1, -6, 2),
        'L': (7, -1, 6, -2),
        'u': (11, 1, -5, 1),
        'd': (11, -1, 5, -1)
    }

    factors[2], factors[3] = note_name_to_factor(note_raw[0])

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
