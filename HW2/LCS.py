import random as rand                   # To generate list
from matplotlib import pyplot as plt    # To draw plots
import timeit                           # To measure running time


# Longest Common Sub-sequence: Top-Down
def lcs(x, y, lx, ly, c):
    if lx == 0 or ly == 0:
        c[lx][ly] = 0
        return c[lx][ly]
    # memoization
    if x[lx - 1] == y[ly - 1]:      # found common sub-sequence
        if c[lx - 1][ly - 1] == -1:     # if never calculated
            c[lx - 1][ly - 1] = lcs(x, y, lx - 1, ly - 1, c)    # do recursion
        return 1 + c[lx - 1][ly - 1]    # return result + 1
    else:
        if c[lx - 1][ly] == -1:     # if never calculated
            c[lx - 1][ly] = lcs(x, y, lx - 1, ly, c)    # do recursion
        if c[lx][ly - 1] == -1:     # if never calculated
            c[lx][ly - 1] = lcs(x, y, lx, ly - 1, c)    # do recursion
        return max(c[lx - 1][ly], c[lx][ly - 1])    # return max between two previous values


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


# Generate random sequence X and Y using given input(user input n)
def generate_random_sequence(n):
    x = ""
    y = ""
    for _ in range(n):
        rd = rand.randint(65, 90)       # generate Upper Case
        x += chr(rd)
    for _ in range(n):
        rd = rand.randint(65, 90)       # generate Upper Case
        y += chr(rd)
    return x, y


# show plot
def draw_plot(x, y, title):
    plt.plot(x, y, linewidth=3)
    plt.plot(x, y, 'bo')
    plt.xticks(x)
    plt.yticks(y)
    plt.xlabel('Input Size')
    plt.ylabel("Running Time")
    plt.title(title)


# Recursion Driver
def dp_driver(n):
    x, y = generate_random_sequence(n)
    cache = [([-1] * (n + 1)) for _ in range(n + 1)]  # initialize memory to -1
    answer = []
    print("Input Size: ", n)
    print("Input X:", x)
    print("Input Y:", y)

    start = timeit.default_timer()  # start time of actual running time
    result = lcs(x, y, len(x), len(y), cache)
    stop = timeit.default_timer()  # end time of actual running time

    print_lcs(x, y, len(x), len(y), cache, answer)      # print result LCS
    runtime = 10000*(stop - start)              # calculate running time
    print("Running Time:", runtime)
    print("Length of lcs:", result)             # print length
    print()
    print()
    return runtime


# main function
if __name__ == "__main__":
    N = 50
    plot_x = []     # plot x
    plot_y = []     # plot y
    avg_runtime = 0     # avg runtime
    for _ in range(10):     # ten different input size N
        avg_runtime = 0
        plot_x.append(N)
        for _ in range(5):      # repeat 5 times on same input size
            avg_runtime += dp_driver(N)     # run DP
        avg_runtime //= 5       # get average : get rid of decimal points
        plot_y.append(avg_runtime)
        N += 50     # increase input size by 50
    draw_plot(plot_x, plot_y, title="Average Runtime")  # draw plots
    plt.show()  # print plots
