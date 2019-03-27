import matplotlib.pyplot as plt
import numpy as np

d = np.ones((20,101,3), dtype=int)

for n in range(100):
	d[:,n,0]=       2*n             
	d[:,n,1]=       255-6*np.sqrt(np.abs(255- 3*n)   )          
	d[:,n,2]=       7*n - np.log(n)                                 

plt.imshow(d)

plt.show()

