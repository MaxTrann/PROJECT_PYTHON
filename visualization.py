import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
data = pd.read_csv('student_sleep_patterns.csv')

# Thiết lập bảng màu và kiểu cho biểu đồ
sns.set(style="whitegrid")

# 1. Phân phối thời gian ngủ - Histogram với màu xanh
plt.figure(figsize=(10, 6))
sns.histplot(data['Sleep_Duration'], kde=True, color="blue")
plt.title("Distribution of Sleep Duration")
plt.xlabel("Sleep Duration (hours)")
plt.ylabel("Frequency")
plt.show()

# 2. Thời gian ngủ theo giới tính và năm học - Boxplot với bảng màu Set3
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x="Gender", y="Sleep_Duration", hue="University_Year", palette="Set3")
plt.title("Sleep Duration by Gender and University Year")
plt.xlabel("Gender")
plt.ylabel("Sleep Duration (hours)")
plt.show()

# 3. Mối quan hệ giữa thời gian ngủ và chất lượng giấc ngủ - Scatter Plot với bảng màu coolwarm
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x="Sleep_Duration", y="Sleep_Quality", hue="Sleep_Quality", palette="coolwarm")
plt.title("Sleep Duration vs. Sleep Quality")
plt.xlabel("Sleep Duration (hours)")
plt.ylabel("Sleep Quality")
plt.show()

# 4. Chất lượng giấc ngủ trung bình theo năm học - Bar Plot với bảng màu magma
plt.figure(figsize=(10, 6))
sns.barplot(data=data, x="University_Year", y="Sleep_Quality", palette="magma")
plt.title("Average Sleep Quality by University Year")
plt.xlabel("University Year")
plt.ylabel("Average Sleep Quality")
plt.show()

# 5. Phân phối thời gian học - Histogram với màu xanh lá cây
plt.figure(figsize=(10, 6))
sns.histplot(data['Study_Hours'], kde=True, color="green")
plt.title("Distribution of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Frequency")
plt.show()

# 6. Phân phối hoạt động thể chất - Histogram với màu đỏ
plt.figure(figsize=(10, 6))
sns.histplot(data['Physical_Activity'], kde=True, color="red")
plt.title("Distribution of Physical Activity")
plt.xlabel("Physical Activity (minutes)")
plt.ylabel("Frequency")
plt.show()

# 7. Thời gian bắt đầu ngủ trong tuần và cuối tuần - Boxplot với bảng màu Spectral
plt.figure(figsize=(10, 6))
sns.boxplot(data=data[['Weekday_Sleep_Start', 'Weekend_Sleep_Start']].melt(), x='variable', y='value', palette="Spectral")
plt.title("Weekday vs. Weekend Sleep Start")
plt.xlabel("Day Type")
plt.ylabel("Sleep Start Time (24-hour)")
plt.show()

# 8. Thời gian bắt đầu và kết thúc giấc ngủ trong tuần - Scatter Plot với bảng màu coolwarm
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x="Weekday_Sleep_Start", y="Weekday_Sleep_End", hue="Weekday_Sleep_End", palette="coolwarm")
plt.title("Weekday Sleep Start vs. End")
plt.xlabel("Sleep Start Time (24-hour)")
plt.ylabel("Sleep End Time (24-hour)")
plt.show()

# 9. Thời gian học và thời gian ngủ - Scatter Plot với bảng màu viridis
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x="Study_Hours", y="Sleep_Duration", hue="Sleep_Duration", palette="viridis")
plt.title("Study Hours vs. Sleep Duration")
plt.xlabel("Study Hours")
plt.ylabel("Sleep Duration (hours)")
plt.show()
