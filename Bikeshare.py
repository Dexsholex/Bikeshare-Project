import time
import pandas as pd
import numpy as np

#Creating a dictionary containing the data sources for the three cities
CITY_DATA = {'chicago': "data/chicago.csv",
              'new york city': "data/new_york_city.csv",
              'washington': "data/washington.csv"}

#Function to figure out the filtering requirements of the user
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Args:
        None.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('Welcome to the Program')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # Initializing an empty city variable to store city choice from user
    # You will see this repeat throughout the program
    city = ''

    #Running this loop to ensure the correct user input gets selected else repeat
    while city not in CITY_DATA.keys():
        print('\nWe have data for Chicago, New york city and Washington')
        print('Please enter city you will like to explore: ')

        # Taking user input and converting into lower to standardize them
        # You will find this happening at every stage of input throughout this
        city = input().lower()

        if city not in CITY_DATA.keys():
            print('\nPlease enter valid month')
            print('Restarting.......')
            continue

        print('You have chosen {}'.format(city.title()))
        break

    # TO DO: get user input for month (all, january, february, ... june)
    # Creating a dictionary to store all the months including the 'all' option
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
    # Creating a list to store all the days including the 'all' option
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
    
    # Returning the city, month and day selections
    return city, month, day

#Function to load data from .csv files
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

    # Filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # Filter by month to create the new dataframe
        df = df[df['Month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        #Filter by day of week to create the new dataframe
        df = df[df['Day_of_week'] == day.title()]
    # Returns the selected file as a dataframe (df) with relevant columns
    return df

#Function to calculate all the time-related statistics for the chosen data
def time_stats(df):
    """Displays statistics on the most frequent times of travel.

    Args:
        param1 (df): The data frame you wish to work with.
    
    Returns:
        None.
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # Uses mode method to find the most popular month 
    popular_month = df['Month'].mode()[0]

    print('\nMost popular month is: {}'.format(popular_month))

    # TO DO: display the most common day of week
    # Uses mode method to find the most popular day of week
    popular_day = df['Day_of_week'].mode()[0]

    print('\nMost popular day is: {}'.format(popular_day))

    # Extract hour from start time to create hour column
    df['Hour'] = df['Start Time'].dt.hour

    # TO DO: display the most common start hour
    # Uses mode method to find the most popular hour
    popular_hour = df['Hour'].mode()[0]

    print('\nMost popular hour is: {}'.format(popular_hour))

    #Prints the time taken to perform the calculation
    #You will find this in all the functions involving any calculation
    #throughout this program
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#Function to calculate station related statistics
def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    
    Args:
        param1 (df): The data frame you wish to work with.
    
    Returns:
        None.
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # Uses mode method to find the most common start station
    popular_start_station = df['Start Station'].mode()[0]

    print('\nMost popular start station is: {}'.format(popular_start_station))

    # TO DO: display most commonly used end station
    # Uses mode method to find the most common end station
    popular_end_station = df['End Station'].mode()[0]

    print('\nMost popular end station is: {}'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    # Uses str.cat to combine two columsn in the df
    # Assigns the result to a new column 'Start To End'
    # Uses mode on this new column to find out the most common combination
    # of start and end stations
    df['Start to End Station'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')

    # Then display the most frequent start and end station
    popular_start_to_end_station = df['Start to End Station'].mode()[0]

    print('\nMost popular combination of start and end station is: {}'.format(popular_start_to_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Function for trip duration related statistics
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # Uses sum method to calculate the total trip duration
    total_travel_time = df['Trip Duration'].sum()

    print('\nTotal Trip duration is: {}'.format(total_travel_time))

    # TO DO: display mean travel time
    # Calculating the average trip duration using mean method
    mean_travel_time = df['Trip Duration'].mean()

    print('\nMean Travel Time is: {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Function to calculate user statistics
def user_stats(df):
    """Displays statistics on bikeshare users.

    Args:
        param1 (df): The data frame you wish to work with.

    Returns:
        None.
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # The total users are counted using value_counts method
    # They are then displayed by their types (e.g. Subscriber or Customer)
    user_type = df['User Type'].value_counts()
    user_type = df['User Type'].value_counts()

    print('\nUser type Count is: {}'.format(user_type))

    # TO DO: Display counts of gender
    # This try clause is implemented to display the numebr of users by Gender
    # However, not every df may have the Gender column, hence this...
    try:
        gender_count = df['Gender'].value_counts()
        print('\nThe gender count: {}'.format(gender_count))
    except:
        print('\nThere is no Gender for this City')

    # TO DO: Display earliest, most recent, and most common year of birth
    # Similarly, this try clause is there to ensure only df containing
    # Birth Year column are displayed
    # The earliest birth year, most recent birth year and the most common
    # birth years are displayed
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


#Main function to call all the previous functions
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
