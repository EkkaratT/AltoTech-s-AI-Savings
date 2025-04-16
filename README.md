# ⚡ AltoTech AI Savings



## Overview

This project evaluates the energy consumption of plants **before and after** the installation of the **AltoTech AI system**. By integrating weather data, the project explores how **external weather conditions influence energy usage** and examines whether the AltoTech AI system contributes to **energy savings**.

The goal is to assess the system's effectiveness in **reducing energy consumption** by comparing data from the period before and after its installation.

---

## Key Objectives

- **Evaluate energy savings**  
  Analyze the reduction in energy consumption after implementing the AltoTech AI system.

- **Assess the impact of weather conditions**  
  Investigate how variables like **temperature**, **humidity**, **wind speed**, and **UV index** affect energy usage.

- **Compare predictive models**  
  Evaluate the performance of different **regression models** in predicting energy consumption and energy savings.

---

## Datasets Used

The project combines **energy consumption** and **weather data** to assess energy usage trends:

### 🔹 `before_ai_plant_data.csv`
- Contains energy consumption data **before** the installation of the AltoTech AI system.
- Includes **timestamps** and **energy consumption values** for each time period.

### 🔹 `after_ai_plant_data.csv`
- Contains energy consumption data **after** the installation of the AltoTech AI system.
- Uses the **same structure** as the "before" data for easy comparison.

### 🔹 `weather_data_Thailand.csv`
- Weather data from **Thailand**, including:
  - Temperature
  - Humidity
  - Feelslike
  - Wind speed
  - UV index
- This data was obtained from **Visual Crossing** and is **time-matched** with the energy consumption data.

---

## Steps Involved

### 1. Loading and Cleaning the Data
- Import datasets and rename columns for consistency.
- Check for **missing values** or **data anomalies** to ensure data quality.

### 2. Exploring the Data
- Visualize **energy consumption trends** before and after AI installation.
- Plot **weather trends** to see how weather patterns align with energy usage.

### 3. Merging the Data
- Merge energy and weather datasets using **common date columns**.
- Create a combined dataset to analyze **weather–energy relationships**.

### 4. Data Preprocessing
- **Scale numerical features** for consistency and better model performance.
- Add **sine and cosine transformations** to capture **monthly seasonality**.
- Split data into **training and testing sets** for evaluation.

### 5. Modeling
- Build and compare the performance of different regression models:
  - Linear Regression
  - Ridge Regression
  - Random Forest
  - Gradient Boosting

### 6. Evaluation
- Use **cross-validation** to evaluate model performance.
- Metrics used:
  - **Root Mean Squared Error (RMSE)**
  - **R² (Coefficient of Determination)**
  - **Coefficient of Variation RMSE (CVRMSE)**
  - **Normalized Mean Bias Error (NMBE)**

## Features of the Application

### Energy Predictions
- Compares **real-time predicted** vs. **actual energy consumption** for the plant.
- Helps users understand how well the models perform in forecasting energy usage.

### KPI Display
Displays key performance indicators, including:
- **Total predicted energy**
- **Actual energy consumption**
- **Savings in kWh**
- **Savings percentage**
- **Estimated cost savings** in Thai Baht (THB)

### 🌤️ Weather Trends
- Visualizes key weather conditions over time:
  - Temperature
  - Humidity
  - Feelslike
  - Wind speed
  - UV index
- Allows users to explore how **weather affects energy consumption and savings**.

### Model Metrics
- Shows performance metrics for each model:
  - **R²** (coefficient of determination)
  - **RMSE** (Root Mean Square Error)
  - **CVRMSE** (Coefficient of Variation of RMSE)
  - **NMBE** (Normalized Mean Bias Error)
- Helps users evaluate **model accuracy and reliability**.

### 📉 Energy Visualization
- Interactive graphs allow users to:
  - Explore **energy trends over time**
  - Compare **weather conditions** and **energy consumption**
  - Understand the **impact of AltoTech AI** on reducing energy usage

## Installation / Setup

### 💻 Local Setup

#### 1. Clone the repository:
```bash
git clone <repo_url>
cd <repo_directory>
```

#### 2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

#### 3. Run the app:
Start the Dash app locally by running:
```bash
python app.py
```

#### 4. Access the app:
Open your browser and navigate to:
http://127.0.0.1:8050/ to view the dashboard.

---

### 🐳  Docker Setup

#### 1. Build the Docker image:
In the project directory, run:
```bash
docker build -t energy-savings-dashboard .
```

#### 2. Run the Docker container:
After building the image, run the app in a container:
```bash
docker run -p 8050:8050 energy-savings-dashboard
```

#### 3. Access the app:
Open your browser and go to:
http://localhost:8050/ to see the dashboard running.
```bash
python app.py
```

---

## Model Explanation

This project evaluates different **regression models** to predict energy consumption and savings:

### 🔹 Linear Regression
A simple and interpretable model that serves as the **baseline**.

### 🔹 Ridge Regression
A variant of linear regression that includes **regularization** to prevent overfitting.

### 🔹 Random Forest
An **ensemble method** that builds multiple decision trees to capture **non-linear relationships** in the data.

### 🔹 Gradient Boosting
A **boosting method** that combines the predictions of many weak learners to improve accuracy.

---

## Model Evaluation Metrics

- **R² (Coefficient of Determination)**  
  Measures how well the model explains the **variance** in the energy consumption data.

- **RMSE (Root Mean Squared Error)**  
  Quantifies the **difference between predicted and actual values**, with lower values indicating better performance.

- **CVRMSE (Coefficient of Variation RMSE)**  
  Normalizes RMSE relative to the **mean**, allowing comparison across different models.

- **NMBE (Normalized Mean Bias Error)**  
  Measures **model bias** by comparing predicted and actual energy values.

---

## ⚡ Energy Savings Calculation

### 🔸 Predicted Energy Consumption (Before and After AI Installation)
- The trained models are used to predict energy consumption for both the **pre-AI** and **post-AI** periods.

### 🔸 Savings Calculation
- **Energy Savings (kWh)** = Difference between **actual consumption** and **predicted pre-AI consumption**.
- **Cost Savings (THB)** = Energy savings × Cost per unit of energy.

By comparing the predicted and actual energy usage **before and after** the AI system, the app displays:
- **Total energy savings**
- **Percentage savings**
- **Estimated cost savings in THB**

---

## 🌱 Future Considerations

### 🔄 IoT Integration & Daily Prediction Updates

Integrate **IoT sensors** within the plant to collect **real-time energy and environmental data** (e.g., temperature, humidity). This data can be used to **update energy consumption predictions daily**, ensuring the dashboard reflects the most **current conditions**.

This approach provides:
- **Timely insights**
- **Faster detection of inefficiencies**
- **More accurate, adaptive energy management**

By continuously updating energy predictions on a daily basis, the system ensures that plant operators are always working with the latest data to optimize energy usage effectively.



