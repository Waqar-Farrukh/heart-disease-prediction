# Task 2: Heart Disease Prediction

Waqar Farrukh | FA24-BSE-118 | BSE-A

## Result

UCI Cleveland dataset: 303 rows. Inputs: age, cp, thalach, exang.
StandardScaler and SVC pipeline. Training: 242 rows. Testing: 61 rows.
Test accuracy: 78.69% (48 of 61 correct).

## GitHub

1. Open https://github.com/new and create a public repository named heart-disease-prediction.
2. Choose Upload files. Upload all files INSIDE this extracted folder, then Commit changes.
3. Confirm app.py, requirements.txt, results.json and heart_disease_model.pkl appear at the repository root.
4. Your repository link will be https://github.com/YOUR-USERNAME/heart-disease-prediction.

## Streamlit deployment

1. Open https://share.streamlit.io and sign in with GitHub.
2. Click Create app and choose to deploy an existing app from GitHub.
3. Repository: YOUR-USERNAME/heart-disease-prediction.
4. Branch: main. Main file path: app.py.
5. Advanced settings: select Python 3.12 and save.
6. Choose an available app URL, such as waqar-farrukh-heart-disease, and click Deploy.
7. Open the published app and test both examples below.
8. Replace the first notebook cell with your actual published URL and save the notebook. Upload the updated notebook to GitHub.

## Test examples

| Age | Chest pain | Maximum heart rate | Exercise-induced angina | Expected model output |
|---|---|---|---|---|
| 63 | Typical angina | 150 | No | Disease absent |
| 68 | Asymptomatic | 150 | Yes | Disease present |

Click Predict heart disease after changing inputs.

## Run locally on Windows

Install Python 3.12 first. Open Command Prompt in this folder.

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Run the notebook

In the activated environment:

```bat
python -m pip install -r requirements-notebook.txt
python -m ipykernel install --user --name heart-disease --display-name "Python Heart Disease"
python -m notebook
```

Open Heart_Disease_Prediction.ipynb, select Python Heart Disease, then Restart Kernel and Run All. Save the notebook. Keep all files in this folder. Notebook outputs are already included.

## Included files

- Heart_Disease_Prediction.ipynb: training, testing, application, feedback review and saved outputs.
- processed.cleveland.data: original UCI dataset.
- heart-disease-four-features.csv: selected inputs and target.
- sample-data-encoded-output.csv and sample-data-encoded.csv: encoded data.
- training-data-encoded.csv and testing-data-encoded.csv: data split.
- heart_disease_model.pkl: trained scaler and classifier.
- app.py: Streamlit prediction app.
- model-predictions.csv, results.json and confusion-matrix.png: evaluation outputs.
- feedback-review.csv: observations from test results.
- model_parameters.json: optional model parameter export.
- requirements.txt: app dependencies.
- requirements-notebook.txt: notebook dependencies.

## Before submission

1. Deploy the app and add the actual working URL at the very top of the notebook.
2. Ask a classmate or instructor to test the app. Record their actual feedback in Step 9.1 and any resulting improvement in Steps 9.2-9.3. The current feedback section contains a test-result review; external feedback has not been collected.
3. Upload the notebook, code, datasets and trained model to Google Classroom. Include the supporting result files.

## Sources

Adapted from the Titanic teaching notebooks by Mohsin Afzal and Dr. Rao Muhammad Adeel Nawab:
https://github.com/haqnawaz99/ml-teaching-notebooks

Janosi, Steinbrunn, Pfisterer and Detrano. Heart Disease. UCI Machine Learning Repository.
https://archive.ics.uci.edu/dataset/45/heart+disease
https://doi.org/10.24432/C52P4X
Dataset license: CC BY 4.0.
