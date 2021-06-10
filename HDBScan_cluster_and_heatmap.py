import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import hdbscan
import seaborn as sns
import plotly
import plotly.express as px

loc_df = pd.read_csv("Florida_Insurance_data.csv")
loc_df = loc_df[['point_latitude','point_longitude']]

def get_points_inside_box(df, box):
    return df.loc[(df['point_longitude']>box[0][0]) & (df['point_longitude']<box[1][0])
                  & (df['point_latitude']>box[0][1]) & (df['point_latitude']<box[1][1])]

#enter your access token below
px.set_mapbox_access_token('access_token')


def get_cluster_map(locations, bounding_box):
    loc_filtered = get_points_inside_box(locations, bounding_box)
    print(loc_filtered.shape)
    clusterer = hdbscan.HDBSCAN(min_cluster_size=10, metric='haversine')
    cluster_labels = clusterer.fit_predict(np.radians(loc_filtered[['point_latitude', 'point_longitude']]))
    loc_filtered['cluster'] = cluster_labels
    cluster_count = pd.DataFrame(loc_filtered.groupby('cluster')['point_latitude']
                                 .agg('count')).reset_index().rename(columns={'point_latitude': 'Count'})
    cluster_lat_mean = pd.DataFrame(loc_filtered.groupby('cluster')['point_latitude']
                                    .agg('mean')).reset_index().rename(columns={'point_latitude': 'Latitude'})
    cluster_lon_mean = pd.DataFrame(loc_filtered.groupby('cluster')['point_longitude']
                                    .agg('mean')).reset_index().rename(columns={'point_longitude': 'Longitude'})
    cluster = cluster_count.merge(cluster_lat_mean, on='cluster').merge(cluster_lon_mean, on='cluster')

    print(cluster.head())

    fig = px.scatter_mapbox(cluster.loc[cluster['cluster'] > -1], lat="Latitude", lon="Longitude", size='Count',
                            color='Count', color_continuous_scale=px.colors.sequential.Aggrnyl, zoom=10)

    return fig

florida_box = [(-88,24), (-76,30)]
miami_box = [(-81.22,25.5), (-79.8,26.2)]

out_map = get_cluster_map(loc_df, florida_box)
out_map.show()
plotly.offline.plot(out_map, filename='florida_heatmap.html')

out_map = get_cluster_map(loc_df, miami_box)
out_map.show()
plotly.offline.plot(out_map, filename='miami_heatmap.html')
