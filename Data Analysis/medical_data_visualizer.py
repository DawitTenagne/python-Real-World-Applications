import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Import the data
df = pd.read_csv('medical_examination.csv')

# 2. Add 'overweight' column
# BMI = weight (kg) / (height (m))^2
df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = (df['BMI'] > 25).astype(int)
df.drop(columns='BMI', inplace=True)  # optional: remove temporary BMI column

# 3. Normalize data
# 0 = good, 1 = bad
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. Draw Categorical Plot
def draw_cat_plot():
    # 4a. Create DataFrame for cat plot
    df_cat = pd.melt(df,
                     id_vars='cardio',
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 4b. Group and reformat data
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']) \
                   .size() \
                   .reset_index(name='total')

    # 4c. Draw the catplot
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio',
                      data=df_cat, kind='bar').fig

    return fig

# 5. Draw Heat Map
def draw_heat_map():
    # 5a. Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 5b. Calculate correlation matrix
    corr = df_heat.corr()

    # 5c. Generate mask for upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 5d. Set up matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # 5e. Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', center=0, linewidths=.5, square=True, cbar_kws={"shrink": .5})

    return fig

# Example usage
if __name__ == "__main__":
    cat_fig = draw_cat_plot()
    cat_fig.show()

    heat_fig = draw_heat_map()
    heat_fig.show()
