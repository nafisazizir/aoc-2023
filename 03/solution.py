import re


def part_1(input):
    res = 0

    for row in range(len(input)):
        for num in re.finditer("\d+", input[row]):
            col_start = num.start() - 1
            col_end = num.end() + 1
            row_start = row - 1
            row_end = row + 1
            is_found = False

            for i in range(row_start, row_end + 1):
                for j in range(col_start, col_end):
                    if i >= 0 and i < len(input) and j >= 0 and j < len(input[row]):
                        if (not input[i][j].isdigit()) and (input[i][j] != "."):
                            is_found = True
                            break

                if is_found:
                    res += int(num.group())
                    break

    return res


def part_2(input):
    res = 0
    map = {}

    for row in range(len(input)):
        for num in re.finditer("\d+", input[row]):
            col_start = num.start() - 1
            col_end = num.end() + 1
            row_start = row - 1
            row_end = row + 1
            is_found = False

            for i in range(row_start, row_end + 1):
                for j in range(col_start, col_end):
                    if i >= 0 and i < len(input) and j >= 0 and j < len(input[row]):
                        if input[i][j] == "*":
                            gears = map.get((i, j), [])
                            gears.append(int(num.group()))
                            map[(i, j)] = gears

                            is_found = True
                            break

                if is_found:
                    break

    for val in map.values():
        if len(val) == 2:
            res += val[0] * val[-1]

    return res


def read_file(file_path):
    input = []

    try:
        with open(file_path, "r") as file:
            for line in file:
                input.append(line.strip())

            return input

    except FileNotFoundError:
        print(f"File not found: {file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    file_path = "./03/input.txt"
    input = read_file(file_path)

    p1 = part_1(input)
    print("Part 1 answer:", p1)

    p2 = part_2(input)
    print("Part 2 answer:", p2)


if __name__ == "__main__":
    main()
