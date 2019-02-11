import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('\nWould you like to see Chicago, New York City or Washington) \n').lower()
    print (city)

    while True: 
        frageeins = input('\nIs this the correct city (yes/no):')
        if frageeins.lower()==('yes'):
            break 
        else: city = input('OK, let us look at the city again.\nFor which city would you like to see the data? (Chicago, New York City, Washington) \n').lower()
    print('thank, let us search for', city)
    
    # get user input for month (all, january, february, ... , june)
    month = input ('\nWhich month? January, February, March, April, May, or June or all?\n').lower()
    print ('I understood:', month)
    while True: 
        fragezwo=input('\nIs this the correct selection (yes/no):')
        if fragezwo.lower()==('yes'):
            break 
        else: month = input('OK, let us look at the month again')
    print('OK.I noted:', month)
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('Are you interested in a particular day of the week or all?').lower()
    while True: 
        if day==('all'):
            break
        else: 
            fragedrei=input('Is the day correct ? (yes/no)')
        if fragedrei.lower()==('yes'):
            break
    print ('OK, I noted:',day)
    

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
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month
    
    # extract month from the Start Time column to create an month column
    df['month'] = df['Start Time'].dt.month
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # find the most common month
    common_month = df['month'].mode()[0]

    print('Most common month:', common_month)

    # display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    # find the most common day
    common_day = df['day_of_week'].mode()[0]

    print('Most common day:', common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour

    common_hour = df['hour'].mode()[0]

    print('Most common hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print ('most commonly used start station:',df['Start Station'].mode()[0])

    # display most commonly used end station
    print ('most commonly used end station:',df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df_count = df.groupby(['Start Station','End Station']).size().reset_index(name='count')
    print('most frequent combination of stations\n:',df_count.max())
    
    print("\nThis took %s seconds." % (time.time() - start_time))


    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nTotal travel time:', total_travel_time)

    # display mean travel time
    mean_trip_duration = df['Trip Duration'].mean()
    print('Mean travel Time:', mean_trip_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types are split in:\n',user_types)

    # Display counts of gender
    gender = df['Gender'].value_counts()
    print('Gender is split in:\n',gender)

    # Display earliest, most recent, and most common year of birth
    print('earliest year of birth is:',df['Birth Year'].min())
    print('most recent year of birth is:',df['Birth Year'].max())
    print('most common year is:',df['Birth Year'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()