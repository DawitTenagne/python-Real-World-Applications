import pandas as pd

def analyze_data():
    # Read the dataset
    df = pd.read_csv('adult.data.csv')  # Make sure your CSV file is named correctly

    # 1. How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. What is the percentage of people who have a Bachelor's degree?
    total_people = len(df)
    bachelors_count = len(df[df['education'] == 'Bachelors'])
    percentage_bachelors = round((bachelors_count / total_people) * 100, 1)

    # 4. Percentage of people with advanced education (Bachelors, Masters, Doctorate) making >50K
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df[df['education'].isin(advanced_education)]
    higher_education_rich = round(
        (len(higher_education[higher_education['salary'] == '>50K']) / len(higher_education)) * 100, 1
    )

    # 5. Percentage of people without advanced education making >50K
    lower_education = df[~df['education'].isin(advanced_education)]
    lower_education_rich = round(
        (len(lower_education[lower_education['salary'] == '>50K']) / len(lower_education)) * 100, 1
    )

    # 6. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # 7. Percentage of people who work minimum hours per week and earn >50K
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage_min_workers = round(
        (len(min_workers[min_workers['salary'] == '>50K']) / len(min_workers)) * 100, 1
    )

    # 8. Country with highest percentage of people earning >50K
    country_counts = df['native-country'].value_counts()
    rich_country_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    highest_earning_country = (rich_country_counts / country_counts * 100).idxmax()
    highest_earning_country_percentage = round(
        (rich_country_counts / country_counts * 100).max(), 1
    )

    # 9. Most popular occupation for those who earn >50K in India
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    # Return results in a dictionary
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage_min_workers': rich_percentage_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# Example usage
if __name__ == "__main__":
    results = analyze_data()
    for key, value in results.items():
        print(f"{key}: {value}")
