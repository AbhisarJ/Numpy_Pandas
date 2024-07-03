import numpy as np
from numpy import random

x= random.randint(100)
print(x)

listt = np.array(['Hello', 'Goodbye', 'Bye', 'Ciao'])
x= random.choice(listt)
print(x)

#actully shuffling the array
random.shuffle(listt)
print(listt)

#only for viewing a random arrangement of the array elements
print(random.permutation(listt))

import seaborn as sns
import matplotlib.pyplot as plt

sns.displot([1,6,8,33,2] , hist = False)

plt.show()