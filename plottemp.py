import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('./2020-8-11-data.csv')
date = data['date']
temp = data['temperature']

plt.plot(date, temp)
plt.show()
