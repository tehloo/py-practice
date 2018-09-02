def read_numbers(filename):
    with open(filename) as f:
        trial = int(f.readline())
        numbers = []
        while trial > 0:
            trial -= 1
            numbers.append(list(map(int, f.readline().split())))
        return numbers


number_set = read_numbers("input00.txt")
for (numbers) in number_set:
    i = 0
    while i < 100000:
        sum = 0
        for j in range(i + 1):
            j %= 5
            sum += numbers[j]

        last_num = sum % 10
        found = True
        repeated = 0
        for x in str(sum):
            if (last_num != int(x)):
                found = False
                break
            repeated += 1

        if found :
            print ("%d %d(%d)" % (i, last_num, repeated))
            break

        i += 1

