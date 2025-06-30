import random
from itertools import combinations

def three_sum_probability(n, trials=1):
    count_no_triple = 0

    for _ in range(trials):
        arr = [random.randint(-2**31, 2**31 - 1) for _ in range(n)]
        found = False

        for i, j, k in combinations(range(n), 3):
            if arr[i] + arr[j] + arr[k] == 0:
                found = True
                break

        if not found:
            count_no_triple += 1

    prob = count_no_triple / trials
    print(f"Probability that no triple sums to zero: {prob}")

def expected_triples(n):
    return n * (n - 1) * (n - 2) / (6 * 2**32)

if __name__ == "__main__":
    n = 100
    three_sum_probability(n, trials=10)
    print(f"Approx expected number of triples: {expected_triples(n)}")
