def get_damage(combos):
    damage = 1
    total_damage = 0
    for c in combos:
        if (c == 'C'):
            damage *= 2
        elif (c == 'S'):
            total_damage += damage

    return total_damage


def try_hack(candidates):
    new_candidates = []
    for combo in candidates:
        damage = get_damage(combo)

        for i in range(len(combo) - 1):
            new_combo = list(combo)
            new_combo[i] = combo[i + 1]
            new_combo[i + 1] = combo[i]

            if list(combo) == new_combo:
                continue

            new_damage = get_damage(new_combo)
            if new_damage <= damage:
                j = 0
                for j in range(len(new_candidates)):
                    if new_damage <= get_damage(new_candidates[j]):
                        break

                new_candidates.insert(j, new_combo)

    return new_candidates


def optimize_combo(max_damage, combo):
    trial = 0
    cur_damage = 0
    candidates = []
    candidates.append(combo)
    while (trial < 10):
        if len(candidates) == 0:
            break;
        cur_damage = get_damage(candidates[0])
        if (cur_damage <= max_damage):
            return str(trial)

        candidates = try_hack(candidates)
        trial += 1

    return "IMPOSSIBLE"


with open("input01.txt") as f:
    cases = int(f.readline())
    for _ in range(cases):
        line = f.readline().split()
        print("Case #%d: %s" % (_ + 1, optimize_combo(int(line[0]), line[1])))
