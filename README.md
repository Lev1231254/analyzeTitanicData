# Description

This educational project explores the Titanic Dataset and builds a ML model that predicts the passanger's probability of survival.
The complete analysis is available in the Jupyter notebook `analysis.ipynb`

The final model achieved mean test accuracy of approximately 82.7%

<img width="562" height="455" alt="изображение" src="https://github.com/user-attachments/assets/cefcb446-c8cb-49a6-b479-17a222b0bdca" />




# Installation
### Requirements

* Python 3.10 or newer
* Git

### Windows
```powershell
git clone https://github.com/Lev1231254/analyzeTitanicData.git
cd analyzeTitanicData
python -m venv .venv
.venv\Scripts\activate
jupyter notebook
```
Open `analysis.ipynb` and run all cells.

### Linux
```bash
git clone https://github.com/Lev1231254/analyzeTitanicData.git
cd <analyzeTitanicData
python3 -m venv .venv
source .venv/bin/activate
jupyter notebook
```
Open `analysis.ipynb` and run all cells.




# Details
### Goals

- Visualize the dataset
- Draw conclusions from the data
- Find the best model for predicting passenger survival

### Technologies used

- Data visualization with the Seaborn library
- Scikit-learn pipelines
- Bayesian hyperparameter optimization
- Decision Tree and Random Forest classification models

### Results

- Best-performing model: RandomForestClassifier
- Achieved approximately 82% accuracy on unseen data
- Achieved approximately 83% accuracy during cross validation
