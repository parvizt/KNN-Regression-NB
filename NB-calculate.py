import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

# خواندن داده‌ها از فایل CSV با فرض وجود ستون‌های مشکل‌ساز
data = pd.read_csv('HouseNew.csv', encoding='utf-8')

# حذف سطرهای دارای مقدار NaN
data = data.dropna()

# تبدیل متغیر ادرس به متغیرهای دسته‌ای (با تبدیل به متغیرهای دامی)
data = pd.get_dummies(data, columns=["Address"])

# تقسیم داده‌ها به داده‌های آموزش و داده‌های تست
X = data.drop('Price', axis=1)  # ویژگی‌ها (بدون Price)
y = data['Price']  # برچسب (Price)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ایجاد مدل Naive Bayes
nb_model = GaussianNB()

# آموزش مدل با داده‌های آموزشی
nb_model.fit(X_train, y_train)

# پیش‌بینی قیمت‌ها با استفاده از داده‌های تست
y_pred = nb_model.predict(X_test)

# ارزیابی دقت مدل
accuracy = accuracy_score(y_test, y_pred)
print(f"دقت مدل: {accuracy * 100:.2f}%")

# نمایش توزیع برچسب‌ها با نمودار
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='Price')
plt.title("Distribution of Prices")
plt.xlabel("Price")
plt.ylabel("Count")
plt.show()
