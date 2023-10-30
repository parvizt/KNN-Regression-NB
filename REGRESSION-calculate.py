import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer

# خواندن داده‌ها از فایل CSV
data = pd.read_csv('HouseNew.csv')

# انتخاب ویژگت‌های ورودی و خروجی برای مدل رگرسیون
X = data[['Elevator', 'Floor', 'Area', 'Parking', 'Room', 'Warehouse', 'YearOfConstruction']]
y = data['Price']

# ایجاد یک متغیر Imputer با استفاده از مقدار میانگین برای پر کردن مقادیر NaN
imputer = SimpleImputer(strategy='mean')

# پر کردن مقادیر NaN در داده‌ها
X = imputer.fit_transform(X)

# ایجاد مدل رگرسیون خطی
regressor = LinearRegression()

# آموزش مدل با داده‌ها
regressor.fit(X, y)

# محاسبه پیش‌بینی‌ها
predictions = regressor.predict(X)

# چاپ پیش‌بینی‌ها
print("Predictions:")
for prediction in predictions:
    print(prediction)

# رسم نمودار
plt.scatter(y, predictions)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual Prices vs. Predicted Prices")
plt.show()
