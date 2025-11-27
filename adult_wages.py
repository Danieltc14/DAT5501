
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import precision_score, recall_score

# 1. Load the dataset
columns = ["age","workclass","fnlwgt","education","education_num","marital_status",
           "occupation","relationship","race","sex","capital_gain","capital_loss",
           "hours_per_week","native_country","income"]

data = pd.read_csv("adult.txt", names=columns, sep=",", skipinitialspace=True)

# 2. Handle missing values
data = data.replace('?', pd.NA).dropna()

# 3. Convert categorical data to numbers
X = pd.get_dummies(data.drop("income", axis=1))
y = (data["income"] == ">50K").astype(int)  # 1 if >50K else 0

# 4. Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# 5. Train a Decision Tree
model = DecisionTreeClassifier(max_depth=5)
model.fit(X_train, y_train)

# 6. Predict and evaluate
y_pred = model.predict(X_test)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("Precision:", round(precision, 2))
print("Recall:", round(recall, 2))
