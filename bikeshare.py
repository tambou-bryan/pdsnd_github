import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
city_list=["chicago","new york city","washington"]
month_list=["all","january","february","march","april","may","june"]
day_list=["all","monday","tuesday","thursday","friday","saturday","sunday"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data! \n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city =input("enter the city \n").lower()
    while city not in city_list:
        city=input("enter a good value of city chicago, new york city or washington \n").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month=input("enter the month all, january, february, ... , june \n").lower()
    while month not in month_list:
        month=input("enter a good value of month \n").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("enter the day all, monday, tuesday, ... sunday \n").lower()
    while day not in day_list:
        day=input("enter a good value of day \n").lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = month_list.index(month) 

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month from the Start Time column to create an month column
    df['month'] = df['Start Time'].dt.month

    # find the most popular month
    popular_month = df['month'].mode()[0]

    print('Most Popular Start month:', popular_month)


    # TO DO: display the most common day of week
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month from the Start Time column to create an month column
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # find the most popular month
    popular_day = df['day_of_week'].mode()[0]

    print('Most Popular Startday:', popular_day)   

    # TO DO: display the most common start hour
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['day'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['day'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().head(1)
    print("most commonly used start station: ",start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().head(1)
    print("most commonly used end station: ",end_station)

    # TO DO: display most frequent combination of start station and end station trip
    user_types = df.groupby(['Start Station','End Station'])['Start Time'].value_counts().head(1)
    print(user_types)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['hour'] = df['Start Time'].dt.hour
    print("total travel time: ",df['hour'].sum())
    # TO DO: display mean travel time
    df['hour'] = df['Start Time'].dt.hour
    print("mean travel time: ",df['hour'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df.groupby(["User Type"])["Start Time"].count()
    print(user_types)

    # TO DO: Display counts of gender
    try:
        gender_types = df.groupby(["Gender"])["Start Time"].count()
        print(gender_types)
    except:
        print("gender column don't exist in this city")

    # TO DO: Display earliest, most recent, and most common year of birth

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # TO DO: Display line of brut data (5 lines to 5)
    
def display_raw_data(df):
    i=input("You want to see 5 lines of raw data ? yes/no: ").lower()
    count=5
    y=True
    while y:
        if i=="no":
            break
        else:
            print(df.head(count))
            count=count+5
            i=input("You want to see 5 lines of raw data ? yes/no: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no. \n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
