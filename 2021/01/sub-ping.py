# %%

import os

filename = os.path.join("input.txt")

with open(filename) as f:
    input = f.read().splitlines()

# %%
count = 0
for i in range(1,len(input)):
    if input[i]>input[i-1]:
        count += 1

print(count)