#!/bin/bash
#SBATCH --job-name=clustering_experiment
#SBATCH --nodes=1  # Number of nodes
#SBATCH --ntasks=1  # Number of tasks
#SBATCH --cpus-per-task=4  # Number of CPU cores per task
#SBATCH --mem=16G
#SBATCH --mem-per-cpu=16G
#SBATCH --output=clustering_experiment.out
#SBATCH --error=clustering_experiment.err
#SBATCH --time=01:00:00  # Set the maximum runtime
#SBATCH --mail-user=ewills1@sheffield.ac.uk

# Load necessary modules
module load python/3.8  # Adjust the Python version as needed
module load cuda/11.2  # Adjust the CUDA version as needed
module load dissertation-experiment1

# Run the Python script
python dissertation-experiment1/src/main.py
