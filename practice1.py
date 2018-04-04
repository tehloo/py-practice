with open('/Users/tehloo/PycharmProjects/practice/file_input.txt') as f:
    n = int(next(f))

    while n > 0:
        n =  n - 1
        line = next(f)
        x_sum = 0;
        for x in line.split():
            x_sum = x_sum + int(x)
        print x_sum, " - ", line


