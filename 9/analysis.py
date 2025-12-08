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
gap = target - current_avg

print(f"Yearly Average: {current_avg:.2f}")
print(f"Gap to Target: {gap:.2f}")

# 3. Visualization
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")

# Plotting the trend line
sns.lineplot(data=df, x='Quarter', y='Retention_Rate', marker='o', linewidth=2.5, color='#2E86C1', label='Current Retention')

# Plotting the target benchmark
plt.axhline(y=target, color='#E74C3C', linestyle='--', linewidth=2, label='Industry Target (85%)')

# Annotating values
for x, y in zip(df['Quarter'], df['Retention_Rate']):
    plt.text(x, y + 0.5, f'{y}%', ha='center', fontweight='bold')

plt.title('2024 Customer Retention Trends vs Industry Target', fontsize=14, pad=20)
plt.ylabel('Retention Rate (%)')
plt.ylim(60, 90)
plt.legend(loc='lower right')

# Highlight the Gap area
plt.fill_between(df['Quarter'], df['Retention_Rate'], target, color='red', alpha=0.1)
plt.text(1.5, 80, f'Performance Gap\nAvg: {current_avg:.2f}% vs Target: {target}%', 
         ha='center', fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout()
plt.savefig('retention_trend.png')
plt.show()
