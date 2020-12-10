# vi = dollars, wi = pounds
# vi > 0, wi = i for 1, 2, 3, ..., n.
# randomly choose value vi [1~2n] as input
# W = floor ( n^2 / 2 )
# bottom up dynamic-programming
# n items -> O(n^3)
import random as rand                   # To generate list
from matplotlib import pyplot as plt    # To draw plots
import timeit                           # To measure running time
from pprint import pprint

# generate random set
def generate_random_set(n):
    w = []
    v = []
    for _ in range(n):
        w.append(rand.randint(1, n))    # generate weight vector
        v.append(rand.randint(1, 2*n))  # generate value vector
    return w, v


def bottom_up_01knapsack(n):
    cap = n**2 // 2     # W which is capacity of knapsack
    c = [[0] * (cap+1) for _ in range(N+1)]
    w, v = generate_random_set(n)

    start = timeit.default_timer()  # start time of actual running time
    for i in range(1, n+1):
        for j in range(1, cap+1):
            if w[i-1] <= j:
                c[i][j] = max(v[i-1] + c[i-1][j-w[i-1]], c[i-1][j])
            else:
                c[i][j] = c[i-1][j]
    stop = timeit.default_timer()  # end time of actual running time

    runtime = 10000 * (stop - start)  # calculate running time
    print("Running Time:", runtime)
    print("Max value:", c[-1][-1])  # print max value
    print(v, w)
    pprint(c)
    print()
    print()
    return runtime


# main function
if __name__ == "__main__":
    N = 5
    bottom_up_01knapsack(N)

