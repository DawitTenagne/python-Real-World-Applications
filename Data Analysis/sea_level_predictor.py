import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# 1. Import the data
df = pd.read_csv('epa-sea-level.csv')

# 2. Create scatter plot
def draw_plot():
    fig, ax = plt.subplots(figsize=(12,6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data Points')

    # 3a. Line of best fit for all data
    slope_all, intercept_all, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = np.arange(df['Year'].min(), 2051)
    line_all = intercept_all + slope_all * years_all
    ax.plot(years_all, line_all, color='red', label='Fit: All Data')

    # 3b. Line of best fit from 2000 onward
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = np.arange(2000, 2051)
    line_recent = intercept_recent + slope_recent * years_recent
    ax.plot(years_recent, line_recent, color='green', label='Fit: 2000 Onward')

    # 4. Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # Save and return figure
    fig.savefig('sea_level_plot.png')
    return fig

# Example usage
if __name__ == "__main__":
    plot_fig = draw_plot()
    plot_fig.show()
