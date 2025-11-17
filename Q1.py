 ***Medical Diagnosis Using SVM
!pip install opencv-python

import os
import cv2
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# HOG descriptor from OpenCV
hog = cv2.HOGDescriptor()

# 1. Function to load images and extract HOG features
def load_images(path, label):
    data = []
    labels = []

    for file in os.listdir(path):
        img_path = os.path.join(path, file)

        img = cv2.imread(img_path)
        if img is None:
            continue
        
        img = cv2.resize(img, (128, 128))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Extract HOG features
        features = hog.compute(gray)
        features = features.flatten()

        data.append(features)
        labels.append(label)

    return data, labels


# Paths of your dataset folders
benign_path = "dataset/benign"
malignant_path = "dataset/malignant"

# 2. Load dataset
benign_data, benign_labels = load_images(benign_path, 0)
malignant_data, malignant_labels = load_images(malignant_path, 1)

# Combine data
X = np.array(benign_data + malignant_data)
y = np.array(benign_labels + malignant_labels)

# 3. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 4. Train SVM Model
model = SVC(kernel='linear')
model.fit(X_train, y_train)

# 5. Test Accuracy
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
------------------------------------------------------------------

***Loan Default Prediction with Decision Tree
Data Set:income,CreditScore,EmployementYears,Default
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# 1. Load dataset
data = pd.read_csv("loan_data.csv")

# 2. Features (X) and Target (y)
X = data[['Income', 'CreditScore', 'EmploymentYears']]
y = data['Default']

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Create Decision Tree model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 5. Predictions
y_pred = model.predict(X_test)

# 6. Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# 7. Visualize the decision tree
plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=['Income', 'CreditScore', 'EmploymentYears'], class_names=['No Default', 'Default'], filled=True)
plt.show()
-------------------------------------------------------------------
****Disease Classification with KNN

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 1. Load dataset
data = pd.read_csv("diabetes_data.csv")

# 2. Features and Target
X = data[['Glucose', 'BMI', 'Age']]
y = data['Diabetes']

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Create KNN model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# 5. Predictions
y_pred = model.predict(X_test)

# 6. Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# 7. Testing with new patient data
sample = [[140, 32.5, 45]]  # Glucose, BMI, Age
prediction = model.predict(sample)
print("Prediction for new patient:", "Diabetic" if prediction[0] == 1 else "Not Diabetic")
--------------------------------------------------------------------
***4. Email Spam Detection Using Naive Bayes
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# 1. Load dataset
data = pd.read_csv("spam_data.csv")

# 2. Features and Labels
X = data['text']
y = data['label']

# 3. Convert text into word frequency (Bag of Words)
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# 4. Train-Test split
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# 5. Train Naive Bayes Model
model = MultinomialNB()
model.fit(X_train, y_train)

# 6. Predictions
y_pred = model.predict(X_test)

# 7. Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# 8. Test new email
sample = ["Get free money by clicking here"]
sample_vectorized = vectorizer.transform(sample)
prediction = model.predict(sample_vectorized)
print("Prediction:", prediction[0])
------------------------------------------------------------
***Customer Sentiment Analysis with SVM
# Step 1: Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Step 2: Load Dataset
data = pd.read_csv("reviews.csv")

# Step 3: Split X and y
X = data['review']
y = data['sentiment']

# Step 4: Convert text into TF-IDF numbers
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Step 5: Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# Step 6: Train SVM Model
model = SVC(kernel='linear')
model.fit(X_train, y_train)

# Step 7: Make Predictions
y_pred = model.predict(X_test)

# Step 8: Check Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
---------------------------------------------------------
*** House Price Prediction Using Linear Regression
# Step 1: Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 2: Load Dataset
data = pd.read_csv("house_prices.csv")

# Step 3: Split into input(X) and output(y)
X = data[['location', 'size_sqft', 'amenities']]
y = data['price']

# Step 4: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Build Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Predict
y_pred = model.predict(X_test)

# Step 7: Evaluate the Model
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Step 8: Predict for new house
new_house = [[2, 1500, 3]]  # location=2, size=1500, amenities=3
predicted_price = model.predict(new_house)
print("Predicted Price (in lakhs):", predicted_price[0])
-------------------------------------------------------
***Churn Probability with Logistic Regression
# Step 1: Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 2: Load Dataset
data = pd.read_csv("telecom_churn.csv")

