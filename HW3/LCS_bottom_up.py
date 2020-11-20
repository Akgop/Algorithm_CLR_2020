import random as rand                   # To generate list
from matplotlib import pyplot as plt    # To draw plots
import timeit                           # To measure running time


# bottom up LCS
def lcs_length(x, y, n, table):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    return table[n][n]


# get string of result
def print_lcs(x, y, lx, ly, c, a):
    if lx == 0 or ly == 0:  # exception handling
        return
    while lx != 0 and ly != 0:
        if x[lx - 1] == y[ly - 1]:
            a.append(x[lx - 1])
            lx -= 1
            ly -= 1
        elif c[lx - 1][ly] > c[lx][ly - 1]:     # lookup memo
            lx -= 1
        else:
            ly -= 1
    print("Output :", ''.join(a[::-1]))     # print reverse from list


# generate random sequence (A,C,G,T)
def generate_random_gene(n):
    finite_set = ['A', 'C', 'G', 'T']
    x = ""
    y = ""
    for _ in range(n):
        x += rand.choice(finite_set)  # generate finite_set
        y += rand.choice(finite_set)  # generate finite_set
    return x, y


def driver(n):
    t = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    answer = []
    x, y = generate_random_gene(n)
    print("Input Size: ", n)
    print("Input X:", x)
    print("Input Y:", y)

    start = timeit.default_timer()  # start time of actual running time
    result = lcs_length(x, y, n, t)
    stop = timeit.default_timer()  # end time of actual running time
    print_lcs(x, y, n, n, t, answer)

    runtime = 10000 * (stop - start)  # calculate running time
    print("Running Time:", runtime)
    print("Length of lcs:", result)  # print length
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
    N = 10
    plot_x = []  # plot x
    plot_y = []  # plot y
    avg_runtime = 0  # avg runtime
    for _ in range(100):     # ten different input size N
        avg_runtime = 0
        plot_x.append(N)
        for _ in range(5):      # repeat 5 times on same input size
            avg_runtime += driver(N)     # run DP
        avg_runtime //= 5       # get average : get rid of decimal points
        plot_y.append(avg_runtime)
        N += 10     # increase input size by 50
    draw_plot(plot_x, plot_y, title="Average Runtime")  # draw plots
    plt.show()  # print plots
