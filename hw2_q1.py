import numpy as np
import matplotlib.pyplot as plt
K = np.arange(1, 10)
theta = np.arange(0.05, 1, 0.05)
N = 30


R = np.zeros((len(K), len(theta)))
for i in range(len(K)):
    rk = (K[i]-0.5)/K[i]
    for j in range(len(theta)):
        R[i, j] = np.log2(K[i])+N*(1-theta[j])*np.log2((1-theta[j])/(1-rk)) + \
            N*theta[j]*np.log2(theta[j]/rk)


print(R)

fig, ax = plt.subplots(1, 1)
img = ax.imshow(R)
# ax.set_xticks([-0.75, -0.25, 0.25, 0.75])
plt.imshow(R)
plt.show()
