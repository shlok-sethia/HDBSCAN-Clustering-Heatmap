<h1 align= "center">Heatmaps using HDBScan Clustering</h1>

![Issues](https://img.shields.io/github/issues/shloksethia-6119/Clustering-Heatmap)
[![License](https://img.shields.io/github/license/shloksethia-6119/Clustering-Heatmap)](https://github.com/shloksethia-6119/Clustering-Heatmap/blob/master/LICENSE)


HDBSCAN - Hierarchical Density-Based Spatial Clustering of Applications with Noise. Performs DBSCAN over varying epsilon values and integrates the result to find a clustering that gives the best stability over epsilon. This allows HDBSCAN to find clusters of varying densities (unlike DBSCAN), and be more robust to parameter selection.

In practice this means that HDBSCAN returns a good clustering straight away with little or no parameter tuning -- and the primary parameter, minimum cluster size, is intuitive and easy to select.

# Clustering
Using Florida Property Insurance data to identify red hot and cold blue areas for potential targeting.  

# Florida Heatmap using HDBSCAN Clustering and Basemap
To view the output "Florida Heatmap" click on To view this file go to https://shloksethia-6119.github.io/Clustering-Heatmap/Heatmaps/florida_heatmap.html

Clearly, Miami is the hotspot for Property Insurance as seen above. To get a better picture we focus on Miami and generate a focused heatmap.
To view the output "Miami Heatmap" click on To view this file go to https://shloksethia-6119.github.io/Clustering-Heatmap/Heatmaps/miami_heatmap.html
