#!/bin/bash
#SBATCH --job-name=clustering_experiment
#SBATCH --output=clustering_experiment.out
#SBATCH --error=clustering_experiment.err
#SBATCH --time=01:00:00  # Set the maximum runtime
#SBATCH --partition=compute  # Specify the partition/queue
#SBATCH --nodes=1  # Number of nodes
#SBATCH --ntasks=1  # Number of tasks
#SBATCH --cpus-per-task=4  # Number of CPU cores per task
#SBATCH --gres=gpu:1  # Request one GPU

# Load necessary modules
module load python/3.8  # Adjust the Python version as needed
module load cuda/11.2  # Adjust the CUDA version as needed
module /c:/Users/Ed/Documents/Dissertation/clustering-experiment/src

# Run the Python script
python /c:/Users/Ed/Documents/Dissertation/clustering-experiment/src/main.py 