# AutoPredictor

Vehicle Price Prediction using Machine Learning Techniques

## Description

This project aims to predict car prices using machine learning algorithms. It analyzes the effectiveness of different algorithms in accurately estimating car prices based on a dataset.

The dataset is preprocessed to handle missing values, external factors, and categorical variables. The research examines eight different machine learning algorithms: XGBoosting Regression, Linear Regression, Support Vector Regression (SVR), Random Forest, Long Short-Term Memory (LSTM), k-Nearest Neighbors (KNN). Neural Network and Decision Tree.

The performance of each algorithm is evaluated by splitting the dataset into training and testing sets. Metrics such as Mean Square Error (MSE) and Coefficient of Determination (R-squared) are used to measure accuracy.

## Installation

1. Clone the repository: `git clone https://github.com/anish0m/Autopredictor.git`
2. Install the required dependencies: `pip install -r requirements.txt`

## Usage

1. Load the dataset into the project.
2. Preprocess the dataset to handle missing values, categorical variables, and other data cleaning steps.
3. Split the dataset into training and testing sets.
4. Run the machine learning algorithms on the preprocessed data.
5. Evaluate the performance of each algorithm using metrics like MSE, RMSE, and R-squared.
6. Analyze the results and compare the accuracy of different algorithms.
7. Visualize the results using scatter plots, line plots, or any other suitable visualization methods.

## Results

The project's results show the performance of each algorithm in predicting car prices. The accuracy of the algorithms is evaluated using metrics like MSE, RMSE, and R-squared. The findings indicate the top-performing algorithms and provide insights into their effectiveness.

| Algorithm              | MSE             | RMSE       | R-squared |
|------------------------|-----------------|------------|-----------|
| XGBoost Regression     | 3,892,578.25    | 1,973.84   | 0.95      |
| Linear Regression      | 17,452,554      | 4,178.48   | 0.79      |
| SVR                    | 70,802,746      | 8,415      | 0.15      |
| Random Forest          | 5,881,171.58    | 2,425.67   | 0.95      |
| LSTM                   | 4.089e+18       | 2.022e+09  | -1.25     |
| KNN                    | 35,099,041      | 5,921.41   | 0.57      |
| Decision Tree          | 5,750,264.18    | 2,397.97   | 0.93      |
| Neural Network         | 11,741,104.03   | 3,426.52   | 0.87      |


## Contributing

Contributions to this project are welcome. You can contribute by following these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make changes and commit them: `git commit -m 'Add your feature'`
4. Push the changes to your forked repository: `git push origin feature/your-feature-name`
5. Submit a pull request.


