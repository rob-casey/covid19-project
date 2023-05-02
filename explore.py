import plotly.express as px
from scipy.stats import ttest_ind
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
import plotly.graph_objs as go

def split_data(df):
    split_point = int(0.7*len(df))
    train = df[0:split_point]
    test = df[split_point:]
    return train, test

def viz_split():
    train, test = split_data(df)

    fig = px.line(df, x=df.index, y="cases", title="Train-Test Split of COVID-19 Cases")
    fig.update_traces(marker=dict(size=3), line=dict(width=1))
    fig.add_vline(x=train.index[-1], line_width=1, line_dash="dash", line_color="gray")
    fig.update_layout(xaxis_title="Date", yaxis_title="Number of Cases", legend_title="Dataset",
                      font=dict(family="Arial", size=12))
    fig.show()

def test_one(train):
    train['daily_cases'] = train['cases'].diff().fillna(0)
    df1 = train.copy()
    # divide the dataset into before and after the vaccination program
    before_vaccine = df1.loc['2020-03-01':'2021-01-15', 'daily_cases']
    after_vaccine = df1.loc['2021-01-16':, 'daily_cases']

    # perform t-test
    t_stat, p_val = ttest_ind(before_vaccine, after_vaccine)

    # print results
    print('t-statistic:', t_stat)
    print('p-value:', p_val)

def viz_one(train):
    df1 = train.copy()
    # Create a new column indicating if each date is before or after the vaccination program start date
    df1['vaccination_program'] = df1.index >= '2021-01-15'

    # Create a box plot to compare the distribution of daily cases before and after the vaccination program
    fig = px.box(df1, x='vaccination_program', y='daily_cases', color='vaccination_program', 
                 title='Daily Cases Before and After Vaccination Program')

    # Add significance level line at y=0 for visualization
    fig.add_shape(type='line', x0=-0.5, x1=1.5, y0=0, y1=0, 
                  line=dict(color='gray', width=1, dash='dash'))

    fig.show()

def test_two(train):
    df1 = train.copy()
    # Extract daily new cases by day of the week
    df1['day_of_week'] = df1.index.dayofweek
    weekdays = df1[df1['day_of_week'] < 5]['daily_cases']
    weekends = df1[df1['day_of_week'] >= 5]['daily_cases']

    # Perform two-sample t-test
    from scipy.stats import ttest_ind
    t, p = ttest_ind(weekdays, weekends, equal_var=False)

    print(f"t-statistic: {t:.2f}")
    print(f"p-value: {p:.4f}")

    return df1

def viz_two(df1):
    df2 = df1.copy()
    fig = px.box(df2, x="day_of_week", y="daily_cases", points="all", 
             title="Daily Cases by Weekday")

    fig.show()

def test_three(df1):
    result = adfuller(df1['daily_cases'])
    print('ADF Statistic: %f' % result[0])
    print('p-value: %f' % result[1])
    print('Critical Values:')
    for key, value in result[4].items():
        print('\t%s: %.3f' % (key, value))

def viz_three(df1):
    result = seasonal_decompose(df1['daily_cases'], model='additive')
    result.plot()
    plt.show()

def viz_four(df1):
    # Create rolling mean and standard deviation
    rolling_mean = df1['daily_cases'].rolling(window=7).mean()
    rolling_std = df1['daily_cases'].rolling(window=7).std()

    # Create traces for the time series, rolling mean, and rolling standard deviation
    trace1 = go.Scatter(x=df1.index, y=df1['daily_cases'], mode='lines', name='Time Series')
    trace2 = go.Scatter(x=df1.index, y=rolling_mean, mode='lines', name='Rolling Mean')
    trace3 = go.Scatter(x=df1.index, y=rolling_std, mode='lines', name='Rolling Standard Deviation')

    # Create figure
    fig = go.Figure(data=[trace1, trace2, trace3], layout=go.Layout(title='Time Series with Rolling Mean and Standard Deviation'))

    # Show figure
    fig.show()

