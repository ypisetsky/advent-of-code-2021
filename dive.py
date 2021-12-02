
def solve2(lines):
    horiz = 0
    depth = 0
    aim = 0
    for line in lines:
        parts = line.strip().split(" ")
        if len(parts) != 2:
            print(f"Error {line} is malformed")
            return None
        step = int(parts[1])
        if parts[0] == "forward":
            horiz += step
            depth += step * aim
        elif parts[0] == "down":
            aim += step
        elif parts[0] == "up":
            aim -= step
        else:
            print(f"Unknown command in {line}")
            return None
    return (horiz * aim, horiz * depth)


f = open('data/day2.txt')
lines = f.readlines()
print(f"Solutions are {solve2(lines)}")
