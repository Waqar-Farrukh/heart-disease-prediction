# Task 2: Heart Disease Prediction

**Live application:** https://heart-disease-prediction-mlf.streamlit.app/  
**GitHub repository:** https://github.com/Waqar-Farrukh/heart-disease-prediction

## Project summary

This project uses the UCI Cleveland Heart Disease dataset to build a binary classifier with four inputs: `age`, `cp`, `thalach`, and `exang`. The original target values are grouped as 0 (disease absent) and 1 (disease present).

- Dataset size: 303 rows
- Training/testing split: 242/61 rows
- Model: `StandardScaler` + `SVC` pipeline
- Test accuracy: 78.69% (48 of 61 test examples)

The model is an educational exercise and is not intended for medical diagnosis.

## Required submission files

- `Heart_Disease_Prediction.ipynb` — data loading, preprocessing, EDA, training, evaluation, predictions and review.
- `processed_cleveland.csv` — dataset used in the notebook.
- `heart_disease_model.pkl` — saved trained pipeline.
- `Heart_Disease_Report.pdf` — PDF export of the notebook.

The ZIP also includes the Streamlit app, requirements, and supporting result files.

## Run the Streamlit app locally

Use Python 3.12. From this directory, run:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Run the notebook

Install the packages listed in `requirements-notebook.txt`, open `Heart_Disease_Prediction.ipynb`, and run the cells from top to bottom. Keep the notebook and data files in the same directory.

## Feedback status

The notebook reviews held-out test results. External user feedback has not been collected. If the instructor specifically requires real user feedback, ask a classmate or instructor to try the app and record their genuine comments and any changes made.

## Dataset source

Janosi, Steinbrunn, Pfisterer and Detrano, *Heart Disease*, UCI Machine Learning Repository, https://doi.org/10.24432/C52P4X (CC BY 4.0).
