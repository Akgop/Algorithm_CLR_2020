import random as rand                   # To generate list
from matplotlib import pyplot as plt    # To draw plots
import timeit                           # To measure running time
import pprint                           # To print 2D-array pretty


# Longest Common Sub-sequence: Top-Down
def lcs(x, y, lx, ly, c):
    if lx == 0 or ly == 0:
        c[lx][ly] = 0
        return c[lx][ly]
    # memoization
    if x[lx - 1] == y[ly - 1]:      # found common sub-sequence
        if c[lx - 1][ly - 1] == -1:
            c[lx - 1][ly - 1] = lcs(x, y, lx - 1, ly - 1, c)
        return 1 + c[lx - 1][ly - 1]
    else:
        if c[lx - 1][ly] == -1:
            c[lx - 1][ly] = lcs(x, y, lx - 1, ly, c)
        if c[lx][ly - 1] == -1:
            c[lx][ly - 1] = lcs(x, y, lx, ly - 1, c)
        return max(c[lx - 1][ly], c[lx][ly - 1])


# get string of result
def print_lcs(x, y, lx, ly, c, a):
    if lx == 0 or ly == 0:  # exception handling
        return
    while lx != 0 and ly != 0:
        if x[lx - 1] == y[ly - 1]:
            a.append(x[lx - 1])
            lx -= 1
            ly -= 1
        elif c[lx - 1][ly] > c[lx][ly - 1]:
            lx -= 1
        else:
            ly -= 1
    print("Output :", ''.join(a[::-1]))


# Generate random sequence X and Y using given input(user input n)
def generate_random_sequence(n):
    x = ""
    y = ""
    for _ in range(n):
        rd = rand.randint(65, 90)       # generate Capital Alphabet
        x += chr(rd)
    for _ in range(n):
        rd = rand.randint(65, 90)
        y += chr(rd)
    return x, y


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

    print_lcs(x, y, len(x), len(y), cache, answer)
    print("Running Time:", 10000*(stop - start))             # calculate running time
    print("Length of lcs:", result)
    print()
    print()
    # pprint.pprint(cache)


# show plot
def draw_plot(x, y, title, plot_num, flag=True, y_label="Number of Times"):
    if plot_num is 244 or 248:
        if flag is True:
            plt.subplot(plot_num)
            plt.xticks(x)
            plt.yticks(y)
            plt.xlabel('Input Size')
            plt.ylabel(y_label)
            plt.title(title)
        plt.plot(x, y, linewidth=3)
        plt.plot(x, y, 'bo')
    else:
        plt.subplot(plot_num)
        plt.plot(x, y, linewidth=3)
        plt.plot(x, y, 'bo')
        plt.xticks(x)
        plt.yticks(y)
        plt.xlabel('Input Size')
        plt.ylabel(y_label)
        plt.title(title)


# main function
if __name__ == "__main__":
    N = 50
    for _ in range(10):
        for _ in range(5):
            dp_driver(N)
        N += 50
