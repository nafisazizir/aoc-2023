def part_1(input):
    res = 1
    t = [int(i.strip()) for i in input[0].split(": ")[-1].split()]
    d = [int(i.strip()) for i in input[1].split(": ")[-1].split()]

    for i in range(len(t)):
        ways = 0
        for j in range(t[i]):
            if j * (t[i] - j) > d[i]:
                ways += 1

        res *= ways

    return res


def part_2(input):
    res = 1
    t = [int(input[0].split(": ")[-1].replace(" ", ""))]
    d = [int(input[1].split(": ")[-1].replace(" ", ""))]

    for i in range(len(t)):
        ways = 0
        for j in range(t[i]):
            if j * (t[i] - j) > d[i]:
                ways += 1

        res *= ways

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
    file_path = "./06/input.txt"
    input = read_file(file_path)

    p1 = part_1(input)
    print("Part 1 answer:", p1)

    p2 = part_2(input)
    print("Part 2 answer:", p2)


if __name__ == "__main__":
    main()
