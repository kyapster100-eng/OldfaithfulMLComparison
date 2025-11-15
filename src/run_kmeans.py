import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

print("--- Running K-Means Model ---")

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

# 2. Create the K-Means model
# We tell it to find 2 clusters
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10) 

# 3. "Fit" the model to the data
kmeans.fit(X)

# 4. Get the cluster assignments (labels) for each data point
kmeans_labels = kmeans.labels_

# 5. Plot the results
plt.scatter(X[:, 1], X[:, 0], c=kmeans_labels, cmap='viridis') # X-axis: waiting, Y-axis: eruptions
plt.title('K-Means Clustering Results')
plt.xlabel('Waiting Time (mins)')
plt.ylabel('Eruption Duration (mins)')

# 6. Save the plot
# This saves the image to your main project folder
plt.savefig('kmeans_plot.png')
print("K-Means plot saved as kmeans_plot.png")