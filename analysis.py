$pyCode = @'
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Data Setup
data = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Retention_Rate': [72.19, 69.43, 72.81, 75.35]
}

df = pd.DataFrame(data)

# 2. Calculation
current_avg = df['Retention_Rate'].mean()
target = 85.0

print(f"Yearly Average: {current_avg:.2f}")

# 3. Visualization
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")
sns.lineplot(data=df, x='Quarter', y='Retention_Rate', marker='o')
plt.axhline(y=target, color='r', linestyle='--', label='Target')
plt.title('2024 Customer Retention Trends')
plt.savefig('retention_trend.png')
'@

Set-Content -Path analysis.py -Value $pyCode -Encoding UTF8
