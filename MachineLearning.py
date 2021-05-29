# A machine learning program comes in a number of steps

# 1. Import the Data, usually comes in .csv format
# 2. Clean the Data, like removing duplicate Data, irrelevant Data
# 3. Split the Data into Training/ Test Sets, perhaps 80% for training and 20 % for testing
# 4. Create a Model, decision tress/ neuro-networks / Psychic - good news we dont have to write machine learning algorithms there are libraries for them
# 5. Train the Model
# 6. Make predictions - not always accurate so #7
# 7. Evalute and Improve


####################### Libraries amd Tools ######################
# 1. Numpy  - a popular multi-dimensional array library
# 2. Pandas - data analysis  library that provides data frame (similar to Excel spreadsheets)
# 3. MatPlotLib - 2 dimensional plotting lib for creating graphs
# 4. Scikit-Learn - a popular ML lib hosting a number of ML models

#Jupyter is a Py notebook used to visualise Data, vs code and terminals sometimes can not support huge amounts of insterted Data hence Jupyter.

import pandas as pd  
df = pd.read_csv('vgsales.csv')
df