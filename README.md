![Alt Text](https://static.independent.co.uk/s3fs-public/thumbnails/image/2020/05/14/13/istock-1138180728.jpg)

# Streaming killed the video star?
### Spotify popularity prediction
Author: Vivika Wilde (wilde.vivika@gmail.com)

The times of video killed the radio star are clearly over but what is it that makes stars nowadays? Attempting to find an answer to this question I have looked at Spotify data from the past 100 years and more specifically tracks from 2019. Using machine learning algorithms popularity was predicted both continuously and in binary classes. Finally, clustering was used to find similarities that could be used in a recommender system.

The data used in this project was found on kaggle (https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks/tasks?taskId=969) and via the Spotify API.


## Steps
- [x] Data mining via kaggle & Spotify's API
- [x] Data Cleaning 
- [x] EDA for both datasets & feature engineering
- [x] Predictive modelling on continuous target
- [x] Predictive modelling on binary target
- [x] Interactive app estimating a tracks popularity based on inputs and showing similar tracks.

## Future Work
#### Model Performance
Improve accuracy of the predictive models (both regression classification) by adding features
#### Generalisability
Use time-series data to  be able to generalise over time (i.e. predict popularity at the time) determine long-term successes.
#### Supervised Clustering
Train a supervised machine learning model (e.g. using user data) to create a recommendation system


## Files and Folders
|File| Description|
|:---|:---|
|Spotify1_100yrs_EDA_200812.ipynb| Jupyter Notebook with Exploratory Data Analysis (EDA) on the dataset taken from Kaggle which comprises of tracks from the past 100 years|
|Spotify2_Additional_Data_200812.ipynb| Jupyter Notebook with code that retrieves data via the Spotify API|
|Spotify3_2019_EDA_200812.ipynb| Jupyter Notebook with Exploratory Data Analysis (EDA) on the second dataset, that includes tracks released 2019|
|Spotify4_Regression_200812.ipynb| Jupyter Notebook containing machine learning algorithms to predict the continuous target|
|Spotify5_Classification_200812.ipynb| Jupyter Notebook containing machine learning algorithms to predict the binary target |
|Spotify6_Clustering_200812.ipynb| Jupyter Notebook containing clustering methods|
|Weights-010--7.24545.hdf5 | File containing the optimal weights for neural network (from regression)
| Pickles folder| Folder containing saved models |
| plotting.py| Auxiliary plotting functions for EDA |
| Figures folder| Folder containing all figures generated in the course of this project |
| App folder| Folder containing files for the interactive dash application |
| Spotify_Popularity_Presentation.pdf| The set of slides used to present the project|




