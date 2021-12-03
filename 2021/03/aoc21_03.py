# %% 
import os
import numpy as np


# %%
def max_element(array):
    return(np.bincount(array).argmax())
def min_element(array):
    return(np.bincount(array).argmin())
# %%

def gamma(input=input):
    M = np.array([list(x) for x in input],int)
    g = ''
    for _,x in enumerate(M.transpose()):
        g+=str(max_element(x))
    g = int(g,2)
    return(g)

def epsilon(input=input):
    M = np.array([list(x) for x in input],int)
    e = ''
    for _,x in enumerate(M.transpose()):
        e+=str(min_element(x))
    e = int(e,2)
    return(e)

def power_consumption(input=input):
    return(gamma(input)*epsilon(input))

# %%
def Co2(input=input):
    M = np.array([list(x) for x in input],int)
    i = 0
    while len(M)>1:
        x = M.transpose()[i]
        b = np.bincount(x)
        if len(b)==1:
            i +=1
        else:
            if b[0]==b[1]:
                v = 1
            else:
                v = max_element(x)
            M = np.delete(M,np.where(x==v),axis=0)
            i +=1
    r =''
    for x in M[0].tolist():
        r+=str(x)
    return(int(r,2))
def O2(input=input):
    M = np.array([list(x) for x in input],int)
    i = 0
    while len(M)>1:

        x = M.transpose()[i]
        b = np.bincount(x)
        if len(b)==1:
            i +=1
        else:
            if b[0]==b[1]:
                v = 0
            else:
                v = min_element(x)
                print(v)
            M = np.delete(M,np.where(x==v),axis=0)
            i +=1
    r =''
    for x in M[0].tolist():
        r+=str(x)
    return(int(r,2))

def life_support(input=input):
    return(Co2(input)*O2(input))
# %%
if __name__=='__main__':
    filename = os.path.join("input.txt")

    input = np.genfromtxt(filename,dtype=str)

    print('power consumption:',gammaXepsilon(input))
    print('life support:', life_support(input))

# %%
