
def read_integers(filename):
    with open(filename) as f:
        nums = [int(x) for x in f]
        print ("All numbers : ", nums)
        trial = nums.pop(0)

        bar_list = []
        while trial > 0:
            trial -= 1
            bar_count = nums.pop(0)
            bars = nums[:bar_count]
            nums = nums[bar_count:]
            bar_list.append(bars)

        return bar_list


def isOverlap(x1, y1, x2, y2):
    for i in range(x1, y1):
        if (i >= x2 and i <= y2): return True
    return False


def ant_route(bars):
    print(bars)
    half = 0
    while True:
        # half value is increasing...
        half += 1

        visit = []
        toVisit = list(range(len(bars)))
        cur_i = 0
        compare_i = toVisit[1]
        print("Trying with ", half)

        while cur_i != compare_i:
            x = bars[cur_i] - half
            y = bars[cur_i] + half
            px = bars[compare_i] - half
            py = bars[compare_i] + half

            #try:
            print("%d(%d:%d-%d) compare to %d(%d:%d-%d)" % (cur_i, bars[cur_i], x, y, compare_i, bars[compare_i] , px, py))
            if (isOverlap(x, y, px, py)):
                toVisit.remove(cur_i)
                visit.append(cur_i)
                if (len(toVisit) == 1):
                    break
                cur_i = compare_i
                if (toVisit.index(cur_i) == len(toVisit) - 1):
                    compare_i = toVisit[0]
                else:
                    compare_i = toVisit[toVisit.index(cur_i) + 1]

                print(" found! ", visit, " to visit ", toVisit)

            else:
                if (toVisit.index(compare_i) == len(toVisit) - 1):
                    compare_i = toVisit[0]
                else:
                    compare_i = toVisit[toVisit.index(compare_i) + 1]

            # except IndexError as e:
            #
            #     print("Exception!!!")
            #     print(toVisit, cur_i, compare_i)
            #     print(visit)
            #     print(e)

        if (len(toVisit) == 1):
            break;

    print ("result=", half)


lists = read_integers('input01.txt')

for bars in lists:
    ant_route(bars)



