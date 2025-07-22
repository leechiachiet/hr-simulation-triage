import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
num_patients = 1000
min_hr = 30   # bpm
max_hr = 150  # bpm
sigma = 3     # standard deviation for Gaussian noise

# Generate uniformly distributed HR
hr_base = np.random.uniform(min_hr, max_hr, num_patients)

# Add Gaussian noise to simulate sensor jitter
hr_noisy = hr_base + np.random.normal(0, sigma, num_patients)

# Create DataFrame
df = pd.DataFrame({
    'patient_id': range(1, num_patients + 1),
    'hr_clean': np.round(hr_base, 2),
    'hr_noisy': np.round(hr_noisy, 2)
})

# Save to CSV
df.to_csv('synthetic_hr_dataset.csv', index=False)
print("Synthetic HR dataset saved as 'synthetic_hr_dataset.csv'")
