# Forest Cover Type Prediction

## Project Overview

This project develops a Machine Learning based Forest Cover Type Prediction system to classify the type of forest cover using geographical and environmental features collected from forest regions.

## Objective

The primary objective of this project is to develop a machine learning model that can accurately predict forest cover types while identifying the most effective classification algorithm for the problem.

## Dataset Information

* Total Records: **15,120**
* Total Features: **55**
* Target Variable: **Cover_Type**

### Forest Cover Classes

* `1` → Spruce/Fir
* `2` → Lodgepole Pine
* `3` → Ponderosa Pine
* `4` → Cottonwood/Willow
* `5` → Aspen
* `6` → Douglas-fir
* `7` → Krummholz

## Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

## Methodology

The following steps were followed during the development of the project:

1. Data Overview
2. Data Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature and Target Separation
5. Train-Test Split
6. Model Training and Evaluation
   - Logistic Regression
   - Decision Tree Classifier
   - Random Forest Classifier
   - Support Vector Classifier (SVC)
7. Model Comparison

## Model Performance

| Model | Accuracy | Precision | Recall | F1 Score |
|-------|----------|-----------|--------|----------|
| Logistic Regression | 0.6918 | 0.6888 | 0.6918 | 0.6891 |
| Decision Tree Classifier | 0.7903 | 0.7896 | 0.7903 | 0.7898 |
| Random Forest Classifier | 0.8552 | 0.8522 | 0.8552 | 0.8524 |
| Support Vector Classifier (SVC) | 0.7272 | 0.7245 | 0.7272 | 0.7241 |

## Final Model Selection

Logistic Regression, Decision Tree Classifier, Random Forest Classifier, and Support Vector Classifier (SVC) models were trained and evaluated for forest cover prediction.

Among all the models, the Random Forest Classifier achieved the highest accuracy, precision, recall, and F1-score values while correctly classifying the majority of forest cover types across all seven classes.

The model achieved an accuracy of **85.52%** and produced the fewest misclassifications compared to the other evaluated models.

Since accurately identifying forest cover types is important for environmental monitoring, land management, and ecological analysis, the **Random Forest Classifier** was selected as the final model for Forest Cover Type Prediction.

## Conclusion

A Forest Cover Prediction system was successfully developed and multiple machine learning algorithms were trained and evaluated for classification performance.
The developed system can assist in predicting forest cover types using geographical and environmental attributes, thereby supporting forest management, ecological studies, and environmental monitoring applications.
