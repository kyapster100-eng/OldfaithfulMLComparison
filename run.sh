#!/bin/bash
# This line tells Linux to run this script using the bash shell

echo "--- Activating virtual environment ---"
# This makes sure the script uses your installed libraries
source venv/bin/activate

echo "--- Running K-Means Model ---"
# This runs your first python script
python src/run_kmeans.py

echo "--- Running GMM Model ---"
# This runs your second python script
python src/run_gmm.py

echo "--- Project run complete. Plots saved. ---"