import numpy as np
import matplotlib.pyplot as plt

def julia(z, c, e=2):
    k=1
    while k<= 100:
        if np.abs(z)>e:
            return False,k
        else:
            z=z**2+c
            k+=1
    return True, 100

def trace_julia(c,I1,I2,pix):
    graph = np.dot(np.ones((pix,1)),[np.linspace(I1[0],I1[1],pix)])+1j*np.dot(np.array([np.linspace(I2[1],I2[0],pix)]).T, np.ones((1,pix)))
    ens = np.vectorize(trace)(graph, True, c)
    img = np.ones((pix,pix,3),dtype=int)
    img[:,:,0]=ens[0]
    img[:,:,1]=ens[1]
    img[:,:,2]=ens[2]

    return img

def trace(M, couleur = False, c=(-0.85+0.2*1j)):
    a = julia(M,c)

    if a[0] == True:
        return (255,220,255)
    elif couleur == False:
        return (200,200,200)

    else:
        n=a[1]
        return (3*n, int(0.5*n), int(255/n))




#plt.figure()
#plt.imshow(trace_julia((0.284-0.0122*1j),[-1.5,1.5],[-1.5,1.5], 2000))
#plt.figure()
#plt.imshow(trace_julia((0.382+0.147*1j),[-1.5,1.5],[-1.5,1.5], 2000))
#plt.imsave('la2.png', trace_julia((0.382+0.147*1j),[-1.5,1.5],[-1.5,1.5], 10000))
#plt.figure()
#plt.imshow(trace_julia((-0.181-0.667*1j),[-1.5,1.5],[-1.5,1.5], 2000))
#plt.figure()
#plt.imshow(trace_julia((-0.0958+0.735*1j),[-1.5,1.5],[-1.5,1.5], 2000))
#plt.figure()
#plt.imshow(trace_julia((-0.1011+0.9563*1j),[-1.5,1.5],[-1.5,1.5], 2000))
#plt.figure()
#plt.imsave('woww.png', trace_julia((-0.1528+1.0397*1j),[-0.4,0.4],[-0.4,0.4], 10000))
#plt.figure()
plt.imshow(trace_julia((-0.4+0.6*1j),[-1.5,1.5],[-1.5,1.5], 500))
#plt.figure()
#plt.imshow(trace_julia((-1.75487),[-1.5,1.5],[-1.5,1.5], 2000))

plt.show()

#'w2.png',
#int(200-9*np.sqrt(np.abs(255- 3*n)))
