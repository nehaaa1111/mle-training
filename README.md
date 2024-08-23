# Median housing value prediction

The housing data can be downloaded from https://raw.githubusercontent.com/ageron/handson-ml/master/. The script has codes to download the data. We have modelled the median house value on given housing data. 

The following techniques have been used: 

 - Linear regression
 - Decision Tree
 - Random Forest

## Steps performed
 - We prepare and clean the data. We check and impute for missing values.
 - Features are generated and the variables are checked for correlation.
 - Multiple sampling techinuqies are evaluated. The data set is split into train and test.
 - All the above said modelling techniques are tried and evaluated. The final metric used to evaluate is mean squared error.

## To excute the script
python nonstandardcode.py

## steps to run the code
1. Create required Anaconda environment conda create --name environmentName python=3 pandas numpy. Include all your dependencies at once while creating the environment.
2. Switch to the environment with conda activate environmentName.
3. Executing the python script python fileName.py. You don't have to specify the python version because the script is running inside the Anaconda environment. The version used will be whatever is specified in the environment (the script required python3 which has already been specified in Anaconda environment).

