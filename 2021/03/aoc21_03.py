# %% 
import os
import numpy as np


# %%
def max_element(array):
    return(np.bincount(array).argmax())
def min_element(array):
    return(np.bincount(array).argmin())
# %%

def gammaXepsilon(input):
    M = np.array([list(x) for x in input],int)
    g = ''
    e = ''
    for _,x in enumerate(M.transpose()):
        g+=str(max_element(x))
        e+=str(min_element(x))
    g = int(g,2)
    e = int(e,2)
    return(g*e)

# %%
def Co2(input):
    M = np.array([list(x) for x in input],int)
    i = 0
    while len(M)>1:
        x = M.transpose()[i]
        b = np.bincount(x)
        if b[0]==b[1]:
            v = np.where(x==0)
        else:
            v = max_element(x)
        M = np.delete(M,np.where(x==v),axis=0)
        i +=1
    r =''
    for x in M[0].tolist():
        r+=str(x)
    return(int(r,2))
def O2(input):
    M = np.array([list(x) for x in input],int)
    i = 0
    while len(M)>1:
        x = M.transpose()[i]
        b = np.bincount(x)
        print(b)
        if b[0]==b[1]:
            v = np.where(x==1)
        else:
            v = min_element(x)
        M = np.delete(M,np.where(x==v),axis=0)
        i +=1
    r =''
    for x in M[0].tolist():
        r+=str(x)
    return(int(r,2))

def life_support(input):
    return(Co2(input)*O2(input))
# %%
if __name__=='__main__':
    filename = os.path.join("input.txt")

    input = np.genfromtxt(filename,dtype=str)

    print('power consumption:',gammaXepsilon(input))

# %%
