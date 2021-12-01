# %%
def bigger(input):
    return sum(x<y for x, y in zip(input,input[1:]))
def rolling_sum(input):
    A = [sum(x) for x in zip(input,input[1:],input[2:])]
    return bigger(A)

# %%
if __name__=='__main__':
    filename = os.path.join("input.txt")

    with open(filename) as f:
        input = [int(i) for i in f.readlines()]

    print(bigger(input))
    print(rolling_sum(input))
