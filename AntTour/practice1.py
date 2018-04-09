import math

def read_integers(filename):
    with open(filename) as f:
        nums = [int(x) for x in f]
        trial = nums.pop(0)

        bar_list = []
        while trial > 0:
            trial -= 1
            bar_count = nums.pop(0)
            bars = nums[:bar_count]
            nums = nums[bar_count:]
            bar_list.append(bars)

        return bar_list

def ant_route(bars):
    bars.sort()

    i = 0
    max_gap = 0
    toVisit = list(range(0, len(bars)))

    for _ in range(0, len(bars)):
        if (max(toVisit) - i >= 2):
            gap = abs(bars[i + 2] - bars[i])
            i += 2
            toVisit.pop(toVisit.index(i))
        else:
            j = toVisit.pop(len(toVisit) - 1)
            gap = abs(bars[j] - bars[i])
            i = j

        if max_gap < gap : max_gap = gap

    return math.ceil(max_gap / 2)

lists = read_integers('input01.txt')

for bars in lists:
    print(ant_route(bars))



