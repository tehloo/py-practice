import math
import numpy as np

def get_min_length(sticks):
    if len(sticks) == 1:
        return 0
    elif len(sticks) == 2:
        return math.ceil((max(sticks)-min(sticks))/2)

    sticks.sort()
    distance = np.array(sticks[2:]) - np.array(sticks[:-2])
    return math.ceil(max(distance)/2)

if __name__ == "__main__":
    with open('input01.txt', 'r') as f:
        line = f.readline()
        T = int(line)
        for _ in range(T):
            line = f.readline()
            N = int(line)
            sticks = []
            for _ in range(N):
                sticks.append(int(f.readline()))
            print(get_min_length(sticks))
