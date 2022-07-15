# XenharmonicCents
This is a simple tool for quickly figuring out just-intonated tunings through a command-line interface.

To use: open it through a terminal and type in a note when prompted.
Using only standard note names alongside the standard "#" and "b" will yield 3-limit, or Pythagorean, tuning, supporting multiple flats/sharps.
The rest of the accidentals take inspiration from Ben Johnston's notation, and are as follows, where the first accidental is overtonal and the second is undertonal:
- "-" and "+" for the syntonic comma (80 / 81)
- "7" and "L" for the septimal comma (63 / 64)
- "u" and "d" for the undecimal comma (33 / 32)
- "3" and "e" for the tridecimal comma (1053 / 1024)

Type the note's letter name first (must be capital), then the accidentals in any order. The program will return the difference between the note's 12TET version and the just intonated version.
This is centered on C, meaning C in this just intonated tuning will be the same as C in 12 TET, or ~523.251 Hz for C5.
