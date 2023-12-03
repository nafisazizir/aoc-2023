def part_1(inputs):
    res = 0

    for line in inputs:
        first = 0
        last = 0

        for i in range(len(line)):
            if line[i].isdigit():
                first = int(line[i])
                break

        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit():
                last = int(line[i])
                break

        res += (first * 10) + (last)

    return res


def helper_2(line):
    pass


def part_2(inputs):
    res = 0

    num = [str(i) for i in range(10)]
    alpha = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    map = {}

    for i in range(len(num)):
        map[num[i]] = i
        map[alpha[i]] = i

    for line in inputs:
        first = 0
        first_idx = float("inf")
        for key in map.keys():
            if key in line:
                idx = line.index(key)
                if idx < first_idx:
                    first_idx = idx
                    first = map[key]

        last = 0
        last_idx = float("-inf")
        for key in map.keys():
            if key in line:
                idx = line.rindex(key)
                if idx > last_idx:
                    last_idx = idx
                    last = map[key]
        res += (first * 10) + (last)

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
    file_path = "./01/input.txt"
    input = read_file(file_path)

    p1 = part_1(input)
    print("Part 1 answer:", p1)

    p2 = part_2(input)
    print("Part 2 answer:", p2)


if __name__ == "__main__":
    main()
