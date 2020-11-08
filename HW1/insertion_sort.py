from matplotlib import pyplot as plt    # To draw plots
import timeit                           # To measure running time
import random as rand                   # To generate list


# insertion sort
def insertion_sort(a):
    counter = 0
    start = timeit.default_timer()  # start time of actual running time
    for j in range(1, len(a)):      # n 회
        key = a[j]                  # n - 1 회
        i = j-1                         # n - 1 회
        while i >= 0 and a[i] > key:    # (counter + 1) 회
            counter += 1            # inner loop 수행 횟수 세기 counter 회
            a[i+1] = a[i]           # (n - 1) * counter
            i -= 1                  # (n - 1) * counter
        counter += 1                # while 문 종료 조건 수행 횟수 세기
        a[i+1] = key                # n - 1 회
    stop = timeit.default_timer()   # end time of actual running time
    print(10000*(stop - start))             # calculate running time
    print("Number of times: ", counter)
    return counter, (stop - start)*10000


# list generator (range for random func, count, case)
def list_generator(m, n, case="Average"):
    if case is "Best":
        return [i for i in range(n)]      # Ascending Order
    elif case is "Worst":
        return [i for i in range(n, 0, -1)]   # Descending Order
    else:
        rd_list = []
        for i in range(n):
            rd = rand.randint(0, m)
            while rd in rd_list:
                rd = rand.randint(0, m)
            rd_list.append(rd)
        return rd_list   # Random Order


# show plot
def draw_plot(x, y, title, plot_num, flag=True, ylabel="Number of Times"):
    if plot_num is 244 or 248:
        if flag is True:
            plt.subplot(plot_num)
            plt.xticks(x)
            plt.yticks(y)
            plt.xlabel('Input Size')
            plt.ylabel(ylabel)
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
        plt.ylabel(ylabel)
        plt.title(title)


# Make a list of Best, Worst, Average Case
maximum = 10000

# Worst Case
num = 100
cnt = 0
plot_x_w = []
plot_y_w = []
plot_x_w2 = []
plot_y_w2 = []
print("----- Worst Case -----")
for _ in range(0, 10):
    worst_list = list_generator(maximum, num, "Worst")
    print("Worst Case Input:  ", worst_list)
    print("Input Size :", num)
    cnt, rt = insertion_sort(worst_list)
    plot_x_w.append(num)
    plot_x_w2.append(num)
    plot_y_w.append(cnt)
    plot_y_w2.append(rt)
    print("Worst Case Output: ", worst_list)
    print()
    num += 200
print("---------------------\n\n")
draw_plot(plot_x_w, plot_y_w, title="Worst Case", plot_num=241)
draw_plot(plot_x_w2, plot_y_w2, title="Worst Case", plot_num=245, ylabel="Running Time")

# Best Case
plot_x_b = []
plot_y_b = []
plot_x_b2 = []
plot_y_b2 = []
num = 100
cnt = 0
print("----- Best Case -----")
for _ in range(0, 10):
    best_list = list_generator(maximum, num, "Best")
    print("Best Case Input:  ", best_list)
    print("Input Size :", num)
    cnt, rt = insertion_sort(best_list)
    plot_x_b.append(num)
    plot_x_b2.append(num)
    plot_y_b.append(cnt)
    plot_y_b2.append(rt)
    print("Best Case Output: ", best_list)
    print()
    num += 200
print("---------------------\n\n")
draw_plot(plot_x_b, plot_y_b, title="Best Case",  plot_num=242)
draw_plot(plot_x_b2, plot_y_b2, title="Best Case",  plot_num=246, ylabel="Running Time")

# Average Case
plot_x_a = []
plot_y_a = []
plot_x_a2 = []
plot_y_a2 = []
num = 100
cnt = 0
result_dict = {}
rt_dict = {}
print("----- Average Case -----")
for _ in range(0, 10):  # num += 200 --> total 100 times iteration
    result = 0
    result2 = 0
    for _ in range(0, 10):      # Random List --> Same num repeat 10 times, get average
        average_list = list_generator(maximum, num)     # Average Case
        print("Average Case Input:  ", average_list)
        print("Input Size :", num)
        cnt, rt = insertion_sort(average_list)
        print("Average Case Output: ", average_list)
        result += cnt
        result2 += rt
        print()
    plot_x_a.append(num)
    plot_x_a2.append(num)
    plot_y_a.append(result // 10)
    plot_y_a2.append(result2 // 10)
    result_dict[num] = (result // 10)
    rt_dict[num] = (result2 // 10)
    num += 200
print("Number of times")
print(result_dict)
print("Actual Running Time")
print(rt_dict)  # calculate running time
print("---------------------\n\n")
draw_plot(plot_x_a, plot_y_a, title="Average Case", plot_num=243)
draw_plot(plot_x_a2, plot_y_a2, title="Average Case", plot_num=247, ylabel="Running Time")

draw_plot(plot_x_w, plot_y_w, title="Insertion Sort", plot_num=244)
draw_plot(plot_x_b, plot_y_b, title="Insertion Sort", plot_num=244, flag=False)
draw_plot(plot_x_a, plot_y_a, title="Insertion Sort", plot_num=244, flag=False)

draw_plot(plot_x_w2, plot_y_w2, title="Insertion Sort", plot_num=248, ylabel="Running Time")
draw_plot(plot_x_b2, plot_y_b2, title="Insertion Sort", plot_num=248, flag=False, ylabel="Running Time")
draw_plot(plot_x_a2, plot_y_a2, title="Insertion Sort", plot_num=248, flag=False, ylabel="Running Time")

plt.show()
