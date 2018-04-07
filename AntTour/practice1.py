
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
    print(bars)
    length = 0;
    while length < 10:
        print (length)
        for center in bars:






        length += 1






lists = read_integers('input01.txt')

for bars in lists:
    print(ant_route(bars))



