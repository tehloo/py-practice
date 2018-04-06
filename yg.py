import math

def get_list_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    input_list = map(lambda x:x.strip(), lines)
    return input_list

def get_result(rod_list):
    rod_list = map(int, rod_list)
    sorted_rod_list = sorted(rod_list)

    if (len(sorted_rod_list) == 1):
        res = 0
        return res

    rod_odd = sorted_rod_list[0::2]
    rod_even = sorted_rod_list[1::2]

    max_interval = max([sorted_rod_list[1] - sorted_rod_list[0], sorted_rod_list[-1] - sorted_rod_list[-2]])
    for i in range(1, len(rod_odd)):
        interval = rod_odd[i] - rod_odd[i-1]
        max_interval = interval if interval > max_interval else max_interval

    for i in range(1, len(rod_odd)):
        interval = rod_even[i] - rod_even[i-1]
        max_interval = interval if interval > max_interval else max_interval

    res = int(math.ceil(max_interval / 2.0))
    return res

def iter_input_list(input_list):
    input_gen = (g for g in input_list)
    total_cnt = int(input_gen.next())
    for i in range(total_cnt):
        inner_cnt = int(input_gen.next())
        rod_list = []
        for j in range(inner_cnt):
            rod_list.append(input_gen.next())
        res = get_result(rod_list)
        print (res)


if __name__ == "__main__":
    yoon = get_list_from_file("input01.txt")
    iter_input_list(yoon)
