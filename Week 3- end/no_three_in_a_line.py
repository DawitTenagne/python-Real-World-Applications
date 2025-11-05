# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment"
#
# Names: Omer Firat
#
# Section: 556
# Assignment: LAB: Topic 10 (team) part 1
# Date: 29 October 2025


import random

def collinear(p1, p2, p3):
    """Check if three points are collinear using area determinant test."""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x2 - x1)*(y3 - y1) == (y2 - y1)*(x3 - x1)

def no_three_in_line(n):
    # --- Small n: special hardcoded cases (bonus guarantee) ---
    if n <= 0:
        return []
    if n == 1:
        return [(0, 0)]
    if n == 2:
        # Return all 4 corners; no three are collinear on a 2x2 grid
        return [(0, 0), (0, 1), (1, 0), (1, 1)]
    if n == 3:  # Always returns 6 points (bonus)
        return [(0, 0), (0, 1), (1, 0), (1, 2), (2, 1), (2, 2)]

    # Target goals
    cap = min(2 * n, n * n)     # Practical upper limit (~2n)
    target = (9 * n + 4) // 5   # ceil(1.8 * n)

    # Candidate pool: several modular quadratic families + full grid
    C = set()
    for x in range(n):
        C.add((x, (x * x) % n))
        C.add((x, (x * x + x) % n))
        C.add((x, (x * x + 1) % n))
        C.add((x, (2 * x * x + x) % n))
    for x in range(n):
        for y in range(n):
            C.add((x, y))
    C = list(C)

    # Greedy builder
    def greedy(order):
        S = []
        for p in order:
            ok = True
            k = len(S)
            if k >= 2:
                for i in range(k - 1):
                    a = S[i]
                    for j in range(i + 1, k):
                        if collinear(a, S[j], p):
                            ok = False
                            break
                    if not ok:
                        break
            if ok:
                S.append(p)
                if len(S) >= cap:
                    break
        return S

    # Multiple randomized attempts
    best = []
    for _ in range(600):
        random.shuffle(C)
        S = greedy(C)
        if len(S) > len(best):
            best = S
        # Stop if we reached the target or upper limit
        if len(best) >= target or len(best) >= cap:
            return best

    # Backup exact search for small grids (guarantees bonus for n <= 6)
    if n <= 6:
        P = [(x, y) for x in range(n) for y in range(n)]
        # Sorting helps pruning by starting near the center
        P.sort(key=lambda t: (abs(t[0] - (n - 1) / 2) + abs(t[1] - (n - 1) / 2)))
        best = []

        def backtrack(i, S):
            nonlocal best
            # Pruning: if even with remaining points we can’t beat best, stop
            if len(S) + (len(P) - i) <= len(best):
                return
            if i == len(P):
                if len(S) > len(best):
                    best = S[:]
                return
            p = P[i]
            # Try including p
            ok = True
            k = len(S)
            if k >= 2:
                for a in range(k - 1):
                    for b in range(a + 1, k):
                        if collinear(S[a], S[b], p):
                            ok = False
                            break
                    if not ok:
                        break
            if ok:
                S.append(p)
                backtrack(i + 1, S)
                S.pop()
            # Try excluding p
            backtrack(i + 1, S)

        backtrack(0, [])
        return best

    return best