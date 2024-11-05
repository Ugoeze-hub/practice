import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.boxplot(data, vert = True, patch_artist = True, labels = ['Group1', 'Group2', 'Group3'])
plt.ylabel('Values')
plt.title('Box Plot')
plt.show()