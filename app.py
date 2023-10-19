# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16DLahiCV2b55nAIZ62Gjm4TnDMTgzt2f
"""

import pandas as pd
from sklearn.cluster import KMeans
import altair as alt
from sklearn.preprocessing import StandardScaler

file_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter05/DataSet/german.data-numeric'

df = pd.read_csv(file_url, header=None, sep='\s\s+', prefix='X')

df.head()

X = df[['X3', 'X9']]

standard_scaler = StandardScaler()
X_scaled = standard_scaler.fit_transform(X)

clusters = pd.DataFrame()
inertia = []

clusters['cluster_range'] = range(1, 15)

for k in clusters['cluster_range']:
    kmeans = KMeans(n_clusters=k, random_state=8).fit(X_scaled)
    inertia.append(kmeans.inertia_)

clusters['inertia'] = inertia

clusters

alt.Chart(clusters).mark_line().encode(alt.X('cluster_range'), alt.Y('inertia'))

clusters_number = 5

kmeans = KMeans(random_state=1, n_clusters=clusters_number, init='k-means++', n_init=50, max_iter=1000)
kmeans.fit(X_scaled)

df['cluster'] = kmeans.predict(X_scaled)

scatter_plot = alt.Chart(df).mark_circle()
scatter_plot.encode(x='X3', y='X9',color='cluster:N')

