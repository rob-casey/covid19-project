import pandas as pd

df_confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')
df_deaths = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv')

def wrangle_cases(df):
    # drop nulls
    df = df.dropna()
    # check
    if df.isnull().any().any():
        print('There are null values in the DataFrame')
    else:
        print('There are no null values in the DataFrame')
    # drop this value
    df = df.drop(df[df['Admin2'] == 'Unassigned'].index)
    # melt data
    df = df.melt(id_vars=['UID', 'iso2', 'iso3', 'code3', 'FIPS', 
                          'Admin2', 'Province_State', 'Country_Region', 
                          'Lat', 'Long_', 'Combined_Key'],
                          var_name='date', value_name='confirmed_cases')
    # drop this value
    df = df.drop(df[df['date'] == 'Population'].index)
    # drop columns
    df.drop(['UID', 'iso2', 'iso3', 'code3', 'FIPS', 'Country_Region', 
             'Lat', 'Long_', 'Combined_Key', 'Admin2'], axis=1, inplace=True)
    # convert date to datetime
    df['date'] = pd.to_datetime(df['date'])
    # set datetime to index
    df.set_index('date', inplace=True)
    # rename columns
    df = df.rename(columns={'confirmed_cases': 'cases', 'Province_State': 'state'})

    return df

def wrangle_deaths(df):
    # drop nulls
    df = df.dropna()
    # check
    if df.isnull().any().any():
        print('There are null values in the DataFrame')
    else:
        print('There are no null values in the DataFrame\n')
    # drop this value
    df = df.drop(df[df['Admin2'] == 'Unassigned'].index)

    # melt data
    df = df.melt(id_vars=['UID', 'iso2', 'iso3', 'code3', 'FIPS', 
                          'Admin2', 'Province_State', 'Country_Region', 
                          'Lat', 'Long_', 'Combined_Key'],
                          var_name='date', value_name='confirmed_cases')
    # drop this value
    df = df.drop(df[df['date'] == 'Population'].index)
    # convert date to datetime
    df['date'] = pd.to_datetime(df['date'])
    # set datetime to index
    df.set_index('date', inplace=True)
    # rename columns
    df = df.rename(columns={'confirmed_cases':'deaths', 'Province_State': 'state'})
    # drop columns
    df.drop(['UID', 'iso2', 'iso3', 'code3', 'FIPS', 'Country_Region', 
             'Lat', 'Long_', 'Combined_Key'], axis=1, inplace=True)
    print(df.head(5))
    
    return df

def nested_wrangle(df_cases, df_deaths):
    feature = df_deaths['deaths']
    df = pd.concat([df_cases, feature], axis=1)
    df = df[df['state'] == 'California']

    return df

def aggregate_data(df):
    df_agg = df.groupby(df.index).agg({'cases': 'sum', 'deaths': 'sum'})
    df = df_agg
    print(df.tail(5))

    return df