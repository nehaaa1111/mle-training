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

## Installation
1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

2. Setup conda environment

conda env create -f env.yaml

3. Activate the environment

conda activate myenv

4. Install the package

pip install -e .

Run tests - pytest tests/

5. Running the Code
## Running the Code

1. **Ingest Data:**

- Use the `ingest_data.py` script to download and create training and validation datasets.

```bash
python src/your_package/ingest_data.py --output ./data

2. Run the train.py script to train your model. 

python src/your_package/train.py --input ./data --output ./artifacts

3. Score the Model:

python src/your_package/score.py --model ./artifacts --data ./data --output ./results


# mlflow-hands-on
