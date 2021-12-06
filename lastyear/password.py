from util import tokenedlines

def checkpassword(tokens):
    expect_letter = tokens[1][0]
    min,max = [int(a) for a in tokens[0].split('-')]
    actual = sum(1 for c in tokens[2] if c == expect_letter)
    part2 = (tokens[2][min-1] == expect_letter) ^ (tokens[2][max-1] == expect_letter)
    return (min <= actual and max >= actual, part2)

x = 0
y = 0
for line in tokenedlines("old2"):
    newx, newy = checkpassword(line)
    x += newx
    y += newy
print(f"{x} passwords are valid, {y} passwords are valid?")