# Step 3: Select Features and Target
X = data[['usage_minutes', 'bill_amount', 'complaints']]
y = data['churn']

# Step 4: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Logistic Regression Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 6: Predictions
y_pred = model.predict(X_test)

# Step 7: Accuracy and Report
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Step 8: Predicting for new customer
new_customer = [[300, 650, 1]]   # 300 minutes, bill 650, 1 complaint
churn_prediction = model.predict(new_customer)

print("\nWill the customer churn? (1 = Yes, 0 = No):", churn_prediction[0])
------------------------------------------------------------------------
***Stock Price Forecasting with Least Squares
# Step 1: Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 2: Load Dataset
data = pd.read_csv("stock_data.csv")

# Step 3: Prepare Data
X = data[['day']]       # independent variable
y = data['price']       # dependent variable

# Step 4: Create Model
model = LinearRegression()
model.fit(X, y)

# Step 5: Predict Future Prices
future_days = np.array([[11], [12], [13], [14], [15]])
future_prices = model.predict(future_days)

# Step 6: Print Results
print("Predicted Prices for next 5 days:")
for d, p in zip(future_days, future_prices):
    print(f"Day {d[0]} → Price: {p:.2f}")

# Step 7: Plot Graph
plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.xlabel("Day")
plt.ylabel("Stock Price")
plt.title("Stock Price Forecast (Least Squares Regression)")
plt.show()
--------------------------------------------------------------
***Crop Yield Estimation Using Linear Regression
# Step 1: Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 2: Load Dataset
data = pd.read_csv("crop_yield.csv")

# Step 3: Prepare Data
X = data[['rainfall', 'temperature', 'soil_quality']]
y = data['yield']

# Step 4: Train Model
model = LinearRegression()
model.fit(X, y)

# Step 5: Predict Yield for New Input
# Example: Rainfall = 280mm, Temp = 24°C, Soil Quality = 8
new_data = np.array([[280, 24, 8]])
predicted_yield = model.predict(new_data)

print(f"Predicted Crop Yield: {predicted_yield[0]:.2f} kg/acre")

# Step 6: Show Model Accuracy (R² Score)
print("Model Accuracy (R² Score):", model.score(X, y))

# Step 7: Plot Actual vs Predicted
predicted = model.predict(X)
plt.scatter(y, predicted)
plt.xlabel("Actual Yield")
plt.ylabel("Predicted Yield")
plt.title("Actual vs Predicted Crop Yield")
plt.show()
-------------------------------------------------------------------
***Heart Disease Risk Prediction with Logistic Regression
# Step 1: Import Libraries
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 2: Load Dataset
data = pd.read_csv("heart_disease.csv")

# Step 3: Select Features and Target
X = data[['age', 'bp', 'cholesterol']]
y = data['risk']

# Step 4: Split Data (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Step 5: Train Logistic Regression Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 6: Predict On Test Data
y_pred = model.predict(X_test)

# Step 7: Check Accuracy
print("Model Accuracy:", accuracy_score(y_test, y_pred))

# Step 8: Predict New Patient
new_patient = [[58, 145, 250]]  # age=58, bp=145, chol=250
risk = model.predict(new_patient)

print("Predicted Risk (0=No, 1=Yes):", risk[0])
------------------------------------------------------------------
***Fraud Detection in Financial Transactions
# Step 1: Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Step 2: Load dataset
data = pd.read_csv("fraud_transactions.csv")

# Step 3: Select features (X) and target (y)
X = data[['amount', 'transaction_time', 'location_mismatch', 'international', 'device_change']]
y = data['fraud']

# Step 4: Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Step 5: Train Random Forest model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Step 6: Predict test data
y_pred = model.predict(X_test)

# Step 7: Show accuracy
print("Model Accuracy:", accuracy_score(y_test, y_pred))

# Step 8: Predict a new transaction
new_txn = [[6000, 1, 1, 1, 1]]   # high risk transaction
prediction = model.predict(new_txn)

print("Fraud Prediction (0=No, 1=Yes):", prediction[0])
--------------------------------------------------------
***Employee Attrition Prediction
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("employee_attrition.csv")

