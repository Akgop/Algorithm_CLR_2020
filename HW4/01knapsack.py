import random as rand                   # To generate list
from matplotlib import pyplot as plt    # To draw plots
import timeit                           # To measure running time
from pprint import pprint


# generate random set
def generate_random_set(n):
    w = []
    v = []
    for i in range(n):
        w.append(i+1)    # generate weight vector
        v.append(rand.randint(1, 2*n))  # generate value vector
    return w, v


def bottom_up_01knapsack(n):
    cap = n**2 // 2     # W which is capacity of knapsack
    c = [[0] * (cap+1) for _ in range(N+1)]     # allocate 2D array
    w, v = generate_random_set(n)

    start = timeit.default_timer()  # start time of actual running time
    for i in range(1, n+1):
        for j in range(1, cap+1):
            if w[i-1] <= j:         # available
                c[i][j] = max(v[i-1] + c[i-1][j-w[i-1]], c[i-1][j])
            else:
                c[i][j] = c[i-1][j]
    stop = timeit.default_timer()  # end time of actual running time

    runtime = 10000 * (stop - start)  # calculate running time
    print("Amount of Item:", n)
    print("Running Time:", runtime)
    print("Max value:", c[-1][-1])  # print max value
    # print(v, w)
    # pprint(c)
    print()
    print()
    return runtime


# show plot
def draw_plot(x, y, title):
    plt.plot(x, y, linewidth=3)
    plt.plot(x, y, 'bo')
    plt.xticks(x)
    plt.yticks(y)
    plt.xlabel('Input Size')
    plt.ylabel("Running Time")
    plt.title(title)


# main function
if __name__ == "__main__":
    N = 5
    plot_x = []
    plot_y = []
    avg_runtime = 0
    for _ in range(30):     # ten different input size N
        avg_runtime = 0
        plot_x.append(N)
        for _ in range(5):      # repeat 5 times on same input size
            avg_runtime += bottom_up_01knapsack(N)     # run DP
        avg_runtime //= 5       # get average : get rid of decimal points
        plot_y.append(avg_runtime)
        N += 5     # increase input size by 5
    draw_plot(plot_x, plot_y, title="Average Runtime")  # draw plots
    plt.show()  # print plots

