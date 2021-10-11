import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': r'C:\Users\DeySholey\Desktop\Bikeshare-project\Data\chicago.csv',
              'new york city': r'C:\Users\DeySholey\Desktop\Bikeshare-project\Data\new_york_city.csv',
              'washington': r'C:\Users\DeySholey\Desktop\Bikeshare-project\Data\washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('Welcome to the Program')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''

    while city not in CITY_DATA.keys():
        print('\nWe have data for Chicago, New york city and Washington')
        print('Please enter city you will like to explore: ')

        city = input().lower()

        if city not in CITY_DATA.keys():
            print('\nPlease enter valid month')
            print('Restarting.......')
            continue

        print('You have chosen {}'.format(city.title()))
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3,
                  'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    
    while month not in MONTH_DATA.keys():
        print('\nPlease enter the month between January to June which you seek to explore: ')
        print('Enter all to view data for all months: ')
        
        month = input().lower()
        
        if month not in MONTH_DATA.keys():
            print('\nPlease enter valid month')
            print('Restarting.......')
            continue
        
        print('You have chosen {}'.format(month.title()))
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''

    while day not in DAY_DATA:
        print('\nPlease enter the day between Monday to Sunday: ')
        print('Enter all to view data for all days: ')

        day = input().lower()

        if day not in DAY_DATA:
            print('\nPlease enter valid day')
            print('Restarting.......')
            continue

        print('You have chosen {}'.format(day.title()))
        break

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
    #load data for city
    print('\nLoading data...')
    df = pd.read_csv(CITY_DATA[city])

    # Convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract Month and Day from Start Time to create new column
    df['Month'] = df['Start Time'].dt.month
    df['Day_of_week'] = df['Start Time'].dt.day_name()

    # Filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Month'] == month]

    # Filter by day
    if day != 'all':
        df = df[df['Day_of_week'] == day.title()]
        print(df)

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['Month'].mode()[0]

    print('\nMost popular month is: {}'.format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['Day_of_week'].mode()[0]

    print('\nMost popular day is: {}'.format(popular_day))

    # Extract hour from start time to create hour column
    df['Hour'] = df['Start Time'].dt.hour

    # TO DO: display the most common start hour
    popular_hour = df['Hour'].mode()[0]

    print('\nMost popular hour is: {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    print('\nMost popular start station is: {}'.format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    print('\nMost popular end station is: {}'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    # Concatenate both the start and end station columns to a single column
    df['Start to End Station'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')

    # Then display the most frequent
    popular_start_to_end_station = df['Start to End Station'].mode()[0]

    print('\nMost popular combination of start and end station is: {}'.format(popular_start_to_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print('\nTotal Trip duration is: {}'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print('\nMean Travel Time is: {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()

    print('\nUser type Count is: {}'.format(user_type))

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('\nThe gender count: {}'.format(gender_count))
    except:
        print('\nThere is no Gender for this City')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = df['Birth Year'].mode()[0]
        print('\nThe earliest birth year is: {}'.format(earliest))
        print('\nThe recent birth year is: {}'.format(recent))
        print('\nThe popular birth year is: {}'.format(common_year))
    except:
        print('\nThere is no year of birth for this City')


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
