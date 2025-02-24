#!/bin/bash
#SBATCH --job-name=clustering_experiment
#SBATCH --output=clustering_experiment.out
#SBATCH --error=clustering_experiment.err
#SBATCH --time=01:00:00  # Set the maximum runtime
#SBATCH --partition=gpu  # Adjust based on your cluster
#SBATCH --qos=gpu
#SBATCH --mem=82G
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --gres=gpu:1  # Request 1 GPU
#SBATCH --mail-user=ewills1@sheffield.ac.
#SBATCH --mail-type=END,FAIL  # Get notified on job completion/failure

# Load necessary modules
module load Anaconda3/2024.02-1  # Adjust the Python version as needed
module load cuda/11.2  # Adjust the CUDA version as needed

conda activate mynumpy # Activate the virtual environment

# Run the Python script
srun --exclusive python ~/clustering-experiment/src/main.py