# Convert target variable to numeric
df["Attrition"] = df["Attrition"].map({"Yes": 1, "No": 0})

# Features & Target
X = df[["Satisfaction", "Performance", "Salary", "YearsAtCompany"]]
y = df["Attrition"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Random Forest Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
---------------------------------------------------------
***Air Quality Classification

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("air_quality.csv")

# Convert AQI labels to numbers
df["AQI_Level"] = df["AQI_Level"].map({"Good": 0, "Moderate": 1, "Unhealthy": 2})

# Features and target
X = df[["PM2.5", "PM10", "NO2", "SO2", "CO"]]
y = df["AQI_Level"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Random Forest Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
-----------------------------------------------------------
***Product Recommendation System
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("product_data.csv")

# Convert product labels to numbers
df["Preferred_Product"] = df["Preferred_Product"].map({
    "Electronics": 0,
    "Fashion": 1,
    "Groceries": 2
})

# Features and Target
X = df[["Browsing_Time (mins)", "Category_Views", "Past_Purchases", "Age"]]
y = df["Preferred_Product"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Random Forest Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
-----------------------------------------------------------
***Customer Segmentation for Marketing
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("customers.csv")

# Select features
X = df[["Age", "AnnualIncome", "SpendingScore"]]

# Create KMeans model (choose 3 clusters)
kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(X)

# Print cluster labels
print(df)

# Plot clusters (3D visualization – optional)
plt.scatter(df["AnnualIncome"], df["SpendingScore"], c=df["Cluster"])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation Using K-Means")
plt.show()
--------------------------------------------------------------
****Document Clustering for News Articles
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv("news.csv")

# Step 1: Convert text to TF-IDF vectors
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df["Article"])

# Step 2: Create K-Means clustering model (choose 3 clusters)
kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(X)

# Print results
print(df)
----------------------------------------------------------------
***Image Compression Using K-Means
pip install opencv-python scikit-learn matplotlib

import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load image
img = cv2.imread("image.jpg")       # Put your image name here
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# reshape image pixels to a 2D array
pixel_values = img.reshape((-1, 3))
pixel_values = np.float32(pixel_values)

# K-Means parameters
k = 8  # Number of colors after compression
kmeans = KMeans(n_clusters=k, random_state=42)
labels = kmeans.fit_predict(pixel_values)

# Replace each pixel with its cluster center
compressed_image = kmeans.cluster_centers_.astype("uint8")[labels]

# Reshape to original shape
compressed_image = compressed_image.reshape(img.shape)

# Show original vs compressed
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(img)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Compressed Image")
plt.imshow(compressed_image)
plt.axis("off")

plt.show()
-------------------------------------------------------------------------------
***Traffic Pattern Analysis
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("gps_data.csv")   # Use your dataset

# Select features: latitude, longitude, hour
X = data[['latitude', 'longitude', 'hour']]

# Apply K-Means clustering
k = 4   # You can choose more clusters if needed
kmeans = KMeans(n_clusters=k, random_state=42)
data['cluster'] = kmeans.fit_predict(X)

# Plot clusters using latitude & longitude
plt.figure(figsize=(8, 6))
plt.scatter(data['longitude'], data['latitude'], 
            c=data['cluster'], cmap='viridis')
plt.title("Traffic Congestion Zones")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

# Plot peak hours cluster-wise
plt.figure(figsize=(8, 5))
plt.hist(data['hour'], bins=24, color='gray')
plt.title("Traffic Density by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Vehicles")
plt.show()
-------------------------------------------------------------------
***Market Basket Analysis for Retail
pip install mlxtend

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Load dataset
data = pd.read_csv("transactions.csv")

# Convert string items to list
transactions = data['items'].apply(lambda x: x.split(", ")).tolist()

# Transaction Encoder
te = TransactionEncoder()
te_data = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_data, columns=te.columns_)

# Step 1: Find Frequent Itemsets
frequent_items = apriori(df, min_support=0.3, use_colnames=True)
print("Frequent Itemsets:")
print(frequent_items)

# Step 2: Generate Association Rules
rules = association_rules(frequent_items, metric="lift", min_threshold=1.0)
print("\nAssociation Rules:")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
------------------------------------------------------------------------------










