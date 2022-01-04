from util import getlines,as_ints
file = "15"

data = as_ints(getlines(file)[0].split(','))
recents = {}

last_val = None

for i in range(30000000):
    if i < len(data):
        next_val = data[i]
    elif last_val in recents:
        next_val = i - recents[last_val] - 1
    else:
        next_val = 0
    recents[last_val] = i - 1
    last_val = next_val
    #print(f"new value is {last_val} at {i}")
    if i % 100000 == 0:
        print(f"{i}: {last_val} {len(recents)}")
print(last_val)
#print(recents)
