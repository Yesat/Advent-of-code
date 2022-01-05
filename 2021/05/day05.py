from aocd import lines
from itertools import *
from collections import *
# %%
def treat_data(line):
    line = line.replace(" -> ",",")    
    return([int(n) for n in line.split(',')])

def treat_coord(coords):
    coords_g = []
    for x in coords:
        if x[0]==x[2]:
            coords_g.append(x)
        elif x[1]==x[3]:
            coords_g.append(x)
    return(coords_g)

def glines(coords_g):
    lines_g = []
    for a in coords_g:
        x_min = min([a[0],a[2]])
        x_max = max([a[0],a[2]])
        y_min = min([a[1],a[3]])
        y_max = max([a[1],a[3]])
        if x_min == x_max:
            lines_g.append([(a[0],v) for v in range(y_min,y_max+1)])
        else:
            lines_g.append([(v,a[1]) for v in range(x_min,x_max+1)])
    return lines_g

def count_cross(lines_g):
    i = 0
    a = Counter(chain(*lines_g))
    for x in a:
        if a[x] >1:
            i+=1
    return(i)

# %% 
def _lines(coords):
    lines_ = []
    for a in coords:
        x_min = min([a[0],a[2]])
        x_max = max([a[0],a[2]])
        y_min = min([a[1],a[3]])
        y_max = max([a[1],a[3]])
        if a[0] == a[2]:
            lines_.append([(a[0],v) for v in range(y_min,y_max+1)])
        elif a[1] == a[3]:
            lines_.append([(v,a[1]) for v in range(x_min,x_max+1)])
        elif a[0]<a[2]:
            lines_.append ([v for v in zip(range(x_min,x_max+1),range(y_min,y_max+1))])
        else:
            lines_.append ([v for v in zip(range(x_max,x_min-1,-1),range(y_min,y_max+1))])
    return lines_

# %%
def main():
    coords =[]
    for line in lines:
        coords.append(treat_data(line))
    coords_g=treat_coord(coords)
    lines_g=glines(coords_g)
    lines_ = _lines(coords)
    print(count_cross(lines_g),count_cross(lines_))
    

if __name__=='__main__':
    main()
# %%
