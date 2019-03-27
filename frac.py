import matplotlib.pyplot as plt
import numpy as np

def conv(z):
    ep,i=0.005,0
    u=[1,0]
    try:
        while abs(u[-1]-u[-2]) > ep:
            u.append(u[-1]**2+z)
            i+=1
            if i >= 500:
                return False, 0
        return True, i
    except OverflowError:
        return False, 0

def trace(taille):
    image=np.ndarray((taille,taille,3),np.uint8)
    k,t=0,0
    for i in range(taille):
        for j in range(taille):
            x=-1+2*j/(taille-1)
            y=1-2*i/(taille-1)
            z=x+y*1.j
            v,n = conv(z)
            if v:
                image[i,j]=[int(6*n),int(7*n), int(255-5*n)]
                t+=n
                k+=1
            else:
                image[i,j]=[15,15,15]
    print(t/k)
    plt.imsave('mafrac.png', image)
    plt.imshow(image)
    plt.show()

trace(40000)
