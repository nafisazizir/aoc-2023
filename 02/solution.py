def part_1(inputs):
    res = 0

    map = {"red": 12, "green": 13, "blue": 14}

    for line in inputs:
        _id, content = line.split(":")
        _id = int(_id.split(" ")[-1])
        is_valid = True

        for game in content.split(";"):
            for bag in game.split(","):
                n, color = bag.split()

                if int(n) > map.get(color, 0):
                    is_valid = False

        if is_valid:
            res += _id

    return res


def part_2(inputs):
    res = 0

    for line in inputs:
        _id, content = line.split(":")
        _id = int(_id.split(" ")[-1])
        map = {}

        for game in content.split(";"):
            for bag in game.split(","):
                n, color = bag.split()
                map[color] = max(map.get(color, 0), int(n))

        curr = 1
        for val in map.values():
            curr = curr * val

        res += curr

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
    file_path = "./02/input.txt"
    input = read_file(file_path)

    p1 = part_1(input)
    print("Part 1 answer:", p1)

    p2 = part_2(input)
    print("Part 2 answer:", p2)


if __name__ == "__main__":
    main()
