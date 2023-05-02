# COVID-19 Time Series Project
## Analyzing COVID-19 daily cases in California from March 2020 to May 2023

## Introduction
The goal of this project is to analyze the daily COVID-19 cases in California from March 2020 to May 2023. We use rolling mean and standard deviation to highlight any trends or patterns in the data and identify changes in the variability of the data over time.

## Data Source
Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE) COVID-19 Data Repository. 
The data frames contain time series data on the confirmed COVID-19 cases and deaths in the United States, with a breakdown by state and county.

## Project Goals
* Analyze the daily COVID-19 cases in California to identify trends and patterns in the data.
* Use rolling mean and standard deviation to smooth out the data and identify changes in variability.
* Visualize the data and findings in a clear and concise manner.

## Data Dictionary

| Feature | Definition | Type |
|:--------|:-----------|:-------
|**UID**| Unique Identifier for each row |*int*|
|**iso2**| Two letter code for countries |*string*|
|**iso3**| Three letter code for countries |*string*|
|**code3**| Three letter code for countries	integer |*int*|
|**FIPS**| Federal Information Processing Standards code that uniquely identifies counties within the US |*float*|
|**Admin2**| County name |*string*|
|**Province_State**| Province, state or dependency name |*string*|
|**Country_Region**| Country, region or sovereignty name |*string*|
|**Lat**| Latitude |*float*|
|**Long**| Longitude |*float*|


## Methods Used
* Data cleaning and preparation using Python and Pandas.
* Data analysis and visualization using Python libraries including Matplotlib and Seaborn.
