repeated_count = int(input())

encoded_lines = []
for _ in range(repeated_count):
    line = input()
    pairs = []

    i = 0
    while i < len(line):
        repeated_count = 0
        c = line[i]
        while i < len(line) and line[i] == c:
            repeated_count += 1
            i += 1
        pairs.append(f"{repeated_count} {c}")


    encoded_lines.append(" ".join(pairs))


print("\n".join(encoded_lines))