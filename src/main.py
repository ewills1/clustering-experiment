from sklearn.datasets import fetch_20newsgroups
from sklearn.manifold import TSNE
from sklearn.cluster import DBSCAN
from sentence_transformers import SentenceTransformer
from llm import extract_topics
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
categories = ['sci.space', 'rec.sport.baseball', 'comp.graphics', 'talk.politics.mideast']
newsgroups = fetch_20newsgroups(subset='train', categories=categories, remove=('headers', 'footers', 'quotes'))

batch_size = 20
topic_list = []

# Extract topics from each newsgroup
for i in range(0, len(newsgroups.data), batch_size):
    batch = newsgroups.data[i:i + batch_size]
    topics_batch = extract_topics(batch)
    topic_list.extend(topics_batch)

model = SentenceTransformer('all-MiniLM-L6-v2')
topic_embeddings = model.encode(topic_list)

# Convert to numpy array
topic_embeddings_array = np.array(topic_embeddings)

# Dimensionality reduction using t-SNE
tsne = TSNE(n_components=2, random_state=42, perplexity=30, n_iter=1000)
X_reduced = tsne.fit_transform(topic_embeddings_array.reshape(-1, 1))

x = X_reduced[:, 0]  # First principal component
y = X_reduced[:, 1]  # Second principal component

# Apply DBSCAN
dbscan = DBSCAN(eps=0.1, min_samples=2)
clusters = dbscan.fit_predict(X_reduced)
print(clusters)

cluster_labels = dbscan.labels_
coords = clusters

no_clusters = len(np.unique(cluster_labels) )
no_noise = np.sum(np.array(cluster_labels) == -1, axis=0)

print('Estimated no. of clusters: %d' % no_clusters)
print('Estimated no. of noise points: %d' % no_noise)

# Visualize clusters
unique_labels = np.unique(cluster_labels)
colors = plt.cm.get_cmap('tab10', len(unique_labels))

plt.figure(figsize=(10, 8))
for label in unique_labels:
    label_mask = (cluster_labels == label)
    plt.scatter(x[label_mask], y[label_mask], color=colors[label], label=f'Cluster {label}' if label != -1 else 'Noise')


plt.title('DBSCAN Clustering of Newsgroups Data')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.legend()
plt.savefig('dbscan_clusters.png')

