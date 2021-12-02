# %%
import os

# %%
def cal_pos(input):
    coord={}
    for (dir,val) in input:
        if dir == 'forward':
            coord.setdefault(dir,[]).append(val)
        elif dir =='up':
            coord.setdefault('vert',[]).append(-val)
        else:
            coord.setdefault('vert',[]).append(val)

    r = 1
    for dir in coord:
        r = r*sum(coord[dir])
    return(r)
# %%
def aimed_cal_pos(input):
    a = 0
    h = 0
    d = 0
    for (dir,val) in input:
        if dir == 'up':
            a = a-val
        elif dir =='down':
            a = a+val
        else:
            h = h+val
            d += val*a

    return(h*d)
        

# %%
if __name__=='__main__':
    filename = os.path.join("input.txt")
    input = []
    with open(filename) as f:
        for line in f:
            [d,v]=line.split()
            input.append((d,int(v)))


    print(cal_pos(input))
    print(aimed_cal_pos(input))
