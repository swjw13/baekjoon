def solution(cap, n, deliveries, pickups):
    answer = 0

    del_idx = n - 1
    while del_idx >= 0 and deliveries[del_idx] == 0:
        del_idx -= 1
    pick_idx = n - 1
    while pick_idx >= 0 and pickups[pick_idx] == 0:
        pick_idx -= 1

    while True:
        cap_start_idx = del_idx
        del_cap = cap
        while del_cap > 0 and del_idx >= 0:
            if deliveries[del_idx] <= del_cap:
                del_cap -= deliveries[del_idx]
                deliveries[del_idx] = 0
                while del_idx >= 0 and deliveries[del_idx] == 0:
                    del_idx -= 1
            else:
                deliveries[del_idx] -= del_cap
                del_cap = 0

        pick_start_idx = pick_idx
        pick_cap = cap
        while pick_cap > 0 and pick_idx >= 0:
            if pickups[pick_idx] <= pick_cap:
                pick_cap -= pickups[pick_idx]
                pickups[pick_idx] = 0
                while pick_idx >= 0 and pickups[pick_idx] == 0:
                    pick_idx -= 1
            else:
                pickups[pick_idx] -= pick_cap
                pick_cap = 0

        answer += max(cap_start_idx + 1, pick_start_idx + 1) * 2

        if del_idx < 0 or pick_idx < 0:
            break
    if del_idx < 0 and pick_idx < 0:
        return answer

    elif del_idx < 0:
        while pick_idx >= 0:
            pick_start_idx = pick_idx
            pick_cap = cap
            while pick_cap > 0 and pick_idx >= 0:
                if pickups[pick_idx] <= pick_cap:
                    pick_cap -= pickups[pick_idx]
                    pickups[pick_idx] = 0
                    while pick_idx >= 0 and pickups[pick_idx]== 0:
                        pick_idx -= 1
                else:
                    pickups[pick_idx] -= pick_cap
                    pick_cap = 0

            answer += (pick_start_idx + 1) * 2

    elif pick_idx < 0:
        while del_idx >= 0:
            cap_start_idx = del_idx
            del_cap = cap
            while del_cap > 0 and del_idx >= 0:
                if deliveries[del_idx] <= del_cap:
                    del_cap -= deliveries[del_idx]
                    deliveries[del_idx] = 0
                    while del_idx >= 0 and deliveries[del_idx] == 0:
                        del_idx -= 1
                else:
                    deliveries[del_idx] -= del_cap
                    del_cap = 0
            answer += (cap_start_idx + 1) * 2

    return answer