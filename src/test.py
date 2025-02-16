from sentence_transformers import SentenceTransformer
import matplotlib.pyplot as plt
import numpy as np

# Load embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Example topics from LLM
topics = ["Football", "Canadian Maple Syrup", "Russian Revolution"]

# Convert topics to embeddings
topic_embeddings = embedder.encode(topics)

# Reduce to 2D
reducer = umap.UMAP(n_components=2)
topics_2D = reducer.fit_transform(topic_embeddings)

fig = plt.figure()
fig, ax = plt.subplots()
