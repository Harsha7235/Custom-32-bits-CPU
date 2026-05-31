def clean_lines(lines):
    output = []

    for line in lines:
        line = line.strip()

        if not line or line.startswith(";"):
            continue

        if ";" in line:
            line = line.split(";")[0].strip()

        output.append(line)

    return output