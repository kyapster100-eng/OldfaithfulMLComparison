GMM vs K-Means on Old Faithful ⛲
📌 Overview
This project explores clustering techniques on the classic Old Faithful geyser dataset, which records eruption durations and waiting times between eruptions. We compare two popular unsupervised learning algorithms:

K-Means Clustering: A partition-based method that minimizes within-cluster variance.

Gaussian Mixture Models (GMM): A probabilistic approach that models data as a mixture of Gaussian distributions.

The goal is to visualize and understand how these algorithms perform on the same dataset, highlighting their strengths and limitations.

📊 Dataset
Source: Old Faithful geyser dataset (commonly available in R and Python libraries).

Features:

eruption duration (minutes)

waiting time (minutes until next eruption)

⚙️ Methods
🔹 K-Means
Assumes spherical clusters of equal variance.

Assigns each point to the nearest cluster centroid.

Fast and simple, but less flexible for irregular cluster shapes.

🔹 Gaussian Mixture Models (GMM)
Uses Expectation-Maximization (EM) to estimate parameters.

Allows clusters with different shapes, sizes, and orientations.

Provides soft clustering (probability of belonging to each cluster).

📈 Results
K-Means tends to split the dataset into rigid partitions.

GMM adapts better to the natural distribution of the data, capturing overlapping clusters.

Visualizations show that GMM provides smoother decision boundaries compared to K-Means.

🖼️ Visualizations
Scatter plots of eruption duration vs waiting time.

Cluster assignments from K-Means and GMM.

Comparison of decision boundaries.

🚀 How to Run
bash
# Clone the repository
git clone https://github.com/your-username/old-faithful-clustering.git
cd old-faithful-clustering

# Install dependencies
pip install -r requirements.txt

# Run the notebook
jupyter notebook OldFaithful_GMM_vs_KMeans.ipynb
📦 Dependencies
Python 3.x

NumPy

Pandas

Matplotlib / Seaborn

scikit-learn

📚 References
Old Faithful dataset: R Documentation

K-Means algorithm: MacQueen (1967)

Gaussian Mixture Models: Dempster et al. (1977)

📝 License
This project is licensed under the MIT License.

✨ With this README, your repo will look professional and informative. Do you want me to also generate sample plots (K-Means vs GMM clustering on Old Faithful) so you can include them in the README?
