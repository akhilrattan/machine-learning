import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    accuracy_score
)

df = pd.read_csv("spam.csv",encoding="latin-1")
df = df[['v1','v2']]
df.columns =['label','message']

print(df.head())
print(df.info())
print(df.isnull().sum())

print(df['label'].value_counts())

plt.figure(figsize=(5,4))
sns.countplot(
    x='label',
    data = df
)
plt.title('spam vs ham messages')
plt.xlabel('messages')
plt.ylabel('count')
plt.show()

df['label'] = df['label'].map({
    'ham':0,
    'spam':1,
})
X = df['message']
y= df['label']

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(X)

X_train , X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
model = MultinomialNB()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"the accuracy scores are : {accuracy:.4f}")

cm = confusion_matrix(
    y_test,
    y_pred
)
plt.figure(figsize=(5,4))

sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=['Ham','Spam'],
    yticklabels=['Ham','Spam']
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")

plt.show()
print(classification_report(y_test,y_pred))

feature_names = vectorizer.get_feature_names_out()
spam_prob = model.feature_log_prob_[1]
ham_prob = model.feature_log_prob_[0]

difference = spam_prob - ham_prob

top_indices = difference.argsort()[-20:]
print("Top Predictive Spam Words:\n")

for i in reversed(top_indices):
    print(feature_names[i])

top_words = [feature_names[i] for i in reversed(top_indices)]
top_scores = [difference[i] for i in reversed(top_indices)]


plt.figure(figsize=(10,6))

plt.barh(top_words, top_scores)

plt.xlabel("Spam Score")
plt.title("Top Predictive Spam Words")

plt.gca().invert_yaxis()

plt.show()