# Recommender_systems

## Retailrocket recommender system dataset

Data source:
https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset/data
Files:
- Items_properties_1.csv
- Items_properties_2.csv
- Categoty_tree.csv
- Events.csv
The aim is to evaluate 3 different approaches for Recommender systems.
- Item Based Collaborative

  o Cosine Similarity

  o Euclidian Distance

  o Pearson Korrelation
- Matrix Factorization Based Collaborative

  o optimization function (SGD)

  o optimization function (ALS)
- Content Based

  o Cosine Similarity
- Hybrid 1 weighted

  o Mix of Item Based Collaborative & Content Based
- Hybrid 2 switching

  o Mix of MF & CBF

The Evaluation should be done with Loocv for top N Recommendations (5,10,15)
