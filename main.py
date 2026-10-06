import pandas as pd
import matplotlib.pyplot as plt

# 1. قراءة الملف المدمج النظيف
df = pd.read_csv("fitbit_cleaned_merged.csv")

# 2. إنشاء رسم بياني (Scatter Plot) لإظهار العلاقة بين الخطوات والنوم
plt.figure(figsize=(8, 5))
plt.scatter(df['TotalSteps'], df['TotalMinutesAsleep'], color='teal', alpha=0.7, edgecolors='k')

# 3. إضافات وتحسين الشكل الجمالي للرسم البياني
plt.title("Relationship Between Daily Steps and Sleep Duration", fontsize=14, fontweight='bold')
plt.xlabel("Total Daily Steps", fontsize=12)
plt.ylabel("Total Minutes Asleep", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)

# 4. حفظ الرسم البياني كصورة للمشروع
plt.savefig("steps_vs_sleep.png", dpi=300, bbox_inches='tight')
print(" Chart generated successfully and saved as 'steps_vs_sleep.png'!")

# 5. عرض الرسمة على الشاشة
plt.show()