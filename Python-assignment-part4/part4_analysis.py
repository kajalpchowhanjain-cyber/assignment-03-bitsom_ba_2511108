

import pandas as pd

df = pd.read_csv("students.csv")

print(df.head())
print(df.shape)
print(df.dtypes)
print(df.describe())

import matplotlib.pyplot as plt

subjects = ['math', 'science', 'english', 'history', 'pe']

df[subjects].mean().plot(kind='bar')
plt.title("Average Marks per Subject")
plt.savefig("plot1_bar.png")
plt.show()             

plt.hist(df['math'], bins=5)
plt.axvline(df['math'].mean(), linestyle='dashed')
plt.title("Math Score Distribution")
plt.savefig("plot2_hist.png")
plt.show()

df['avg_score'] = df[subjects].mean(axis=1)

pass_df = df[df['passed']==1]
fail_df = df[df['passed']==0]

plt.scatter(pass_df['study_hours_per_day'], pass_df['avg_score'], label="Pass")
plt.scatter(fail_df['study_hours_per_day'], fail_df['avg_score'], label="Fail")

plt.legend()
plt.title("Study Hours vs Avg Score")
plt.savefig("plot3_scatter.png")
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

X = df[['math','science','english','history','pe','attendance_pct','study_hours_per_day']]
y = df['passed']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

print("Train Accuracy:", model.score(X_train, y_train))
print("Test Accuracy:", model.score(X_test, y_test))