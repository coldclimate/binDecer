#!/usr/bin/env python3

# written because one day I realised that all binary numbers could be read as decimal
# eg. 101 is both 5 and one hundred and one, then wondered what the relationship between them was like.

# https://hackaday.com/2019/03/07/make-xkcd-style-plots-from-python/

import numpy as np
import matplotlib.pyplot as plt



xs = []
ys = []
for counter in range(10000):
	xs.append(counter)
	ys.append(int(bin(counter)[2:]))

#print(xs)
#print(ys)

#x = np.linspace(0, 1, 100)
#y = 1+np.cos(x*18*np.pi)*0.75

plt.xkcd(scale=4, length=400)
plt.xticks([100,1000,10000,100000], rotation=60)
plt.yticks([10000], rotation=60)
#plt.minorticks_on()
plt.ylabel('decimal value')
plt.xlabel('binary number')
plt.plot(xs,ys)
#plt.axis([min(xs),max(xs),0,max(ys)])
#plt.gca().set_aspect(2*9/16)
plt.savefig('binaryDecimal.png', dpi=100)

