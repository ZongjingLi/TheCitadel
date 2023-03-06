from icc import *

print(I ** 2)
print(log(E))

print(oo >= 1e9)

print(pi)
print(pi.evalf())

x,y = symbols("x y")

print(diff(cos(x),x))

pf = ParticleFilter(40)

import matplotlib.pyplot as plt

ims = text2img(["Hello there!"],[480,360])

plt.imshow(ims)
plt.show()