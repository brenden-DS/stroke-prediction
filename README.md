# Stroke Prediction Web App using Streamlit

This repository contains the code for a web application built with Streamlit for predicting the likelihood of a stroke based on various features. The app utilizes a machine learning model trained on a dataset with several features related to health and lifestyle.

## Features in the Dataset
The dataset used for training the model includes the following features:

1. **Age**: The age of the individual.
2. **Hypertension**: Indicates whether the individual has hypertension (0 for no, 1 for yes).
3. **Heart Disease**: Indicates whether the individual has heart disease (0 for no, 1 for yes).
4. **Marital Status**: The marital status of the individual.
5. **Work Type**: The type of work the individual is engaged in.
6. **Residence Type**: The type of residence (urban or rural).
7. **Average Glucose Level**: The average glucose level in the individual's blood.
8. **Body Mass Index (BMI)**: The body mass index of the individual.
9. **Smoking Status**: The individual's smoking status.
10. **Stroke**: The target variable indicating whether the individual had a stroke (0 for no, 1 for yes).

These features are used to predict the likelihood of a stroke for a given individual. The web app provides an intuitive interface for users to input their information and receive a prediction regarding their stroke risk.The dataset is publicly available on kaggle https://www.kaggle.com/datasets/jillanisofttech/brain-stroke-dataset
Here's a link to the web apphttps://stroke-prediction007.streamlit.app/


## Usage
To run the web app locally, make sure you have Streamlit installed. Then, simply run the following command:
```bash
streamlit run app.py
```

## Contributions
Contributions to improve the web app or the underlying machine learning model are welcome. Feel free to fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
A stroke prediction app using Streamlit is a user-friendly tool designed to assess an individual's risk of experiencing a stroke. By inputting relevant health data such as age, blood pressure, cholesterol levels, and lifestyle factors, the app utilizes predictive algorithms to calculate the user's likelihood of having a stroke. The app's intuitive interface and interactive features make it easy for users to understand their risk factors and take proactive measures to prevent stroke.


