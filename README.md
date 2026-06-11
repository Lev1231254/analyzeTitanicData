# Analyze Titanic Data

This educational project explores the Titanic Dataset and builds a ML model that predicts the passanger's probability of survival.
The complete analysis is available in the Jupyter notebook `analysis.ipynb`

The final model achieved mean test accuracy of approximately 82.5%

<img width="554" height="455" alt="изображение" src="https://github.com/user-attachments/assets/5174d693-d249-42b5-94dc-a84712f15710" />




# Installation
### Requirements

* Python 3.10 or newer

### Windows
```powershell
git clone https://github.com/Lev1231254/analyzeTitanicData.git
cd analyzeTitanicData
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```
Open `analysis.ipynb` and run all cells.

### Linux
```bash
git clone https://github.com/Lev1231254/analyzeTitanicData.git
cd <analyzeTitanicData
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
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
- Features, that correlate to survival the most:
  - Passenger class
  - Sex
  - Age
  - Amount of children and parents
  - Fare
  - Adult male
  - Being alone
- Best-performing model: RandomForestClassifier
- Achieved approximately 82% accuracy after Hyperparameter tuning
  
  <img width="562" height="455" alt="изображение" src="https://github.com/user-attachments/assets/c4b30a3d-d648-4355-b14c-17e89aede680" />

  
