import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Import the data
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# 2. Clean the data by filtering out top 2.5% and bottom 2.5% of page views
lower_quantile = df['value'].quantile(0.025)
upper_quantile = df['value'].quantile(0.975)
df = df[(df['value'] >= lower_quantile) & (df['value'] <= upper_quantile)]


# 3. Draw Line Plot
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df['value'], color='red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    fig.savefig('line_plot.png')
    return fig


# 4. Draw Bar Plot
def draw_bar_plot():
    # Copy the dataframe to avoid modifying original
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    # Group by year and month and calculate average page views
    df_bar_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Order months correctly
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    df_bar_grouped = df_bar_grouped[month_order]

    # Draw bar plot
    fig = df_bar_grouped.plot(kind='bar', figsize=(12, 6)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    fig.savefig('bar_plot.png')
    return fig


# 5. Draw Box Plot
def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')
    df_box['month_num'] = df_box['date'].dt.month
    df_box = df_box.sort_values('month_num')

    fig, axes = plt.subplots(1, 2, figsize=(18, 6))

    # Year-wise box plot
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Month-wise box plot
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    fig.savefig('box_plot.png')
    return fig


# Example usage
if __name__ == "__main__":
    line_fig = draw_line_plot()
    line_fig.show()

    bar_fig = draw_bar_plot()
    bar_fig.show()

    box_fig = draw_box_plot()
    box_fig.show()
