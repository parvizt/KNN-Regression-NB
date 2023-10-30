import tkinter as tk
from tkinter import ttk
import subprocess
import random

# تابع اجرای کد KNN محاسبه
def run_knn_calculation():
    subprocess.Popen(['python', 'knn-calculate.py'])

# تابع اجرای کد Regression
def run_regression_calculation():
    subprocess.Popen(['python', 'REGRESSION-calculate.py'])

# تابع اجرای کد NB
def run_nb_calculation():
    subprocess.Popen(['python', 'NB-calculate.py'])

# تابع تولید رنگ تصادفی
def random_color():
    r = lambda: random.randint(0, 255)
    return f'#{r():02X}{r():02X}{r():02X}'

# ایجاد رابط کاربری
root = tk.Tk()
root.title("پیش‌بینی قیمت ملک")

# تنظیم اندازه پنجره
root.geometry("400x300")

# تنظیم رنگ پنجره به مشکی
root.configure(bg="black")

# ایجاد ویجت‌ها
elevator_label = tk.Label(root, text="Elevator", bg="black", fg="white")
elevator_radio = ttk.Combobox(root, values=["True", "False"])
floor_label = tk.Label(root, text="Floor", bg="black", fg="white")
floor_combobox = ttk.Combobox(root, values=["-1", "0", "1", "2"] + list(map(str, range(30)))
, )
area_label = tk.Label(root, text="Area", bg="black", fg="white")
area_combobox = ttk.Combobox(root, values=["0-50", "51-100", "101-150", "151-200", "200+"], )
parking_label = tk.Label(root, text="Parking", bg="black", fg="white")
parking_radio = ttk.Combobox(root, values=["True", "False"])
room_label = tk.Label(root, text="Room", bg="black", fg="white")
room_combobox = ttk.Combobox(root, values=["1", "2", "3", "4", "5+"], )
price_label = tk.Label(root, text="Price", bg="black", fg="white")
price_combobox = ttk.Combobox(root, values=["50000-100000", "100000-150000", "150000-200000", "200000+"], )
warehouse_label = tk.Label(root, text="Warehouse", bg="black", fg="white")
warehouse_radio = ttk.Combobox(root, values=["True", "False"])
year_label = tk.Label(root, text="Year of Construction", bg="black", fg="white")
year_combobox = ttk.Combobox(root, values=["1395-1396", "1396-1397", "1397-1398", "1398-1399", "1399-1400", "1400-1401"])

# ایجاد ویجت Label برای نمایش متن قبل از دکمه‌ها
frame_label = tk.Label(root, text="Choose an Algorithm:", bg="black", fg="white")

# ایجاد ویجت‌های دکمه
knn_button = tk.Button(root, text="KNN", command=run_knn_calculation)
regression_button = tk.Button(root, text="REGRESSION", command=run_regression_calculation)
nb_button = tk.Button(root, text="NB", command=run_nb_calculation)

# تولید رنگ‌های تصادفی برای دکمه‌ها
button_colors = [random_color() for _ in range(3)]

# نمایش ویجت‌ها در رابط کاربری
elevator_label.grid(row=0, column=0)
elevator_radio.grid(row=0, column=1)
floor_label.grid(row=1, column=0)
floor_combobox.grid(row=1, column=1)
area_label.grid(row=2, column=0)
area_combobox.grid(row=2, column=1)
parking_label.grid(row=3, column=0)
parking_radio.grid(row=3, column=1)
room_label.grid(row=4, column=0)
room_combobox.grid(row=4, column=1)
price_label.grid(row=5, column=0)
price_combobox.grid(row=5, column=1)
warehouse_label.grid(row=6, column=0)
warehouse_radio.grid(row=6, column=1)
year_label.grid(row=7, column=0)
year_combobox.grid(row=7, column=1)
frame_label.grid(row=8, column=0, columnspan=2)
knn_button.grid(row=11, column=0, columnspan=1)
regression_button.grid(row=11, column=1, columnspan=1)
nb_button.grid(row=11, column=2, columnspan=1)

# تنظیم رنگ دکمه‌ها با استفاده از اندیس رنگ‌های تصادفی
knn_button.configure(bg=button_colors[0])
regression_button.configure(bg=button_colors[1])
nb_button.configure(bg=button_colors[2])

# نمایش رابط کاربری
root.mainloop()
