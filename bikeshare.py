import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

"""
    Asks user to specify a city, month, and day to analyze.

    Returns:
       (str) city - name of the city to analyze
       (str) month - name of the month to filter by, or "all" to apply no month filter
       (str) day - name of the day of week to filter by, or "all" to apply no day filter
"""
print('Hello! Let\'s explore some US bikeshare data!')
 
    # get user input for city (chicago, new york city, washington). 
def city_input():
    city = input("Please enter what cities data you would like to view (chicago, new york city, washington): ")
    city = city.lower()
    while city not in ('all', 'chicago', 'new york city', 'washington'):
        print("\nSorry, please enter a valid city name (all, chicago, new york city, washington)\n")
        city = input("Please enter what cities data you would like to view (chicago, new york city, washington): ")
    return(city)
  
    
    # get user input for month (all, january, february, ... , june)
def month_input():
    month = input("\nPlease enter a month you would like to view data for (type \"all\" for all months): ")
    month = month.lower()
    while month.lower() not in ('all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'):
        print("\nSorry, please enter a valid month (all, january, february, march, april, may, june, july, august, september, october, november, december)\n")
        month = input("Please enter a month you would like to view data for (type \"all\" for all months): ")
    return(month)
 
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
def day_input():
    day = input("\nPlease enter a day you would like to view data for (type \"all\" for all days): ")
    day = day.lower()
    while day.lower() not in ('all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'):
        print("\nSorry, please enter a valid month (all, sunday, monday, tuesday, wednesday, thursday, friday, saturday)\n")
        day = input("Please enter a day you would like to view data for (type \"all\" for all days): ")
    return(day)

   
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
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1

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
    popular_month = df['month'].mode()[0]
    print('Most Frequent month:', popular_month)

    # TO DO: display the most common day of week
    df['week'] = df['Start Time'].dt.week
    popular_week = df['week'].mode()[0] 
    print('Most Frequent week:', popular_week)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most Popular Start Station:',df['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
    print('Most Popular End Station:',df['End Station'].value_counts().idxmax())
    
    # TO DO: display most frequent combination of start station and end station trip
    df['st_ed_station'] = df['Start Station'] + ' to ' + df['End Station']
    trip = df['st_ed_station'].mode()[0]
    print('Most Popular Trip:', trip)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df = pd.DataFrame(df,columns=['Trip Duration'])
    total_travel_time = df.sum(axis=0)
    print ("Total travel time:\n",int(total_travel_time // 60),"Hours",int(total_travel_time % 60), "Minutes")

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('\nMean Travel Time:',int(mean_travel // 60),"Hours",int(mean_travel % 60), "Minutes")

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    try:
        user_gender_count = df['Gender'].value_counts()
        print('\n',user_gender_count)
    except KeyError:
        print('\nNo "Gender" data to display gender count.')
      
    # TO DO: Display earliest, most recent, and most common year of birth   
    try:
        birth_yr_min = df['Birth Year'].min()
        print('\nEarliest Birth Year:',int(birth_yr_min))
    except KeyError:
        print('\nNo "Birth Year" data to calculate most earliest birth year.')
        
    
    try:
        birth_yr_max = df['Birth Year'].max()
        print('\nMost Recent Birth Year:',int(birth_yr_max))
    except KeyError:
        print('\nNo "Birth Year" data to calculate most recent birth year.')
   
    
    try:
        birth_yr_mode = df['Birth Year'].mode()
        print('\nMost Common Birth Year:',int(birth_yr_mode))
    except KeyError:
        print('\nNo "Birth Year" data to calculate most common birth year.')
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # ask user if they want to view 5 lines of raw data
def raw_data(df):
    data_choice = input("\nWould you like to see 5 lines of Raw Data (yes/no)? ")
    if data_choice.lower() == 'yes': 
        print(df.iloc[:5])

            
def main():
    city = ""
    month = ""
    day = ""
    
    while True:
        city = city_input()
        month = month_input()
        day = day_input()
        df = load_data(city, month, day)
                
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)  
        raw_data(df)
        
        print(time_stats)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()