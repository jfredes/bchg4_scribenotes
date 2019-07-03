import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(777)

x = 100 + 15 * np.random.randn(437)
plt.figure(1)
sns.distplot(x)
plt.draw()

y = 90 + 25 * np.random.randn(437)
plt.figure(2)
sns.distplot(y)

plt.show()
