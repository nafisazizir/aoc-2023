def part_1(input):
    res = 0

    for line in input:
        winning_set = set()
        card_winning = []

        winning = line.split("|")[0].split(":")[-1]
        for n in winning.split():
            winning_set.add(int(n))

        cards = line.split("|")[-1]

        for n in cards.split():
            if int(n) in winning_set:
                card_winning.append(int(n))

        if len(card_winning):
            res += 2 ** (len(card_winning) - 1)

    return res


def part_2(input):
    res = 0
    copies = {}

    for id, line in enumerate(input):
        winning_set = set()
        card_winning = []

        winning = line.split("|")[0].split(":")[-1]
        for n in winning.split():
            winning_set.add(int(n))

        cards = line.split("|")[-1]

        for n in cards.split():
            if int(n) in winning_set:
                card_winning.append(int(n))

        copies[id + 1] = copies.get(id + 1, 0) + 1
        for i in range(1, len(card_winning) + 1):
            next = id + 1 + i
            copies[next] = copies.get(next, 0) + copies.get(id + 1)

        res += copies[id + 1]

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
    file_path = "./04/input.txt"
    input = read_file(file_path)

    p1 = part_1(input)
    print("Part 1 answer:", p1)

    p2 = part_2(input)
    print("Part 2 answer:", p2)


if __name__ == "__main__":
    main()
