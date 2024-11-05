import pandas as pd
import numpy as np
import sys
print(sys.executable)

# Generate random data
np.random.seed(42)
n_samples = 100
X = np.random.rand(n_samples, 5)  # 5 features
y = np.random.rand(n_samples)  # Target variable

# Create DataFrame
data = pd.DataFrame(X, columns=[f'Feature_{i+1}' for i in range(5)])
data['Target'] = y
print(data)

# Save to CSV
data.to_csv('synthetic_data.csv', index=False)

print("Synthetic dataset saved as 'synthetic_data.csv'")
