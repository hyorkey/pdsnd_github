import time
import statistics
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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington?\n").lower()
        if city in ["chicago", "new york city", "washington"]:
            print("You would like to see data for", city.title(), "! If this is incorrect exit the program now.\n")
            break
        else:
            print("Sorry, you've entered an invalid option. Please try again.\n")
        
    # TO DO: get user input for filtering
    filter_by = input("Would you like to filter the data by month, day, both or none?\n").lower()
    while filter_by not in ["month", "day", "both", "none"]:
        print("Sorry, you've entered an invalid option. Please try again.\n")
        filter_by = input("Would you like to filter the data by month, day, both or none?\n").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    if filter_by in ["month", "both"]:
        month = input("Which month would you like to view? Please enter January, February, March, April, May, or June.\n").lower()
        while month not in ["january", "february", "march", "april", "may", "june"]:
            print("Sorry, you've entered an invalid option. Please try again.\n")
            month = input("Which month would you like to view? Please enter January, February, March, April, May, or June.\n").lower()
    else:
        month = "all"
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    if filter_by in ["day", "both"]:
        day = input("Which day would you like to view? Please enter Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday.\n").lower()
        while day not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
            print("Sorry, you've entered an invalid option. Please try again.\n")
            day = input("Which day would you like to view? Please enter Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday.\n").lower()
    else:
        day = "all"


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day Of Week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['Month'] == month]
        
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['Day Of Week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is", df['Month'].value_counts().idxmax(), "\n")

    # TO DO: display the most common day of week
    print("The most common day of the weeek is", df['Day Of Week'].value_counts().idxmax(), "\n")

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    print("The most common start hour is", df['Hour'].value_counts().idxmax(), "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is", df['Start Station'].value_counts().idxmax(), "\n")

    # TO DO: display most commonly used end station
    print("The most commonly used end station is", df['End Station'].value_counts().idxmax(), "\n")

    # TO DO: display most frequent combination of start station and end station trip
    station_combinations = df.groupby(['Start Station', 'End Station'])
    common_combination = station_combinations.size().idxmax()
    print("The most frequent combination of start station and end station is", common_combination, "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time is", df['Trip Duration'].sum(), "\n")

    # TO DO: display mean travel time
    print("The average travel time is", df['Trip Duration'].mean(), "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("These are the amounts of each user type:\n", user_types)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_demigraphics(df):
    """Displays statistics on bikeshare users' demigraphics."""

    print('\nCalculating User Demigraphics...\n')
    start_time = time.time()

    # TO DO: Display counts of gender
    gender_types = df['Gender'].value_counts()
    print("These are the amounts of each gender:\n", gender_types)

    # TO DO: Display earliest, most recent, and most common year of birth
    print("The earliest birth year is:", int(df['Birth Year'].min()), "\n")
    print("The most recent birth year is:", int(df['Birth Year'].max()), "\n")
    print("The most common birth year is:", int(df['Birth Year'].mode()[0]), "\n")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def main():
    while True:
        city, month, day = get_filters()
        print("Here is the data you requested:")
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        if city in ["chicago", "new york city"]:
            user_demigraphics(df)
        else:
            print("There are no gender or birth year statistics for your city.\n")

        view_raw_data = input("Would you like to view the raw data? Enter yes or no.\n").lower()
        start_row = 0
        while view_raw_data == "yes":
            end_row = start_row + 5
            print(df.iloc[start_row:end_row])
            view_raw_data = input("Would you like to view more raw data? Enter yes or no.\n")
            if view_raw_data == "yes":
              start_row += 5
       
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
