import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def generate_chart():
    # 1. Generate Synthetic Data for Goodwin and Sons
    # Setting seed for reproducibility
    np.random.seed(42)
    n_points = 200

    # Generating data: Response times (in hours) for different channels
    # Email: High variance, longer response times
    email_data = np.random.normal(loc=24, scale=8, size=n_points)
    # Call Center: Medium variance, faster response times
    phone_data = np.random.normal(loc=8, scale=3, size=n_points)
    # Chat: Low variance, immediate response times
    chat_data = np.random.normal(loc=2, scale=1, size=n_points)

    # Create DataFrame
    data = {
        'Email': email_data,
        'Call Center': phone_data,
        'Live Chat': chat_data
    }
    
    # Melt dataframe for Seaborn (Long format)
    df = pd.DataFrame(data)
    df_melted = df.melt(var_name='Support Channel', value_name='Response Time (Hours)')
    
    # Clean data (no negative time)
    df_melted['Response Time (Hours)'] = df_melted['Response Time (Hours)'].clip(lower=0)

    # 2. Setup Figure Dimensions
    # 8 inches * 64 DPI = 512 pixels
    plt.figure(figsize=(8, 8))

    # 3. Apply Professional Styling
    sns.set_style("whitegrid")
    sns.set_context("talk") # Increases font size for presentations/executive summaries

    # 4. Create the Violin Plot
    # inner='quartile' adds lines for the quartiles inside the violins
    plot = sns.violinplot(
        data=df_melted,
        x='Support Channel',
        y='Response Time (Hours)',
        palette="viridis",
        inner="quartile",
        linewidth=1.5,
        density_norm='width' # Ensures width represents density relative to other categories
    )

    # 5. Add Titles and Labels
    plt.title('Goodwin & Sons: Customer Support\nResponse Time Distribution', 
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Support Channel', fontsize=12, labelpad=10)
    plt.ylabel('Response Time (Hours)', fontsize=12, labelpad=10)

    # 6. Save the Chart
    # Uses tight_layout to fit elements within the 8x8 figure, then saves at 64dpi
    plt.tight_layout()
    plt.savefig('chart.png', dpi=64)
    print("Chart saved successfully as chart.png (512x512 pixels)")

if __name__ == "__main__":
    generate_chart()
