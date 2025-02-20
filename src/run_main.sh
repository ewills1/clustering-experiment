#!/bin/bash
#SBATCH --job-name=clustering_experiment
#SBATCH --output=clustering_experiment.out
#SBATCH --error=clustering_experiment.err
#SBATCH --output=clustering_experiment.out
#SBATCH --error=clustering_experiment.err
#SBATCH --time=01:00:00  # Set the maximum runtime
#SBATCH --mail-user=ewills1@sheffield.ac.uk

# Load necessary modules
module load Anaconda3/2024.02-1  # Adjust the Python version as needed
module load cuda/11.2  # Adjust the CUDA version as needed
module load dissertation-experiment1

source activate mynumpy # Activate the virtual environment

# Run the Python script
srun python ~/dissertation-experiment1/src/main.py
