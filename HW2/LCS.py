import random as rand                   # To generate list
# import pprint

# Longest Common Sub-sequence: Top-Down
def lcs(row, col, cache):
    pass


# DP Initialize
def initialize_dp(n):
    cache = [([0] * n) for _ in range(n)]  # initialize memory to zero
    lcs(0, 0, cache)
    # pprint.pprint(dp)


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


N = int(input())
X, Y = generate_random_sequence(N)
initialize_dp(N)
print(X)
print(Y)
