def part_1(input):
    seeds = {int(i): int(i) for i in input[0][0].split()}
    soil = input[1]
    ferti = input[2]
    water = input[3]
    light = input[4]
    temp = input[5]
    humid = input[6]
    loc = input[7]

    seeds = map_seeds(seeds, soil)
    seeds = map_seeds(seeds, ferti)
    seeds = map_seeds(seeds, water)
    seeds = map_seeds(seeds, light)
    seeds = map_seeds(seeds, temp)
    seeds = map_seeds(seeds, humid)
    seeds = map_seeds(seeds, loc)

    return min(seeds.values())


def map_seeds(seeds, map_range):
    for i in seeds.keys():
        for j in range(len(map_range)):
            to_map = [int(k) for k in map_range[j].split()]
            src = int(to_map[1])
            dest = int(to_map[0])
            count = int(to_map[-1])

            if seeds[i] >= src and seeds[i] < (src + count):
                seeds[i] = dest + (seeds[i] - src)
                break

    return seeds


def part_2(input):
    s = [int(i) for i in input[0][0].split()]
    soil = input[1]
    ferti = input[2]
    water = input[3]
    light = input[4]
    temp = input[5]
    humid = input[6]
    loc = input[7]

    seeds = {}
    for i in range(0, len(s), 2):
        for j in range(0, s[i + 1], int(s[i + 1] ** 0.5)):
            seeds[s[i] + j] = s[i] + j

    seeds = map_seeds(seeds, soil)
    seeds = map_seeds(seeds, ferti)
    seeds = map_seeds(seeds, water)
    seeds = map_seeds(seeds, light)
    seeds = map_seeds(seeds, temp)
    seeds = map_seeds(seeds, humid)
    seeds = map_seeds(seeds, loc)

    best = min(seeds, key=seeds.get)
    bound = 0
    for b in seeds.keys():
        if b < best:
            bound = max(bound, b)
    best_seeds = {i: i for i in range(bound, best + 1)}

    seeds = map_seeds(best_seeds, soil)
    seeds = map_seeds(seeds, ferti)
    seeds = map_seeds(seeds, water)
    seeds = map_seeds(seeds, light)
    seeds = map_seeds(seeds, temp)
    seeds = map_seeds(seeds, humid)
    seeds = map_seeds(seeds, loc)

    return min(best_seeds.values())


def read_file(file_path):
    input = []

    try:
        with open(file_path, "r") as file:
            per_line = []

            for line in file:
                line = line.strip()

                if line[0:6] == "seeds:":
                    per_line.append(line[7:])
                elif line and line[0].isalpha():
                    input.append(per_line)
                    per_line = []
                elif line != "":
                    per_line.append(line)

            input.append(per_line)

            return input

    except FileNotFoundError:
        print(f"File not found: {file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    file_path = "./05/input.txt"
    input = read_file(file_path)

    p1 = part_1(input)
    print("Part 1 answer:", p1)

    p2 = part_2(input)
    print("Part 2 answer:", p2)


if __name__ == "__main__":
    main()
