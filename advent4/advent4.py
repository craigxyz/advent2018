from collections import Counter, defaultdict

data = []
for line in open('input.txt'):
       data.append(line)
data.sort()

guards = defaultdict(Counter)
guard_id = 0
sleep = 0
for each in data:
    parts = each.split()
    minute = int(parts[1].split(":")[1][:-1])
    if 'Guard' in each:
        # starting shift
        guard_id = (parts[3][1:])
        continue
    if 'wakes' in each:
        # waking up
        guards[guard_id].update([x for x in range(sleep, minute)])
    else:
        # falling asleep
        sleep = minute

# Part 1
_, g_id = max((sum(c.values()), g) for g, c in guards.items())
minute = guards[g_id].most_common(1)[0][0]
print(int(g_id)*int(minute))

_, g_id = max((c.most_common()[0][1], g) for g, c in guards.items())
minute = guards[g_id].most_common(1)[0][0]
print(int(g_id)*int(minute))