import pandas as pd
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

print("--- Running GMM Model ---")

# 1. Load the data
data_url = "https://www.stat.cmu.edu/~larry/all-of-statistics/=data/faithful.dat"
try:
    df = pd.read_csv(data_url, delim_whitespace=True, skiprows=26, names=['index', 'eruptions', 'waiting'])
    df = df.drop(columns=['index'])
    # Get just the data (eruptions and waiting) as a NumPy array
    X = df.values
    print("Data loaded successfully.")
except Exception as e:
    print(f"Error loading data: {e}")
    exit() # Exit the script if data can't be loaded

# 2. Create the GMM model
# We tell it to find 2 components
gmm = GaussianMixture(n_components=2, random_state=42)

# 3. "Fit" the model
gmm.fit(X)

# 4. Get the cluster assignments using 'predict'
gmm_labels = gmm.predict(X)

# 5. Plot the results
plt.scatter(X[:, 1], X[:, 0], c=gmm_labels, cmap='viridis') # X-axis: waiting, Y-axis: eruptions
plt.title('GMM Clustering Results')
plt.xlabel('Waiting Time (mins)')
plt.ylabel('Eruption Duration (mins)')

# 6. Save the plot
plt.savefig('gmm_plot.png')
print("GMM plot saved as gmm_plot.png")