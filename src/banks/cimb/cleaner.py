def clean_lines(text):
    lines = []

    for line in text.splitlines():
        line = line.strip()

        if line:
            lines.append(line)

    return lines