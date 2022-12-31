from collections import deque


def is_destroyed(bull, key):
    if bull <= key:
        return True
    return False


price_for_a_bullet = int(input())
barrel_capacity = int(input())
bullets = deque([int(x) for x in input().split()])
locks = deque([int(x) for x in input().split()])
intelligence = int(input())
shots = 0
bullets_cost = 0

while locks and bullets:
    bullet = bullets.pop()
    lock = locks[0]
    bullets_cost += price_for_a_bullet
    shots += 1

    if is_destroyed(bullet, lock):
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")

    if shots == barrel_capacity:
        if bullets:
            print("Reloading!")
            shots = 0

else:
    if not bullets and not locks:
        print(f"{len(bullets)} bullets left. Earned ${intelligence - bullets_cost}")
    elif bullets:
        print(f"{len(bullets)} bullets left. Earned ${intelligence - bullets_cost}")
    else:
        print(f"Couldn't get through. Locks left: {len(locks)}")
