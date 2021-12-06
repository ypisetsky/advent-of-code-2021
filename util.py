def getlines(day):
    with open(f"data/day{day}.txt") as f:
        return [line.strip() for line in f.readlines() if len(line) > 1]

def getblankseparated(day):
    with open(f"data/day{day}.txt") as f:
        return f.read().split("\n\n")

def tokenedlines(day):
    lines = getlines(day)
    ret = []
    for line in lines:
        parts = line.strip().split(' ')
        parsed_parts = []
        for part in parts:
            try:
                parsed_parts.append(int(part))
            except:
                try:
                    parsed_parts.append(float(part))
                except:
                    parsed_parts.append(part)
        ret.append(parsed_parts)
    return ret
